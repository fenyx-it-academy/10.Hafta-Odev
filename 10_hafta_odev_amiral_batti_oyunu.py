import random as r
import time
print('b.')
print('>>>>>>>>>>>>>>>>>>>>...Amiral batti oyununa HOSGELDINIZ...<<<<<<<<<<<<<<<<<<<<\n'
      '>>>>>>>>>>>>>>>>>>>>>>>>>>>>.......1.0.......<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'
      '2 tane 4 birim \t( * * * * )\n2 tane 3 birim\t(  * * *  )\n'
      '2 tane 2 birim \t(   * *   )\n2 tane 1 birim \t(    *    )  sekillerinden olusan 8 tane gemi vardir \n'
      'tablodaki dogru kordinatlari girerek 15 tahminde bulmaya calisiniz...Basarilar')

tahta =  [[' '," 1","2","3","4","5","6","7","8","9","10"],
          ['1 ',"-","-","-","-","-","-","-","-","-","-"],
          ['2 ',"-","-","-","-","-","-","-","-","-","-"],
          ['3 ',"-","-","-","-","-","-","-","-","-","-"],
          ['4 ',"-","-","-","-","-","-","-","-","-","-"],
          ['5 ',"-","-","-","-","-","-","-","-","-","-"],
          ['6 ',"-","-","-","-","-","-","-","-","-","-"],
          ['7 ',"-","-","-","-","-","-","-","-","-","-"],
          ['8 ',"-","-","-","-","-","-","-","-","-","-"],
          ['9 ',"-","-","-","-","-","-","-","-","-","-"],
          ['10',"-","-","-","-","-","-","-","-","-","-"]]

def tablo():
    print('-'*70)
    for i in tahta:
       print(*i)
    print("-"*70,'\n( dogru hamleler "*", yanlis hamleler "X" isareti ile belirtilmistir )\n',"-"*70)
tablo()
gemiler=[]      # bos gemiler listesi olusturduk
gemi1=[]
gemi2=[]
gemi3=[]
gemi4=[]
gemi5=[]
gemi6=[]
gemi7=[]
gemi8=[]
# gemilerin kordinatlarini belirledik
# while ile 8 tane rastgele gemi urettirdik
gemi_sayisi=0
while gemi_sayisi<=8:
    gemi_sayisi += 1
    #gemi1
    if gemi1 not in gemiler:
        x=r.randint(1,7)
        y=r.randint(1,7)
        gemi1=[ [x,y],[x,y+1],[x,y+2],[x,y+3] ]
        gemiler.append(gemi1)
    #gemi 2
    elif gemi2 not in gemiler:
        x=r.randint(1,7)
        y=r.randint(1,7)
        gemi2=[ [x,y],[x+1,y],[x+2,y],[x+3,y] ]
        gemiler.append(gemi2)
    # gemi 3
    elif gemi3 not in gemiler:
        x=r.randint(1,8)
        y=r.randint(1,8)
        gemi3=[ [x,y],[x,y+1],[x,y+2] ]
        gemiler.append(gemi3)
    #gemi 4
    elif gemi4 not in gemiler:
        x=r.randint(1,8)
        y=r.randint(1,8)
        gemi4=[ [x,y],[x+1,y],[x+2,y] ]
        gemiler.append(gemi4)
    # gemi 5
    elif gemi5 not in gemiler:
        x = r.randint(1, 9)
        y = r.randint(1, 9)
        gemi5 = [[x, y], [x, y + 1]]
        gemiler.append(gemi5)
    # gemi 6
    elif gemi6 not in gemiler:
        x = r.randint(1, 9)
        y = r.randint(1, 9)
        gemi6 = [[x,y],[x+1,y]]
        gemiler.append(gemi6)
    # gemi 7
    elif gemi7 not in gemiler:
        x = r.randint(1, 10)
        y = r.randint(1, 10)
        gemi7 = [[x, y]]
        gemiler.append(gemi7)
    # gemi 8
    elif gemi8 not in gemiler:
        x = r.randint(1, 10)
        y = r.randint(1, 10)
        gemi8 = [[y, x]]
        gemiler.append(gemi8)
gemi1_hamleler=[]
gemi2_hamleler=[]
gemi3_hamleler=[]
gemi4_hamleler=[]
gemi5_hamleler=[]
gemi6_hamleler=[]
gemi7_hamleler=[]
gemi8_hamleler=[]
#yapilan hamleleri toplamak icin bos yapilan hamleler listesi olusturduk
yapilan_hamleler = []
dogru_gemiler=[]
hak=15
while hak>0:
    try:        # try-except ile sayidan farkli deger girilmesini kontrol ettik
        print(f'{hak} . hakkiniz....basarilar') #kac hakki kaldigini bildirdik
        # kullanicidan input ile kordinatlari aldik
        x = int(input('\nyukaridan asagiya "1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz : '))
        y = int(input('soldan sağa...... "1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz : '))
        print('\n')
        time.sleep(3)       # 3 saniye bekleme koyduk
        if 1 <= x <= 10 and 1 <= y <= 10:  # girilen sayilarin 0 ile 11 arasinda olmasini kontrol ettik
            hamle = [x,y]  # girilen kordinatlari listeye cevirdik
            # if ile yapilan hamle kontrolu yaptik
            if hamle in yapilan_hamleler:
                print('!!!...UYARI...BU HAMLE DAHA ONCE YAPILDI \n')
                continue
            else:
                yapilan_hamleler.append(hamle)  # yapilan hamleleri listemizde ekledik
                tahta[x][y] = 'X'  # 'X' isareti ile oyun tahtamizda yapilan hamleleri belirttik
                # if'ler ile gemilere isabet etme durumlarini inceledik
                if hamle in gemi1:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi1_hamleler.append(hamle)
                    if len(gemi1_hamleler) == 4:
                        print('>>>>>>....Tebrikler...( * * * * ) 4 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                        # gemiyi tamamen bulunca dogru_gemiler list. ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi1)
                if hamle in gemi2:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi2_hamleler.append(hamle)
                    if len(gemi2_hamleler) == 4:
                        print('>>>>>>....Tebrikler...( * * * * ) 4 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                        # gemiyi tamamen bulunca dogru_gemiler list. ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi2)
                if hamle in gemi3:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi3_hamleler.append(hamle)
                    if len(gemi3_hamleler) == 3:
                        print('>>>>>>....Tebrikler...( * * * ) 3 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi3)
                if hamle in gemi4:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi4_hamleler.append(hamle)
                    if len(gemi4_hamleler) == 3:
                        print('>>>>>>....Tebrikler...( * * * ) 3 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi4)
                if hamle in gemi5:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi5_hamleler.append(hamle)
                    if len(gemi5_hamleler) == 2:
                        print('>>>>>>....Tebrikler...( * * ) 2 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi5)
                if hamle in gemi6:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi6_hamleler.append(hamle)
                    if len(gemi6_hamleler) == 2:
                        print('>>>>>>....Tebrikler...( * * ) 2 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi6)
                if hamle in gemi7:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi7_hamleler.append(hamle)
                    if len(gemi7_hamleler) == 1:
                        print('>>>>>>....Tebrikler...( * ) 1 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi7)
                if hamle in gemi8:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi8_hamleler.append(hamle)
                    if len(gemi8_hamleler) == 1:
                        print('>>>>>>....Tebrikler...( * ) 1 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi8)
                tablo()     # fonksiyon ile oyun tahtamizi ekrana yazdirdik
                hak -= 1    # hakkimizi 1 azalttik
        else:
            print('\n!!!...UYARI..."1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz\n')
            continue
        if len(dogru_gemiler) == 8:  # dogru hamleler sayisi ile kazanma durumunu kontrol ettik
            print('\nTEBRIKLER OYUNU KAZANDINIZ')
            quit()
    except ValueError:
        print('Lutfen "1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz')
print(f'{hak} hak....hakkiniz bitti.....KAYBETTINIZ')
