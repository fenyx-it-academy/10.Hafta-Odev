"""ODEV: AMIRAL BATTI

Deniz olarak varsayacagimiz 10x10'luk bir tablo olusturun (X-O-X oyununa benzer).
Bu tabloya 2 adet 4 birimlik, 2 adet 3 birimlik, 2 adet 2 birimlik ve 2 adet 1 birimlik gemiler yerlestirin.
 Yerlestirdiginiz gemileri kullanici gormeyecek. Kullanicidan tablo uzerindeki herhangi bir noktaya hamlede
  bulunmasini isteyin. Kullanicinin hamlesi gemilerin herhangi bir noktasina isabet ederse kullaniciya
  tablo uzerinde bunu gosterin. Ayni sekilde bosa atis yaptiginda da kullaniciya tablo uzerinde bunu
  gosterin ve kullanicinin 5 sn boyunca hamle yapmasini engelleyin. Kullanici daha once hamle yapmis
  oldugu bir noktaya tekrar hamlede bulunursa bunu engelleyin. Kullaniciya toplamda 15 yanlis hamle
  hakki verin. Kullanici tum gemileri vurdugunda oyunu bitirin.

Oyunu mumkun oldugunca fonksiyonlar kullanarak yapmanizi istiyoruz.

BONUS(ISTEGE BAGLI): Yukaridaki versiyonda gemiler sabit. Oyunu her actigimizda gemilerin yeri degismiyor.
 Isteyenler gemilerin random yerlestirildigi bir versiyonunu yapabilir."""

# deniz = []

# def denizOlustur():
#     for _ in range(10): #satirlar
#         satir = []
#         for _ in range(10): #sutunlar
#             satir.append('0')
#         deniz.append(satir)
#
# denizOlustur()
# print(deniz)

from functools import reduce
from random import randint
from time import sleep
class oyun():
    deniz = []
    kayitliGemiler = []
    kullaniciHakki = 15
    bilinenGemiler = []


def denizOlustur():
    for _ in range(10):
        deniz.append(['0']*10)


def denizYazdir():
    # cikti = reduce(lambda sonuc, satir: sonuc + ' '.join(satir) + '\n', deniz, '')
    # print(cikti)
    print(reduce(lambda sonuc, satir: sonuc + ' '.join(satir) + '\n', deniz, ''))


def gemiVarMi(gemicik):
    cakisangemiler = list(
        filter(lambda gemi: gemi[0] == gemicik[0] and gemi[1] == gemicik[1], kayitliGemiler))  # 0: satir, 1: sutun
    if len(cakisangemiler) > 0:
        return True
    else:
        return False


def birlikGemiYap():
    while True:
        satir = randint(0, 9)
        sutun = randint(0, 9)
        if gemiVarMi([satir, sutun]):
            continue
        else:
            return [satir, sutun]


def ikilikGemiYap():
    yeni_satir = -1
    yeni_sutun = -1
    while yeni_satir == -1 and yeni_sutun == -1:
        birinci_birim_gemi = birlikGemiYap()
        satir = birinci_birim_gemi[0]
        sutun = birinci_birim_gemi[1]
        if sutun < 9: #saga ekleme
            if not gemiVarMi([satir, sutun + 1]):
                yeni_satir = satir
                yeni_sutun = sutun + 1
                return [birinci_birim_gemi, [yeni_satir, yeni_sutun]]
        if sutun > 0: #sola ekleme
            if not gemiVarMi([satir, sutun - 1]):
                yeni_satir = satir
                yeni_sutun = sutun - 1
                return [[yeni_satir, yeni_sutun], birinci_birim_gemi]
        if satir < 9: #alta ekleme
            if not gemiVarMi([satir + 1, sutun]):
                yeni_satir = satir + 1
                yeni_sutun = sutun
                return [birinci_birim_gemi, [yeni_satir, yeni_sutun]]
        if satir > 0: #uste ekleme
            if not gemiVarMi([satir - 1, sutun]):
                yeni_satir = satir - 1
                yeni_sutun = sutun
                return [[yeni_satir, yeni_sutun], birinci_birim_gemi]


def uclukGemiYap():
    yeni_satir = -1
    yeni_sutun = -1
    while yeni_satir == -1 and yeni_sutun == -1:
        iki_birimlik_gemi = ikilikGemiYap()
        ilk_birim_gemi = iki_birimlik_gemi[0]
        ikinci_birim_gemi = iki_birimlik_gemi[1]
        if ilk_birim_gemi[0] == ikinci_birim_gemi[0]: #yatay gemi
            if ikinci_birim_gemi[1] < 9: #geminin sagindaki birim kontrolu
                if not gemiVarMi([ikinci_birim_gemi[0], ikinci_birim_gemi[1] + 1]):
                    yeni_satir = ikinci_birim_gemi[0]
                    yeni_sutun = ikinci_birim_gemi[1] + 1
                    return [ilk_birim_gemi, ikinci_birim_gemi, [yeni_satir, yeni_sutun]]
            if ilk_birim_gemi[1] > 0:  # geminin solundaki birim kontrolu
                if not gemiVarMi([ilk_birim_gemi[0], ilk_birim_gemi[1] - 1]):
                    yeni_satir = ilk_birim_gemi[0]
                    yeni_sutun = ilk_birim_gemi[1] - 1
                    return [[yeni_satir, yeni_sutun], ilk_birim_gemi, ikinci_birim_gemi]
        else: #dikey gemi
            if ikinci_birim_gemi[0] < 9: #geminin altindaki birim kontrolu
                if not gemiVarMi([ikinci_birim_gemi[0] + 1, ikinci_birim_gemi[1]]):
                    yeni_satir = ikinci_birim_gemi[0] + 1
                    yeni_sutun = ikinci_birim_gemi[1]
                    return [ilk_birim_gemi, ikinci_birim_gemi, [yeni_satir, yeni_sutun]]
            if ilk_birim_gemi[0] > 0:  # geminin ustundeki birim kontrolu
                if not gemiVarMi([ilk_birim_gemi[0] - 1, ilk_birim_gemi[1]]):
                    yeni_satir = ilk_birim_gemi[0] - 1
                    yeni_sutun = ilk_birim_gemi[1]
                    return [[yeni_satir, yeni_sutun], ilk_birim_gemi, ikinci_birim_gemi]


def dortlukGemiYap():
    yeni_satir = -1
    yeni_sutun = -1
    while yeni_satir == -1 and yeni_sutun == -1:
        uc_birimlik_gemi = uclukGemiYap()
        ilk_birim_gemi = uc_birimlik_gemi[0]
        ikinci_birim_gemi = uc_birimlik_gemi[1]
        ucuncu_birim_gemi = uc_birimlik_gemi[2]
        if ilk_birim_gemi[0] == ikinci_birim_gemi[0]: #yatay gemi
            if ucuncu_birim_gemi[1] < 9: #geminin sagindaki birim kontrolu
                if not gemiVarMi([ucuncu_birim_gemi[0], ucuncu_birim_gemi[1] + 1]):
                    yeni_satir = ucuncu_birim_gemi[0]
                    yeni_sutun = ucuncu_birim_gemi[1] + 1
                    return [ilk_birim_gemi, ikinci_birim_gemi, ucuncu_birim_gemi, [yeni_satir, yeni_sutun]]
            if ilk_birim_gemi[1] > 0:  # geminin solundaki birim kontrolu
                if not gemiVarMi([ilk_birim_gemi[0], ilk_birim_gemi[1] - 1]):
                    yeni_satir = ilk_birim_gemi[0]
                    yeni_sutun = ilk_birim_gemi[1] - 1
                    return [[yeni_satir, yeni_sutun], ilk_birim_gemi, ikinci_birim_gemi, ucuncu_birim_gemi]
        else: #dikey gemi
            if ucuncu_birim_gemi[0] < 9: #geminin altindaki birim kontrolu
                if not gemiVarMi([ucuncu_birim_gemi[0] + 1, ucuncu_birim_gemi[1]]):
                    yeni_satir = ucuncu_birim_gemi[0] + 1
                    yeni_sutun = ucuncu_birim_gemi[1]
                    return [ilk_birim_gemi, ikinci_birim_gemi, ucuncu_birim_gemi, [yeni_satir, yeni_sutun]]
            if ilk_birim_gemi[0] > 0:  # geminin ustundeki birim kontrolu
                if not gemiVarMi([ilk_birim_gemi[0] - 1, ilk_birim_gemi[1]]):
                    yeni_satir = ilk_birim_gemi[0] - 1
                    yeni_sutun = ilk_birim_gemi[1]
                    return [[yeni_satir, yeni_sutun], ilk_birim_gemi, ikinci_birim_gemi, ucuncu_birim_gemi]


def gemileriDenizeEkle():
    for i in range(2):
        dortluk_gemi = dortlukGemiYap()
        for gemi in dortluk_gemi:
            kayitliGemiler.append(gemi)
        ucluk_gemi = uclukGemiYap()
        for gemi in ucluk_gemi:
            kayitliGemiler.append(gemi)
        ikilik_gemi = ikilikGemiYap()
        for gemi in ikilik_gemi:
            kayitliGemiler.append(gemi)
        kayitliGemiler.append(birlikGemiYap())


def bilgilendirmeVeKontrol():
    global kullaniciHakki
    print('Kalan deneme sayiniz:', kullaniciHakki)
    print("Gemi koordinatinda satir ve sutun bilgileri:")
    satir = int(input("Satir giriniz: "))
    sutun = int(input("Sutun giriniz: "))
    if not gemiVarMi([satir, sutun]):
        print('Isabet ettiremediniz!!!')
        kullaniciHakki = kullaniciHakki - 1
        deniz[satir][sutun] = ' '
        sleep(2)
    else:
        if [satir, sutun] in bilinenGemiler:
            print("Daha onceden bu gemiyi bildiniz.")
        else:
            print("Bir gemiye denk geldiniz!!!!")
            bilinenGemiler.append([satir, sutun])
        deniz[satir][sutun] = 'X'
    denizYazdir()


def sadeceDeneme(): #gemilerin deniz uzerinde gorunumu
    denizOlustur()
    gemileriDenizeEkle()
    for gemi in kayitliGemiler:
        deniz[gemi[0]][gemi[1]] = 'X'
    denizYazdir()


denizOlustur()
gemileriDenizeEkle()
denizYazdir()
while kullaniciHakki > 0:
    bilgilendirmeVeKontrol()
    if len(bilinenGemiler) == len(kayitliGemiler):
        print("TEBRIKLER: Kazandiniz.")
        break
if kullaniciHakki == 0:
    print("Basarisiz oldunuz... :(")
