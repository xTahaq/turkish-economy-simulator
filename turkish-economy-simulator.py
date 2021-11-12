import random
import time
rp = True
try:
    from pypresence import Presence
except ModuleNotFoundError:
    rp = False

startts = time.time()

languages = {
    "en": {
        "spMpTxt": "Please enter waiting time per refresh (max 10, min 0.001, default 0.1, you can type 'none' to disable waiting time) (less = faster refresh and simulation) (press ENTER to skip, it will automaticly set it to default)",
        "endGameTxt": " days survived and dollar is now 9 Turkish Liras. Press ENTER to still continue.",
        "mainDay": "Day: ",
        "mainDollar": " - Dollar: ",
        "rpcDtls": "Running Turkish economy simulation."
    },
    "tr": {
        "spMpTxt": "Lütfen yenileme başı bekleme süresi giriniz (en fazla 10, en az 0.001, normal 0.1, 'none' yazarak beklemeyi kapatabilirsiniz) (az = daha hızlı yenileme ve simülasyon) (ENTER basarak geç, otomatik normal değeri ayarlıyacaktır)",
        "endGameTxt": " gün hayatta kaldın ve dolar artık 9 lira. Yine de devam etmek için ENTER'a bas.",
        "mainDay": "Gün: ",
        "mainDollar": " - Dolar: ",
        "rpcDtls": "Türk ekonomi simülasyonu yürütüyor."
    }
}
if rp == True:
    client_id = '853891028401389568' 
    RPC = Presence(client_id,pipe=0) 
    RPC.connect()
    RPC.update(details="Ekonomi simülasyonu yürütüyor.", state="Başlatılıyor - Kurucu: Taha#4216", start=startts)
dollar = 1
days = 0
devamet = False
enableCooldown = True
lang = "tr"

print("-------------------------------------------------")
print("")
print("Welcome to Turkish Economy Simulator")
print("")
print("-------------------------------------------------")
print("Please enter your preferences to start the app.")
lang = input("Type a language (options: tr, en) (press ENTER to skip - it will automaticly set it to Turkish)\n> ")
if lang != "tr" and lang != "en":
    lang = "tr"
speedMultiplier = input(languages[lang]["spMpTxt"] + "\n> ")
try:
    speedMultiplier = float(speedMultiplier)
except Exception:
    if speedMultiplier == "none":
        enableCooldown = False
        speedMultiplier = 0.1
    else:
        speedMultiplier = 0.1

speedMultiplier = float(speedMultiplier)
if speedMultiplier > 10:
    speedMultiplier = 10
if speedMultiplier < 0.001:
    speedMultiplier = 0.001

print("Lang: " + lang + " - Speed: " + str(speedMultiplier))
while True:
    days += 1
    amount = random.randint(-40, 46) / 1000
    dollar += amount
    if dollar < 0:
        dollar = 0
    dollar = round(dollar * 10000) / 10000
    print(languages[lang]["mainDay"] + str(days) + languages[lang]["mainDollar"] + str(dollar))
    if (dollar > 9 and devamet == False):
        if lang == "tr":
            print(str(days) + languages[lang]["endGameTxt"])
        input()
        devamet = True
    if round(days / 50) == days / 50:
        if rp == True:
            RPC.update(details=languages[lang]["rpcDtls"], state=languages[lang]["mainDay"] + str(days) + languages[lang]["mainDollar"] + str(dollar), start=startts)
    if enableCooldown == True:
        time.sleep(speedMultiplier)