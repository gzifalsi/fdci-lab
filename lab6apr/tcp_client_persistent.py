# processo client persistente

from socket import *
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket_address = (serverName, serverPort)
clientSocket.connect(welcomeSocket_address)

while True:
    message = input('invia (. per chiudere): ')
    if message == '.': break
    clientSocket.send(message.encode('utf-8'))
    response = clientSocket.recv(2048)
    print('il server dice:', response.decode('utf-8'))

clientSocket.close()