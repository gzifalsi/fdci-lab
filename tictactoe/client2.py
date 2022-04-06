from socket import *
from threading import *

serverName = '192.168.1.156'
serverPort = 12000

def invia():
    while True:
        message = input()
        clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

ti = Thread(target=invia)

clientSocket = socket(AF_INET, SOCK_DGRAM)

ti.start()


while True:
    message_received, serverAddress = clientSocket.recvfrom(2048)
    print('dice:', message_received.decode('utf-8'))


clientSocket.close()