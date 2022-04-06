from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket_address = (serverName, serverPort)

clientSocket.connect(welcomeSocket_address)

message = input('invia: ')
clientSocket.send(message.encode('utf-8'))

modifiedMessage = clientSocket.recv(1024)
print('il server dice:', modifiedMessage.decode('utf-8'))

clientSocket.close()