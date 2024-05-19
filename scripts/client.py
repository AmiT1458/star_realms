import socket
import pickle
import threading
from cards_data import server

PORT = 65432  # Same port as server

allowed_letters = "qwertyuiopasdfghjklzxcvbnm1234567890"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
thread_alive = True
is_connection = False
message = ''

def check_allow_name(name):
    name_allowed = False
    while not name_allowed:
        if any((c in allowed_letters) for c in name):
            name_allowed = True
        else:
            name_allowed = False
            server("\nplease enter a legal name\n")

    return name_allowed


def send_name(name) -> bool:
    if check_allow_name(name):
        client_socket.sendall(name.encode())  # Send name to server on connection
        server('Name entered!')
        return True

    else:
        server('name was not entered.. try a different one')
        return False


def send_msg(msg) -> bool:
    data = pickle.dumps(f' {msg}')
    try:
        client_socket.sendall(data)  # Send pickled data
        return True
    except ConnectionError:
        return False


def receive_msg():
    global message
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        # Unpickle received data
        message = pickle.loads(data)
        server(message)


def connect(host):
    global is_connection
    HOST = host
    try:
        client_socket.connect((HOST, PORT))
        server(f"Connected to server {HOST}:{PORT}")
        is_connection = True
    except ConnectionError:
        server("Connection failed.")


def start_receive():
    global recive_thread
    recive_thread = threading.Thread(target=receive_msg)
    recive_thread.start()


def disconnect():
    global thread_alive
    try:
        thread_alive = False
        client_socket.close()
        server("disconnected")
    except:
        pass


if __name__ == "__main__":
    connect(input("ip address: "))
    send_name(input("name: "))
    start_receive()
    while True:
        send_msg(input())
