import socket

HOST = "127.0.0.1"
PORT = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def recv():
    client.connect((HOST, PORT))
    file = []
    filename = ""
    while True:
        data = client.recv(1024)
        if not data:
            break
        if data.decode() == "~~~END~~~":
            filename = client.recv(1024).decode()
            print(filename)
            break
        file.append(data)
        print(data)

    f = open(filename, "wb")
    f.writelines(file)
    f.close()

if __name__ == "__main__":
    recv()