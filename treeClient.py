import socket

HOST, PORT = "localhost", 8080
MESSAGE = "TALK"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # sock.connect((HOST, PORT))
    sock.sendto(MESSAGE.encode(), (HOST, PORT))
    print("Request sent to server")
