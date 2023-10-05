import socket

"""
    One way communication between server and client, two way requires 
    multithreading (maybe, haven't researched much about the topic)
"""

rot13 = __import__("7_rot13")

def main():
    HOST = "127.0.0.1"
    PORT = 4444

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.bind((HOST, PORT))

    while True:
        data, addr = client.recvfrom(1024)
        print(f"Server: {rot13.decrypt(data.decode('utf-8'))}")
        if data.decode('utf-8') == "exit":
            break

if __name__ == "__main__":
    main()