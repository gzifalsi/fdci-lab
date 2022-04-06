#server

from socket import *

serverPort = 12000

#apriamo il socket server
serverSocket = socket(AF_INET, SOCK_DGRAM)

#mettiamo il server in ascolto su serverPort
serverSocket.bind(('', serverPort))
print('server pronto')

clients = [(), ()]
#il server si mette in attesa che un client lo contatti
while clients[0] == () or clients[1] == ():
    message, clientAddress = serverSocket.recvfrom(2048)
    print(clientAddress[0])

    if clients[0] == () or clients[0] == clientAddress:
        clients[0] = clientAddress
    else:
        clients[1] = clientAddress

    okString = str(clientAddress[0])
    serverSocket.sendto(okString.encode('utf-8'), clientAddress)
    print('clients connessi:', clients)

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    #decodifica del messaggio
    message_decoded = message.decode('utf-8')

    # print di chi ha contattato il server e di cosa ha mandato
    print(clientAddress, 'dice:', message_decoded)

    okString = 'messaggio ricevuto dal server'

    #inviare il messaggio modificato al client
    if clientAddress == clients[0]:
        serverSocket.sendto(message_decoded.encode('utf-8'), clients[1])
    else:
        serverSocket.sendto(message_decoded.encode('utf-8'), clients[0])