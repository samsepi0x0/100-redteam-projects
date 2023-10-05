import socket
import time

HOST = "127.0.0.1"
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(4)

def main():
    conn, addr = server.accept()
    print(f"Connected: {addr}")
    print("Sending file...")
    file = input("File Path >> ")
    contents = open(file, 'rb')
    lines = contents.readlines()

    for line in lines:
        conn.send(line)

    time.sleep(3)
    conn.send("~~~END~~~".encode())
    print("File sent, waiting confirmation")
    
    time.sleep(3)
    conn.send(file.encode())
    print("File transfer complete.")

if __name__ == "__main__":
    main()