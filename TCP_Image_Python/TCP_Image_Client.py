import socket
import cv2
import sys
import time
import datetime
import numpy
import base64

# Windows OpenCV 설치
# >> pip install opencv-python
# https://200309jinmi.tistory.com/entry/Python-377-VScode-%EC%84%A4%EC%B9%98

# Python TCP image socket 구현 (OpenCV)
# https://millo-l.github.io/Python-TCP-image-socket-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-Server-Client/


class ClientSocket:
    def __init__(self, ip, port):
        self.TCP_SERVER_IP = ip
        self.TCP_SERVER_PORT = port
        self.connectCount = 0
        self.connectServer()

    def connectServer(self):
        try:
            self.sock = socket.socket()
            self.sock.connect((self.TCP_SERVER_IP, self.TCP_SERVER_PORT))
            print(u'Clinet socket is connected with Server socket [ TCP_SERVER_IP : ' 
            + self.TCP_SERVER_IP + ', TCP_SERVER_PORT : ' + self.TCP_SERVER_PORT + ']')
            self.connectCount = 0
            self.sendImages()

        except Exception as e:
            print(e)
            self.connectCount += 1
            if self.connectCount == 10:
                print(u'Connect fail %d times. exit program'%(self.connectCount))
                sys.exit()
            print(u'%d times try to connect with server'%(self.connectCount))
            self.connectServer()

    def sendImages(self):
        cnt = 0
        capture = cv2.VideoCapture(0)

        imgWidth = 480
        imgHeight = 315
        imgExt = '.jpg'
        encoding = 'utf-8'

        ###### Image Size ######
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, imgWidth)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, imgHeight)
            
        try:
            while capture.isOpened():
                ret, frame = capture.read()
                resize_frame = cv2.resize(frame, dsize=(imgWidth, imgHeight), interpolation=cv2.INTER_AREA)

                now = time.localtime()
                stime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

                encode_param = [int(cv2.IMWRITE_JPEG_QUALITY, 90)]
                result, imgencode = cv2.imencode(imgExt, resize_frame, encode_param)
                data = numpy.array(imgencode)
                stringData = base64.b64encode(data)
                length = str(len(stringData))
                self.sock.sendall(length.encode(encoding).ljust(64))
                self.sock.send(stringData)
                self.sock.send(stime.encode(encoding).ljust(64))
                print(u'send images %d'%(cnt))
                cnt += 1
                time.sleep(0.095)

        except Exception as e:
            print(e)
            self.sock.close()
            time.sleep(1)
            self.connectServer()
            self.sendImages()

def main():
    TCP_IP = '192.168.201.83'
    TCP_PORT = 8080
    client = ClientSocket(TCP_IP, TCP_PORT)

if __name__ == "__main__":
    main()

