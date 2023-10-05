import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = "127.0.0.1"
    PORT = 4444

    try:
        client.connect((HOST, PORT))
        print("Connected to Server.\n")
        while True:
            client_cmd = input(">> ")
            client.send(client_cmd.encode())

            data = client.recv(1024)
            print(f"Server: {data.decode('utf-8')}")
            if client_cmd == "exit":
                break


    except:
        print("Unable to connect to the server.")
    

    print("Connection Closed.")

if __name__ == '__main__':
    main()