import socket

"""
    One way communication between server and client, two way requires 
    multithreading (maybe, haven't researched much about the topic)
"""


def main():
    HOST = "127.0.0.1"
    PORT = 4444

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.bind((HOST, PORT))

    while True:
        data, addr = client.recvfrom(1024)
        print(f"Server: {data.decode('utf-8')}")
        if data.decode('utf-8') == "exit":
            break

if __name__ == "__main__":
    main()