from socket import *
from threading import Thread

def handler(connectionSocket):
    while True:
        message = connectionSocket.recv(2048)
        message = message.decode('utf-8')
        if message == '.': break
        response = message.upper()
    connectionSocket.close()

serverPort = 12000
welcomeSocket = socket(AF_INET, SOCK_STREAM)
binding = ('', serverPort)
welcomeSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# SO_REUSEADDR è un flag, lo usiamo per dire al server di accettare più connessioni in serie sulla socket
welcomeSocket.bind(binding)
welcomeSocket.listen(1)

while True:
    print('server pronto')
    connectionSocket, clientAddress = welcomeSocket.accept()
    thread = Thread(target=handler, args=(connectionSocket,))
    thread.start()