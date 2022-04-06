from socket import *

# trasforma la mappa in una stringa da visualizzare
def mapString(map):
    string = ""
    for i in range(3):
        for j in range(3):
            string = string + "\t"
            string = string + "[" + map[3*i+j] + "]"
        string = string + "\n"
    return string


# controlla se la partita è finita  (VITTORIA se righe, colonne o diagonali uguali. Pari se la mappa è tutta piena)
def checkMap(map):
    # ritorna 1 se abbiamo una VITTORIA, -1 se la partita è finita PARI, 0 se la partita è IN CORSO
    # controlla la riga 1
    if((map[0] == map[1] == map[2]) and map[0] != ""):
        return 1

    # controlla la riga 2
    elif((map[3] == map[4] == map[5]) and map[3] != ""):
        return 1

    # controlla la riga 3
    elif ((map[6] == map[7] == map[8]) and map[6] != ""):
        return 1

    # controlla la diagonale 1
    elif ((map[0] == map[4] == map[8]) and map[0] != ""):
        return 1

    # controlla la diagonale 2
    elif ((map[2] == map[4] == map[6]) and map[2] != ""):
        return 1

    # controlla la colonna 1
    elif ((map[0] == map[3] == map[6]) and map[0] != ""):
        return 1

    # controlla la colonna 2
    elif ((map[1] == map[4] == map[7]) and map[1] != ""):
        return 1

    # controlla la colonna 3
    elif ((map[2] == map[5] == map[8]) and map[2] != ""):
        return 1

    # Se nessuno ha vinto, controlla se non ci sono piu caselle disponibili (PAREGGIO)
    elif map.count("") == 0:
        return -1

    # Altrimenti la partita non è finita e ritorno 0
    return 0


# assegna il segno nella casella della mappa corrispondente all'indice scelto dal client.
# Ritorna la nuova mappa e un boolean (True se la scelta è ok, False se la scelta non va bene)
def play(map,scelta,segno):
    if scelta < 0 or scelta > 8:
        # ritorna false, la mossa non va bene!
        return map, False
    # se la casella è libera, la mossa è ok
    if map[scelta] == "":
        map[scelta] = segno
        return map, True
    #altrimenti ritorna false, la mossa non va bene!
    return map, False


#funzione principale
def main():
    serverPort = 12000 # porta della socket server
    segni = ["X", "0"] # segni dei giocatori (il primo avrà una X, il secondo client connesso avrà uno O)
    map = ["", "", "","","","","","",""]  # mappa del gioco, inizialmente vuota!
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("", serverPort))
    clients = [] #lista dei client "connessi", inizialmente vuota

    #faccio "connettere" i client al gioco
    #HINT: Che MESSAGGIO si aspetta il server dai client come prima operazione ???
    while len(clients) < 2:
        message, clientAddr = serverSocket.recvfrom(2048)
        message = message.decode("utf-8")
        if message == "CONNECT":
            clients.append(clientAddr)


    i = 0  # indice del giocatore corrente
    finish = 0 # stato della partita (0 se è in CORSO, 1 se c'è un VINCITORE, -1 se PAREGGIO)

    while finish == 0: # faccio giocare alternatamente player 0, 1, 0, ... , fino a che la partita non finisce

        # manda la mappa e avvisa l'ALTRO client di ASPETTARE (controlla l'indice)
        serverSocket.sendto((mapString(map) + "\nPer favore ASPETTA il tuo turno").encode("utf-8"), clients[(i + 1) % 2]) # il (% n ) è l'operatore MODULO n

        # manda la mappa e avvisa il client CORRENTE di GIOCARE (controlla l'indice)
        serverSocket.sendto((mapString(map) + "\nTocca a te, GIOCA ("+segni[i]+")").encode("utf-8"), clients[i])

        # aspetta la risposta del client che deve giocare!
        message, clientAddr = serverSocket.recvfrom(2048)
        if(clientAddr != clients[i]):
            # errore, ha giocato il client sbagliato, non tenere conto della mossa
            # NOTA BENE: con il continue salto il cambio di client, così tocca nuovamente allo stesso client
            continue

        # processa la scelta del messaggio client (HINT: cosa deve mandare il client al server???)
        message = message.decode("utf-8")

        #assegna la scelta della giocata, se valida
        map, res = play(map, int(message), segni[i])
        # se la mossa non è valida, avvisa il client dell'errore!
        if not res:
            print("Mossa non valida")
            serverSocket.sendto(("ERRORE, mossa non valida").encode("utf-8"), clients[i])
            continue # NOTA BENE: con il continue salto il cambio di client, così tocca nuovamente allo stesso client


        # aggiorna lo stato della partita
        finish = checkMap(map)
        if finish != 0: # interrompi la partita se è finita (così non si cambia giocatore)
            break

        # Cambia giocatore per il turno successivo
        if i == 0:
            i = 1
        else:
            i = 0

    # Informa i due client che la partita è finita, i client devono terminare dopo un messaggio che contiene "FINE"
        # HINT: usa      'if "FINE" in message'      per sapere se terminare il client
    if finish == 1:
        message = mapString(map) + "\nFINE: HA VINTO "+segni[i]
    if finish == -1:
        message = mapString(map) + "\nFINE: PAREGGIO"
    serverSocket.sendto(message.encode("utf-8"), clients[0]) # avvisa client 0 della fine della partita
    serverSocket.sendto(message.encode("utf-8"), clients[1]) # avvisa client 1 della fine della partita

    #chiudo la socket server
    serverSocket.close()

    #N.B. A fine partita il SERVER verrà chiuso automaticamente.
    # Se i client terminano prima della fine della partita, il server deve essere riavviato.


#eseguo il codice della funzione principale
main()