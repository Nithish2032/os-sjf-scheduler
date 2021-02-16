import socket

server_socket = socket.socket()

server_socket.bind((socket.gethostname(),8000))

server_socket.listen(2)

while True:
    client_socket,address = server_socket.accept()

    print("Connected to "+ str(address))

    client_socket.send(bytes("Hello this is server","utf-8"))








