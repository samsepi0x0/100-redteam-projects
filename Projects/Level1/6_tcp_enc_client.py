import socket
import threading

caeser = __import__("5_caeser")
HOST = "127.0.0.1"
PORT = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def recieve():
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            print("\t\t>> ", caeser.decrypt(data))
        except:
            print("error.")
            client.close()
            break

def send():
    while True:
        data = input('>> ')
        client.send((caeser.encrypt(data)).encode())

recv_thread = threading.Thread(target=recieve)
recv_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()