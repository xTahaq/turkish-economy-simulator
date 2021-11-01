import random
import time
rp = True
try:
    from pypresence import Presence
except ModuleNotFoundError:
    rp = False

startts = time.time()

if rp == True:
    client_id = '853891028401389568' 
    RPC = Presence(client_id,pipe=0) 
    RPC.connect()
    RPC.update(details="Ekonomi simülasyonu yürütüyor.", state="Başlatılıyor - Kurucu: Taha#4216", start=startts)
dollar = 1
days = 0
devamet = False

while True:
    time.sleep(0.1)
    days += 1
    amount = random.randint(-40, 46) / 1000
    dollar += amount
    if dollar < 0:
        dollar = 0
    dollar = round(dollar * 10000) / 10000
    print("Gün: " + str(days) + " / Dolar: " + str(dollar))
    if (dollar > 9 and devamet == False):
        print("Oyun bitti, " + str(days) + " gün hayatta kaldın ve dolar artık 9 lira. Yine de devam etmek için ENTER'a bas.")
        input()
        devamet = True
    if round(days / 50) == days / 50:
        if rp == True:
            RPC.update(details="Ekonomi simülasyonu yürütüyor.", state="Gün: " + str(days) + " - Dolar: " + str(dollar), start=startts)