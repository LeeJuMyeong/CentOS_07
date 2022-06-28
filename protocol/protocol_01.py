import socket
import struct

IP = "10.0.2.15"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(0)

receive_data, addr = s.accept()

#print("IP : " + addr[0] + " PORT : " + addr[1])

#data = s.recv(65535)	# 65535 = 2^16 - 1

print(type(addr), addr)		# tuple
print(type(receive_data))	# socket.socket


#print(addr + " " + receive_data)

#receive_data = struct.unpack('5B', receive_data)

print("[Received Data]: ", receive_data)

data = receive_data.recv(65535)

data = struct.unpack('BBBBBB', data)

D0 = hex(data[0])
D1 = hex(data[1])
D2 = hex(data[2])
D3 = hex(data[3])
D4 = hex(data[4])
D5 = hex(data[5])

print(D0, D1, D2, D3, D4, D5)


s.close()
