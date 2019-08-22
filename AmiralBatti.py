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

# GemiTablo = [["___ ", "////", "////","////", "////", "___ ","___ ", "___ ", "___ ","___"],
#          ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
#          ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
#          ["___ ", "___ ", "___ ","////", "////", "___ ","////", "////", "////","////"],
#          ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
#          ["___ ", "////", "////","////", "___ ", "___ ","___ ", "___ ", "___ ","___"],
#          ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","___ ", "___ ", "___ ","___"],
#          ["___ ", "___ ", "___ ","___ ", "___ ", "___ ","////", "////", "___ ","___"],
#          ["___ ", "___ ", "___ ","___ ", "////", "___ ","___ ", "___ ", "___ ","___"],
#          ["___ ", "////", "___ ","___ ", "___ ", "___ ","////", "////", "////","___"],
#          ]
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


#gemilerinnin bulundugu konumlar
doluOlanlar = [[0, 1], [0, 2], [0, 3], [0, 4],  #4 birimlik gemi
               [3, 6], [3, 7], [3, 8], [3, 9],
               [5, 1], [5, 2], [5, 3], #3 birimlik gemi
               [9, 6], [9, 7], [9, 8],
               [3, 3], [3, 4], #2 birimlik gemi
               [7, 6], [7, 7],
               [8, 4], #1 birimlik gemi
               [9, 1]
               ]

rakamlar = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

dogruHamleler = []
# kullanicinin dogru hamlelerini bu listeye atayacagiz

strJa = '////'
# gemiye isabet ettiginde hamle yapilan alanda gosterilecek sekil
strNee = 'XXXX'
# gemiye isabet etmediginde hamle yapilan alanda gosterilecek sekil

try:
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
    for i in tablo:
        print("\t".expandtabs(30), *i, end="\n" * 2)
except:
    print('Hata! Programdan cikiliyor...')