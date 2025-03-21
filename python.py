# parallel
python ohjelma

import threading
import time

def tulosta_viesti(viesti, kesto):
    for i in range(5):
        time.sleep(kesto)
        print(viesti)

# Luodaan säikeet
thread1 = threading.Thread(target=tulosta_viesti, args=("Säie 1: Hei!", 1))
thread2 = threading.Thread(target=tulosta_viesti, args=("Säie 2: Moi!", 5))

# Käynnistetään säikeet
thread1.start()
thread2.start()

# Odotetaan, että säikeet päättyvät
thread1.join()
thread2.join()

print("Kaikki säikeet ovat valmiita.")
