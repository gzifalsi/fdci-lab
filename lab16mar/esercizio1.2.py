# script che stampi il nome della pagina col miglior tempo di risposta medio
# 10 richieste
# urls: http://www.google.com; http://www.youtube.com; ...

import requests as req

siti = ['http://www.google.com',
        'http://www.youtube.com',
        'http://www.polimi.it',
        'http://www.wikipedia.org',
        'http://www.amazon.com',
        'http://www.twitter.com']
avg = 999999
risultato = ''

for url in siti:
    t = []

    for _ in range(10):
        r = req.get(url)
        t.append(r.elapsed.microseconds / 1000)

    temp = sum(t) / len(t)
    if temp < avg:
        avg = temp
        risultato = url

print('il sito più veloce e\'', risultato, ', con un tempo di risposta medio di', avg, ' ms')