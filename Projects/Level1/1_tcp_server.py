import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp connection
    HOST = "127.0.0.1"
    PORT = 4444

    server.bind((HOST, PORT))
    server.listen(5)
    print("Listening for connections...")
    conn, addr = server.accept()

    if conn:
        print(f"Connected: {addr}")
        data = conn.recv(1024)

        while not data == b"exit":
            print(f"Client: {data.decode('utf-8')}")
            server_cmd = input(">> ")
            conn.send(server_cmd.encode())
            data = conn.recv(1024)
            if data == b'':
                break

if __name__ == '__main__':
    main()