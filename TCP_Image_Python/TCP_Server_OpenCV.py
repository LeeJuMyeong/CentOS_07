#!/usr/bin/python
import socket
import cv2
import numpy

#socket 수신 버퍼를 읽어서 반환하는 함수
def recvall(sock, count):
	buf = b''
	while count:
		newbuf = sock.recv(count)
		if not newbuf: return None
		buf += newbuf
		count -= len(newbuf)
	return buf

# Receviced ip and port
TCP_IP = '10.0.2.15'
TCP_PORT = 8080

# TCP open and ready
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)
conn, addr = s.accept()

# Image of String Type receviced Client, Image output to Screen
length = recvall(conn, 16)

print(length, type(length))
print('===============')

length = int.from_bytes(length, byteorder='big')
print(length, type(length))
print('===============')

stringData = recvall(conn, int(length))

# fromstring is decrecated. instead frombuffer recommend.
#data = numpy.fromstring(str(stringData), dtype='uint8')

# frombuffer
data = numpy.frombuffer(stringData, dtype='uint8')

s.close()

decimg = cv2.imdecode(data, 1)
cv2.imwrite('Test_Check.jpg', decimg)

#cv2.imshow('SERVER', decimg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



