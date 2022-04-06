from socket import *

serverPort = 12000
welcomeSocket = socket(AF_INET, SOCK_STREAM)
binding = ('', serverPort)
welcomeSocket.bind(binding)
welcomeSocket.listen(1)

print('server pronto')
while True:
    connectionSocket, clientAddress = welcomeSocket.accept()
    print('connesso con:', clientAddress)

    while True:
        message = connectionSocket.recv(1024)
        message = message.decode('utf-8')
        if message == '.': break
        response = message.upper()
        connectionSocket.send(response.encode('utf-8'))
    connectionSocket.close()