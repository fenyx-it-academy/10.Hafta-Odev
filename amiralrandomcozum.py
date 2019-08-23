from random import*
import secrets
from amiralmodul import tabloilk
tablo=tabloilk().copy()

def sayiyatay(x,y,i):       #sayilari 00 01 02.. veya 23 24 25 26 diye yazmasi icin
    s=f"{x}{y+i}"           #ilk sabit ikinciye ekleyerek gitsin
    return s                #string olarak sayi duruyor


def sayidikey(x,y,i):       #sayilari dikeye yerlestirsin
    s=f"{x+i}{y}"           #23 33 43 53 gibi
    return s

def yatay(uzunluk):         #geminin uzunluguna bagliolarak 4 kutu mu sececek 3 kutumu belirliyor
    kume = []
    x = randint(0, 9)       #geminin ilk kutusu icin yatayda birler basamagina ekleme yapmayacak.0 dan 9 a istedigini alabilir
    y = randint(0,10-uzunluk)                  #0dan 9 a kadar secemez.ekleme yapacak yeri bos birakiyor
    for i in range(uzunluk):            #gemi uzunlugu kadar yatayda ardarda gelen sayiyi kume icine atiyor.
        kume.append(sayiyatay(x, y, i))
    return kume

def dikey(uzunluk):             #gemiyi dikey yerlestirmek icin gemi uzunlugu kadar kutucuk sececek
    kume = []
    x = randint(0, 10-uzunluk)  #onlar basamagi artarak gidecek.kuyruga yer birakiyor
    y = randint(0,9)            #birler basamagi sabit olacak
    for i in range(uzunluk):
        kume.append(sayidikey(x, y, i))
    return kume                 #gemi uzunlugu kadar dikey kutucugu kume de tutuyor

def dorty():                       #dortluk gemiyi yatay yerlestirecekse
    uzunluk=4
    return yatay(uzunluk)

def dortd():                       #dortluk gemiyi dikey yerlestirecekse
    uzunluk=4
    return dikey(uzunluk)

def ucd():                      #ucluk gemiyi dikey yerlestirecekse...
    uzunluk=3
    return dikey(uzunluk)
def ucy():
    uzunluk=3
    return yatay(uzunluk)
def ikid():
    uzunluk=2
    return dikey(uzunluk)
def ikiy():
    uzunluk=2
    return yatay(uzunluk)

def biry():                     #birlik gemide yatay dikey fark etmiyor ama ortak fonksiyonu kullanip tekrar fonk yazmamak icin
    uzunluk=1
    return yatay(uzunluk)

def bird():
    uzunluk=1
    return dikey(uzunluk)


ck=[]
#enson birbirinden farkli sayilardan olusan gemileri burada toplasin
# sonuc strinlerin olusturdugu liste olmali,ana program o sekilde calisiyor



def yerlestir(fonksiyond,fonksiyony):
    while True:
        dikeyyatay = secrets.choice(["yatay", "dikey"])
        #yatay mi dikey mi yerlestircek random karar versin.listelerde random.
        # choice kullanilamiyormus secrets modulu import edilip bu calisiyor


        if dikeyyatay == "dikey":  #eger dikey yerlestirme secilmisse
            a=fonksiyond()          #dortd() ucd() ikid() bird() fonksiyonlarini kullanacak

            if [True for i in a if i in ck]:
                print('if')
                continue
            else:               #aksi halde

                ck.extend(a)     #ck icine koy

                break       #while durdur


        else:                       #eger yatay yerlestirme yapilacaksa(dikeydeki mantigin aynisi)
            a = fonksiyony()

            if [True for i in a if i in ck]:
                print('if')
                continue
            else:

                ck.extend(a)

                break

    return ck

#iki tane 4lu gemi 2 tane 3lu ...icin fonksiyonlari ard arda calistir
yerlestir(dortd,dorty)
yerlestir(dortd,dorty)
yerlestir(ucd,ucy)
yerlestir(ucd,ucy)
yerlestir(ikid,ikiy)
yerlestir(ikid,ikiy)
yerlestir(bird,biry)
yerlestir(bird,biry)
cozum=ck              #tum islemler yapilinca cozum kumesini goster