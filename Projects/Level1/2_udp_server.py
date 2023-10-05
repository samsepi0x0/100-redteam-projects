import socket

def main():
    HOST = "127.0.0.1"
    PORT = 4444
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP Connection
    
    while True:
        server_cmd = input(">> ")
        server.sendto(server_cmd.encode(), (HOST, PORT))
        if server_cmd == "exit":
            break
       
if __name__ == '__main__':
    main()