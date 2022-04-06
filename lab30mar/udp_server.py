#server

from socket import *
from time import sleep

consonanti = []
for i in range(ord('a'), ord('z')):
    if i not in [ord('a'), ord('e'), ord('i'), ord('o'), ord('u')]:
        consonanti.append(chr(i))

serverPort = 8080

#apriamo il socket server
serverSocket = socket(AF_INET, SOCK_DGRAM)

#mettiamo il server in ascolto su serverPort
serverSocket.bind(('', serverPort))
print('server pronto')

#il server si mette in attesa che un client lo contatti
while(True):
    message, clientAddress = serverSocket.recvfrom(2048)

    #decodifica del messaggio
    message_decoded = message.decode('utf-8')

    # print di chi ha contattato il server e di cosa ha mandato
    print('contattato tramite udp da:', clientAddress)
    print('dice:', message_decoded)

    #modifica del messaggio decodificato
    message_decoded = message_decoded.lower()
    if message_decoded == 'sleep': sleep(10)
    result = 0
    for letter in message_decoded:
        if letter in consonanti:
            result += 1
    result = str(result)

    #inviare il messaggio modificato al client
    serverSocket.sendto(result.encode('utf-8'), clientAddress)