import threading
import socket
from better_profanity import profanity

host = "localhost"
port = 65432
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
names = []

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle(client):
    while True:
        try:
            index = clients.index(client)
            name = names[index]
            msg = client.recv(1024)
            if msg == f"{name}:":
                pass
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast(f"\n{name} left the chat :(".encode("utf-8"))
            names.remove(name)
            break

def recive():
    while True:
        client, address = server.accept()
        print(f"{str(address)} connected")

        client.send("name -> ".encode("utf-8"))
        name = client.recv(1024).decode("utf-8")
        if profanity.contains_profanity(name) == True:
            client.close()
            
        else:
            print(f"name of {str(address)} is {name}")
            broadcast(f"\n{name} joined the chat :)".encode("utf-8"))
            names.append(name)
            clients.append(client)


            thread = threading.Thread(target=handle, args=(client,))
            thread.start()


recive()
while True:
  pass