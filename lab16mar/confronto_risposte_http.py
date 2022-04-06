import requests as req
import matplotlib.pyplot as plt

siti = ['http://www.gazzetta.it',
        'http://www.facebook.it',
        'http://www.netflix.com']

plt.figure() # apro una finestra grafica fuori dai cicli for
m = 0 # inizializziamo il massimo dei massimi a 0

for url in siti:
    print(20 * '*')
    print('contattando ', url)

    stats = []

    for i in range(10): # ciclo interno per le misure
        r = req.get(url)
        stats.append(r.elapsed.microseconds / 1000)

    min_s = min(stats)
    avg_s = sum(stats) / len(stats)
    max_s = max(stats)

    plt.plot(stats, label=url)

    print('min: ', min_s, ' ms')
    print('avg: ', avg_s, ' ms')
    print('max: ', max_s, ' ms')

    m = max([m, max_s]) # modifichiamo dinamicamente il ping massimo ad ogni iterazione

plt.ylim([0, m * 1.1])
plt.xlabel('Id. Misura', color='b')
plt.ylabel('ms', color='b')
plt.title('confronto tempi di risposta server HTTP')

plt.legend(loc='lower right', fontsize=8)
plt.grid(True)

plt.show()