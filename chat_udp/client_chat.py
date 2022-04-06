from socket import *
from threading import *

serverName = '192.168.1.156'
serverPort = 12000


def invia():
    while True:
        message = input()
        clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

'''
def ricevi():
    message_received, serverAddress = clientSocket.recvfrom(2048)
    print(message_received.decode('utf-8'))
'''

ti = Thread(target=invia)
#tr = Thread(target=ricevi)

#identificato il server ora ci connettiamo al socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#AF_INET -> ipv4, SOCK_DGRAM -> udp

ti.start()
#tr.start()

while True:
    message_received, serverAddress = clientSocket.recvfrom(2048)
    print('dice:', message_received.decode('utf-8'))

#se sei big brain ci arrivi da solo
clientSocket.close()