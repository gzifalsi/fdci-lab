#analisi tempi di risposta di un server HTTP

#server: www.google.it

def avg(array):
    return sum(array) / len(array)

import requests as req
import matplotlib.pyplot as plt
# necessaria per contattare i server HTTP tramite richieste GET
# CTRL+Q sul nome della libreria per leggerne la documentazione (poderoso)

r = req.get('http://www.google.it')

'''
print('siamo tornati su python borga droia')

print('r è una variabile di tipo')
print(type(r))
print('qual\'era l\'url?')
print(r.url)
print('la richiesta è andata a buon fine?')
if(r.status_code ==  200):
    print('sì')
else:
    print('nope, codice: ', r.status_code)
# ricorda
# 200 OK (2xx successo)
# 304 not modified
# 404 not found (4xx errori client)
# 5xx errore server
print('cosa ci ha mandato il sito?')
print(r.content)
'''

print('misuriamo il tempo di risposta del server contattato')
print(r.elapsed.microseconds / 1000, ' ms')

statistiche = []

for i in range(10):
    r2 = req.get('http://www.google.it')
    t = r2.elapsed.microseconds / 1000
    print('Id. Misura: ', i+1, '; ', t, ' ms')
    statistiche.append(t)

min_s = min(statistiche)
avg_s = avg(statistiche)
max_s = max(statistiche)


print('min: ', min_s, ' ms')
print('avg: ', avg_s, ' ms')
print('max :', max_s, ' ms')

plt.figure() # apre una finestra grafica vuota

plt.plot(statistiche, 'bs') # x: 1, 2, 3, 4...; y: statistiche[1]...
# nota bene, b è il colore (blu) e 'o' è per i puntini
# se avessi usato '*' avrebbe messo le stelline
plt.ylim([min_s * 0.9, max_s * 1.1]) # centriamo l'asse y sul range di valori che abbiamo raccolto
plt.axhline(avg_s, 0, i, color='y') # linea orizzontale y=avg_s

plt.title('analisi delle prestazioni dei server poracci di google') # titolo del grafico
plt.xlabel('Id. Misura', color='b') # nome e colore dell'asse x
plt.ylabel('ms', color='b') # nome e colore dell'asse y

plt.grid(True) # aggiungiamo la griglia

plt.show() # mostriamo a video il grafico che abbiamo popolato
