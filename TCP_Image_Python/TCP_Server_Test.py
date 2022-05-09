import socket

IP = '10.0.2.15'
PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#print(IP, type(IP), " - ", PROT, type(PROT))

server_socket.bind((IP,PORT))
server_socket.listen(0)

client_socket, addr = server_socket.accept()

data = client_socket.recv(65535)

print("Received Data: ", data.decode())

