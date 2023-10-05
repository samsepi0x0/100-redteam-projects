import socket
import os
import threading

HOST = "127.0.0.1"
PORT = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def recieve():
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            print("\t\t>> ", data)
        except:
            print("error.")
            client.close()
            break

def send():
    while True:
        data = input('>> ')
        client.send(data.encode())

recv_thread = threading.Thread(target=recieve)
recv_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()