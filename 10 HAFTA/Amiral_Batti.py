# 10.Hafta-Odev

"""ODEV: AMIRAL BATTI

(1)Deniz olarak varsayacagimiz 10x10'luk bir tablo olusturun (X-O-X oyununa benzer).
(2)Bu tabloya 2 adet 4 birimlik, 2 adet 3 birimlik, 2 adet 2 birimlik ve 2 adet 1 birimlik gemiler yerlestirin.
(3)Yerlestirdiginiz gemileri kullanici gormeyecek. Kullanicidan tablo uzerindeki herhangi bir noktaya hamlede bulunmasini isteyin.
(4)Kullanicinin hamlesi gemilerin herhangi bir noktasina isabet ederse kullaniciya tablo uzerinde bunu gosterin. Ayni sekilde bosa atis yaptiginda da kullaniciya tablo uzerinde bunu gosterin
(5)ve kullanicinin 5 sn boyunca hamle yapmasini engelleyin. Kullanici daha once hamle yapmis oldugu bir noktaya tekrar hamlede bulunursa bunu engelleyin.
(6)Kullaniciya toplamda 15 yanlis hamle hakki verin.  Kullanici tum gemileri vurdugunda oyunu bitirin.

<>Oyunu mumkun oldugunca fonksiyonlar kullanarak yapmanizi istiyoruz.

<>BONUS(ISTEGE BAGLI): Yukaridaki versiyonda gemiler sabit. Oyunu her actigimizda gemilerin yeri degismiyor. Isteyenler gemilerin random yerlestirildigi bir versiyonunu yapabilir."""



from random import randint
from time import sleep
atis_hakki = 0
deniz = []

for i in range(0,10):
    deniz.append(["-"]*10)
def denizalani(deniz):
    for satir in deniz:
        print("".join(satir))
def denizsatir(deniz):
    return randint(0,len(deniz)-1)
def denizsutun (deniz):
    return randint(0,len(deniz)-1)

print(denizalani(deniz))

gemi1_satir = denizsatir(deniz)
gemi1_sutun = denizsutun(deniz)
gemi2_satir = denizsatir(deniz)
gemi2_sutun = denizsutun(deniz)
gemi3_satir = denizsatir(deniz)
gemi3_sutun = denizsutun(deniz)
gemi4_satir = denizsatir(deniz)
gemi4_sutun = denizsutun(deniz)
gemi5_satir = denizsatir(deniz)
gemi5_sutun = denizsutun(deniz)
gemi6_satir = denizsatir(deniz)
gemi6_sutun = denizsutun(deniz)
gemi7_satir = denizsatir(deniz)
gemi7_sutun = denizsutun(deniz)


while atis_hakki <= 15:
    atissatir = int(input("satir atisinizi yapin: "))
    atissutun = int(input("sutun atisinizi yapin: "))
    atis_hakki+=1
    if (atissatir == gemi1_satir and atissutun == gemi1_sutun) or (atissatir == gemi2_satir and atissutun == gemi2_sutun)\
        or (atissatir == gemi3_satir and atissutun == gemi3_sutun) or (atissatir == gemi4_satir and atissutun == gemi4_sutun)\
        or (atissatir == gemi5_satir and atissutun == gemi5_sutun) or (atissatir == gemi6_satir and atissutun == gemi6_sutun)\
        or (atissatir == gemi7_satir and atissutun == gemi7_sutun):
        print("tebrikler!!!gemiyi batirdiniz")
        print(denizalani(deniz))
        break
    elif (atissatir == gemi1_satir and atissutun == gemi1_sutun):
        print("birinci gemiyi batirdin")

    elif (atissatir == gemi2_satir and atissutun == gemi2_sutun):
        print("ikinci gemiyi batirdin")

    elif (atissatir == gemi3_satir and atissatir == gemi3_sutun):
        print("ucuncu gemiyide batirdin")

    elif (atissatir == gemi4_satir and atissatir == gemi4_sutun):
        print("dorduncu gemiyide batirdin")

    elif (atissatir == gemi5_satir and atissatir == gemi5_sutun):
        print("besinci gemiyide batirdin")

    elif (atissatir == gemi6_satir and atissatir == gemi6_sutun):
        print("altinci gemiyide batirdin")

    elif (atissatir == gemi7_satir and atissatir == gemi7_sutun):
        print("yedinci gemiyide batirdin")
    else:

        if (atissatir < 0 or atissutun < 0) or (atissatir > 10 or atissutun > 10):
            print("KARAVANA,atis alaninin disina isbaet ettiniz")

        elif deniz[atissatir - 1][atissutun - 1] == "X":
            print("ayni yere atis yaptiniz")
            sleep(5)
        else:

         print("ISKALADINIZ")
         deniz[atissatir - 1][atissutun - 1] = "X"
         print(denizalani(deniz))


    if  atis_hakki > 15:
        print("atis hakkiniz bitti,maalesef oyunuz kaybettiniz")
        break