from socket import *

consonanti = []
for i in range(ord('b'), ord('z')):
    if i not in [ord('e'), ord('i'), ord('o'), ord('u')]:
        consonanti.append(chr(i))

serverPort = 12000
welcomeSocket = socket(AF_INET, SOCK_STREAM)
binding = ('', serverPort)
welcomeSocket.bind(binding)

welcomeSocket.listen(1) # welcomeSocket messo in ascolto

print('server pronto')

while True:
    connectionSocket, clientAddress = welcomeSocket.accept()
    print('connesso con: ', clientAddress)
    message = connectionSocket.recv(1024)
    message = message.decode('utf-8')

    cons = 0
    for i in message:
        if i in consonanti:
            cons += 1

    modifiedMessage = str(cons)
    connectionSocket.send(modifiedMessage.encode('utf-8'))

connectionSocket.close()