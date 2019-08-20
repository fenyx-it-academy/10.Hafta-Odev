import random as r
import time
print('b.')
print('>>>>>>>>>>>>>>>>>>>>...Amiral batti oyununa HOSGELDINIZ...<<<<<<<<<<<<<<<<<<<<\n'
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

yapilan_hamleler = []
dogru_hamleler=[]
hak=1
while hak<=15:
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
                # if'ler ile gemileri bulma durumlarini inceledik
                if hamle in gemi1:
                    # tahta uzerindeki gemilerin indexlerine isabet ettigini '*' isareti kullanarak belirledik
                    tahta[gemi1[0][0]][gemi1[0][1]] = '*'
                    tahta[gemi1[1][0]][gemi1[1][1]] = '*'
                    tahta[gemi1[2][0]][gemi1[2][1]] = '*'
                    tahta[gemi1[3][0]][gemi1[3][1]] = '*'
                    print('...BOOOOOOOOM...Tebrikler...1.gemiyi buldunuz.......<<<<<<<\n')
                    dogru_hamleler.append(hamle)  # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                    for i in gemi1:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        yapilan_hamleler.append(i)
                if hamle in gemi2:
                    # tahta uzerindeki gemilerin indexlerine isabet ettigini '*' isareti kullanarak belirledik
                    tahta[gemi2[0][0]][gemi2[0][1]] = '*'
                    tahta[gemi2[1][0]][gemi2[1][1]] = '*'
                    tahta[gemi2[2][0]][gemi2[2][1]] = '*'
                    tahta[gemi2[3][0]][gemi2[3][1]] = '*'
                    for i in gemi2:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        yapilan_hamleler.append(i)
                    print('...BOOOOOOOOM...Tebrikler...2.gemiyi buldunuz.......<<<<<<<\n')
                    dogru_hamleler.append(hamle)  #dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                if hamle in gemi3:
                    # tahta uzerindeki gemilerin indexlerine isabet ettigini '*' isareti kullanarak belirledik
                    tahta[gemi3[0][0]][gemi3[0][1]] = '*'
                    tahta[gemi3[1][0]][gemi3[1][1]] = '*'
                    tahta[gemi3[2][0]][gemi3[2][1]] = '*'
                    for i in gemi3:  #dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        yapilan_hamleler.append(i)
                    print('...BOOOOOOOOM...Tebrikler...3.gemiyi buldunuz.......<<<<<<<\n')
                    dogru_hamleler.append(hamle)  #dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                if hamle in gemi4:
                    # tahta uzerindeki gemilerin indexlerine isabet ettigini '*' isareti kullanarak belirledik
                    tahta[gemi4[0][0]][gemi4[0][1]] = '*'
                    tahta[gemi4[1][0]][gemi4[1][1]] = '*'
                    tahta[gemi4[2][0]][gemi4[2][1]] = '*'
                    for i in gemi4:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        yapilan_hamleler.append(i)
                    print('...BOOOOOOOOM...Tebrikler...4.gemiyi buldunuz.......<<<<<<<\n')
                    dogru_hamleler.append(hamle)  #dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                if hamle in gemi5:
                    # tahta uzerindeki gemilerin indexlerine isabet ettigini '*' isareti kullanarak belirledik
                    tahta[gemi5[0][0]][gemi5[0][1]] = '*'
                    tahta[gemi5[1][0]][gemi5[1][1]] = '*'
                    for i in gemi5:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        yapilan_hamleler.append(i)
                    print('...BOOOOOOOOM...Tebrikler...5.gemiyi buldunuz.......<<<<<<<\n')
                    dogru_hamleler.append(
                        hamle)  # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                if hamle in gemi6:
                    # tahta uzerindeki gemilerin indexlerine isabet ettigini '*' isareti kullanarak belirledik
                    tahta[gemi6[0][0]][gemi6[0][1]] = '*'
                    tahta[gemi6[1][0]][gemi6[1][1]] = '*'
                    for i in gemi6:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        yapilan_hamleler.append(i)
                    print('...BOOOOOOOOM...Tebrikler...6.gemiyi buldunuz.......<<<<<<<\n')
                    dogru_hamleler.append(hamle)  #dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                if hamle in gemi7:
                    # tahta uzerindeki gemilerin indexlerine isabet ettigini '*' isareti kullanarak belirledik
                    tahta[gemi7[0][0]][gemi7[0][1]] = '*'
                    for i in gemi7:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        yapilan_hamleler.append(i)
                    print('...BOOOOOOOOM...Tebrikler...7.gemiyi buldunuz.......<<<<<<<\n')
                    dogru_hamleler.append(hamle)  #dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                if hamle in gemi8:
                    # tahta uzerindeki gemilerin indexlerine isabet ettigini '*' isareti kullanarak belirledik
                    tahta[gemi8[0][0]][gemi8[0][1]] = '*'
                    for i in gemi8:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        yapilan_hamleler.append(i)
                    print('...BOOOOOOOOM...Tebrikler...8.gemiyi buldunuz.......<<<<<<<\n')
                    dogru_hamleler.append(hamle)  #dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                tablo()     # fonksiyon ile oyun tahtamizi ekrana yazdirdik
                hak += 1    # hakkimizi 1 arttirdik
        else:
            print('\n!!!...UYARI..."1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz\n')
            continue
        if len(dogru_hamleler) == 8:  # dogru hamleler sayisi ile kazanma durumunu kontrol ettik
            print('\nTEBRIKLER OYUNU KAZANDINIZ')
            quit()
    except ValueError:
        print('Lutfen "1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz')
print(f'{hak-1} hakkiniz bitti.....KAYBETTINIZ')