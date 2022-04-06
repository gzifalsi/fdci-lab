# script che stampi il nome della pagina col miglior tempo di risposta medio
# 5 richieste
# urls: http://www.google.com; http://www.youtube.com

import requests as req

siti = ['http://www.google.com',
        'http://www.youtube.com']
avg = 999999
risultato = ''

for url in siti:
    t = []

    for _ in range(5): # puoi usare _ al posto di una lettera se non devi usarla
        r = req.get(url)
        t.append(r.elapsed.microseconds / 1000)

    temp = sum(t) / len(t)
    if temp < avg: # aggiorna avg solo se la media appena misurata e' inferiore
        avg = temp
        risultato = url

print('il sito più veloce e\'', risultato, ', con un tempo di risposta medio di', avg, ' ms')