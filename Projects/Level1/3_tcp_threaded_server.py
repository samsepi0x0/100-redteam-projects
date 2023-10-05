import socket
import os
import threading

HOST = "127.0.0.1"
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

clients = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            data = client.recv(1024)
            broadcast(data)
        except:
            clients.remove(client)
            client.close()
            break

def recieve():
    while True:
        client, addr = server.accept()
        print(f"Connected: {addr}")
        clients.append(client)

        broadcast("New Client Joined.".encode())
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

recieve()