from socket import *

serverName = 'localhost'
serverPort = 8080

clientSocket = socket(AF_INET, SOCK_DGRAM)

#impostiamo un timeout sul socket
clientSocket.settimeout(4)

message = input('inserisci lettere: ')
clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

try:
    message_modified, serverAddress = clientSocket.recvfrom(2048)
    print(message_modified.decode('utf-8'))

#nel caso in cui il messaggio non arriva
except TimeoutError:
    print('timeout scaduto. errore sconosciuto')
finally:
    clientSocket.close()