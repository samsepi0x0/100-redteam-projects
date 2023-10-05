import socket

def main():
    HOST = "127.0.0.1"
    PORT = 4444

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(3)

        conn, addr = s.accept()

        with conn:
            print(f"Connected: {addr}")
            while True:
                data = conn.recv(1024)
                if data == b'': # connection is closed
                    break
                print(data)

if __name__ == "__main__":
    main()