# Deniz olarak varsayacagimiz 10x10luk bir tablo olusturun
# Bu tabloya 2 adet 4 birimlik, 2 adet 3 birimlik, 2 adet 2 birimlik ve 2 adet 1 birimlik gemiler yerlestirin.
# Yerlestirdiginiz gemileri kullanici gormeyecek.
# Kullanicidan tablo uzerindeki herhangi bir noktaya hamlede bulunmasini isteyin.
# Kullanicinin hamlesi gemilerin herhangi bir noktasina isabet ederse kullaniciya tablo uzerinde bunu gosterin.
# Ayni sekilde bosa atis yaptiginda da kullaniciya tablo uzerinde bunu gosterin
# kullanicinin 5 sn boyunca hamle yapmasini engelleyin.
# Kullanici daha once hamle yapmis oldugu bir noktaya tekrar hamlede bulunursa bunu engelleyin.
# Kullaniciya toplamda 15 yanlis hamle hakki verin.
# Kullanici tum gemileri vurdugunda oyunu bitirin.

print('''
                                *********************************
                            
                                       Amiral Batti Oyunu
                     
                                *********************************     
''')

tablo = [["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
         ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
         ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
         ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ "],
         ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
         ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
         ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
         ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
         ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
         ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
         ]

rakamlar = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

doluOlanlar = []
dogruHamleler = []
# kullanicinin dogru hamlelerini bu listeye atayacagiz

strJa = '////'
# gemiye isabet ettiginde hamle yapilan alanda gosterilecek sekil
strNee = 'XXXX'
# gemiye isabet etmediginde hamle yapilan alanda gosterilecek sekil

# doluOlanlar = []
yanlisHamleler = []
import random

try:
    def randomIndex(a):
        a = random.randrange(0, a)
        return a


    def dortBirimlikGemi():
        i = 0
        a = randomIndex(10)  # ilk deger 9a kadar rakam alabilecegi icin range siniri 10
        b = randomIndex(7)  # ikinci index 6ya kadar deger alabilecegi icin range siniri 7
        # gemi yatay olarak yerlesecegi icin ikinci indexi max 6dan baslayabilir
        if [a, b] and [a, b + 1] and [a, b + 2] and [a, b + 3] not in doluOlanlar:
            while i < 4:
                doluOlanlar.append([a, b + i])
                i += 1
        else:
            dortBirimlikGemi()


    def ucBirimlikGemi():
        i = 0
        a = randomIndex(10)
        b = randomIndex(8)
        if [a, b] and [a, b + 1] and [a, b + 2] not in doluOlanlar:
            # random olarak yerlestirilen uc birimlik gemi
            # tabloda mevcut mu degil mi
            while i < 3:
                doluOlanlar.append([a, b + i])
                i += 1
        else:
            ucBirimlikGemi()

    def ikiBirimlikGemi():
        i = 0
        a = randomIndex(10)
        b = randomIndex(9)
        if [a, b] and [a, b + 1] not in doluOlanlar:
            # random olarak yerlestirilen iki birimlik gemi
            # tabloda mevcut mu degil mi
            while i < 2:
                doluOlanlar.append([a, b + i])
                i += 1
        else:
            ikiBirimlikGemi()


    def birBirimlikGemi():
        i = 0
        a = randomIndex(10)
        b = randomIndex(10)
        if [a, b] not in doluOlanlar:
            # random olarak yerlestirilen bir birimlik gemi
            # tabloda mevcut mu degil mi
            while i < 1:
                doluOlanlar.append([a, b + i])
                i += 1
        else:
            birBirimlikGemi()


    a = 0
    while a < 3:
        # her gemiden 3er adet olusturuyoruz
        dortBirimlikGemi()
        ucBirimlikGemi()
        ikiBirimlikGemi()
        birBirimlikGemi()
        a += 1

    a = 0
    while a < 15:
        dogruHamleler.sort()
        doluOlanlar.sort()
        # listelerin esit olup olmadigini kontrol edebilmek icin iki listeyi de kucukten buyuge siraadik
        if doluOlanlar == dogruHamleler:
            # listeler esit ise kullanici tum gemileri vurmus kabul edilir.Oyunu kazanir.
            print('Tebrikler Oyunu Kazandiniz!!!')
            break
        else:
            hamleA = input('Satir icin bir rakam girin: ')
            hamleB = input('Sutun icin bir rakam girin: ')

            # kullanicidan aldigimiz degerleri ilk ve ikinci index
            # olarak kullanacagimiz degiskenlere atiyoruz

            if hamleA in rakamlar and hamleB in rakamlar:
                # girilen degerlerin rakam olup olmadigini kontrol ediyoruz
                hamleA = int(hamleA)
                hamleB = int(hamleB)
                # stringi inte cevirdik
                hamleIndex = [hamleA, hamleB]

                if hamleIndex in doluOlanlar:
                    # kullanicinin hamlesi listede var ise yani isabet ettirdi ise;
                    if tablo[hamleA][hamleB] == '___ ':
                        # isabet ettirdigi alanin bos olup olmadigini
                        # daha onceden atis yapip yapmadigini kontrol ediyoruz.

                        print('Tebrikler gemiye isabet ettirdiniz.')
                        tablo[hamleA][hamleB] = strJa
                        # geminin isabet ettirilen alanini tabloda gosteriyoruz
                        dogruHamleler.append(hamleIndex)
                    else:
                        print('Bu alana daha onceden atis yaptiniz! Tekrar deneyin!')
                        continue
                else:
                    if tablo[hamleA][hamleB] != 'XXXX':
                        a += 1
                        # her bosa atista 1 hakki gidiyor.
                        print(
                            'Isabet ettiremediniz.Tekrar deneyin! 5 sn bekleme cezasi aldiniz. Kalan Hakkiniz {}'.format(
                                15 - a))
                        tablo[hamleA][hamleB] = strNee
                        yanlisHamleler.append([hamleA, hamleB])
                        # kullaniciya, bosa atis yaptigi alani tabloda gosteriyoruz.
                        import time
                        time.sleep(5)
                        # kullanici yanlis tahmin yaptiginda 5 sn bekletiyoruz.
                    else:
                        print('Bu alana daha onceden atis yaptiniz! Tekrar deneyin!')
                        continue

                for i in tablo:
                    print("\t".expandtabs(30), *i, end="\n" * 2)
                    # tabloyu ekrana bastiriyoruz
            else:
                print('Lutfen 0 ile 9 arasinda bir rakam girin!')
                continue

    print('Maalesef kaybettiniz! Iskaladiginiz noktalar ve gemilerin konumlari soyledir;\n')

    for i in doluOlanlar:
        # kullanici kaybettigi icin, tabloda gemilerin yerlerini gosteriyoruz
        tablo[i[0]][i[1]] = strJa
        print(i)
    for i in yanlisHamleler:
        # kullanicinin iskaladigi noktalari gosteriyoruz
        tablo[i[0]][i[1]] = strNee
    for i in tablo:
        print("\t".expandtabs(30), *i, end="\n" * 2)
except:
    print('Hata! Programdan cikiliyor...')
