#client

from socket import *
#invece di import socket as s o simili

flag = True
serverName = input('inserisci l\'ip del server: ')
while(flag):
    flag = False
    serverPort = input('inserisci la porta del server: ')
    try:
        int(serverPort)
    except ValueError:
        print('porta non valida')
        flag = True

serverPort = int(serverPort)

#identificato il server ora ci connettiamo al socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#AF_INET -> ipv4, SOCK_DGRAM -> udp

#imposto un timeout lato client di 5 secondi
clientSocket.settimeout(5)

while(True):
    #interazione con l'utente
    message = input('Inserisci un messaggio (-1 per uscire): ')
    if message == '-1': break
    #inviare il messaggio al server
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

    #in attesa della risposta
    message_modified, serverAddress = clientSocket.recvfrom(2048)

    #printare il messaggio ricevuto
    print(message_modified.decode('utf-8'))

#se sei big brain ci arrivi da solo
clientSocket.close()