import socket

rot13 = __import__("7_rot13")


def main():
    HOST = "127.0.0.1"
    PORT = 4444
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP Connection
    
    while True:
        server_cmd = input(">> ")
        server.sendto(rot13.encrypt(server_cmd).encode(), (HOST, PORT))
        if server_cmd == "exit":
            break
       
if __name__ == '__main__':
    main()