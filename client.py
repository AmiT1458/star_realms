import socket
import threading

name = input("your name -> ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        server_ip = input("IP of the server -> ")
        client.connect((server_ip, 65432))
        client.send(name.encode("utf-8"))
        break
    except:
        print("wrong ip address \n")

def receive():
    while True:
        try:
            msg = client.recv(1024).decode("utf-8")
            if f"{name}: " in msg:
                pass
            else:
                print(f"{msg}")
        except:
            print("server does not respond :(")
            client.close()
            

def write():
    while True:
        msg = f"\n{name}: {input('send-> ')}\n"
        if  f"{name}:" == msg:
            pass
        else:
            client.send(msg.encode("utf-8"))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()

receive_thread.join()
write_thread.join()

