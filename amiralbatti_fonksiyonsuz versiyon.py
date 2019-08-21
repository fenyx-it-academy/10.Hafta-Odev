import time

print("\nAMIRAL BATTI OYUNU")                                                          # imza sablonumuzun ilk satirini yazdik
print("-" * 6, "ZAFER", "-" * 6, end="\n\n")                                        # imza sablonumuzun ikinci satirini yazdik
                                                                                    # kullaniciya karsilama metni ve menuyu sunduk
print("""Amiral Batti oyunumuza hosgeldiniz.
Oyun alanimiz 10 x 10 ebatindadir.
Oyun alanimizda
    2 tane 4 birim
    2 tane 3 birim
    2 tane 2 birim
    2 tane 1 birim
buyuklugunde gemimiz yer almaktadir.
Girmek istediginiz satir ve sutun numarisini oyun tahtasindan da bakip girerek tercihte bulunabilirsiniz.
15 isabetsiz atis yaparsaniz oyunu kaybedersiniz.
Basarilar.
""")

tahta=[
["    ", "  1  ", "  2  ", "  3  ", "  4  ", "  5  ", "  6  ", "  7  ", "  8  ", "  9  ", " 10  "],
[" 1  ", " 1_1 ", " 1_2 ", " 1_3 ", " 1_4 ", " 1_5 ", " 1_6 ", " 1_7 ", " 1_8 ", " 1_9 ", " 1_10"],
[" 2  ", " 2_1 ", " 2_2 ", " 2_3 ", " 2_4 ", " 2_5 ", " 2_6 ", " 2_7 ", " 2_8 ", " 2_9 ", " 2_10"],
[" 3  ", " 3_1 ", " 3_2 ", " 3_3 ", " 3_4 ", " 3_5 ", " 3_6 ", " 3_7 ", " 3_8 ", " 3_9 ", " 3_10"],
[" 4  ", " 4_1 ", " 4_2 ", " 4_3 ", " 4_4 ", " 4_5 ", " 4_6 ", " 4_7 ", " 4_8 ", " 4_9 ", " 4_10"],
[" 5  ", " 5_1 ", " 5_2 ", " 5_3 ", " 5_4 ", " 5_5 ", " 5_6 ", " 5_7 ", " 5_8 ", " 5_9 ", " 5_10"],
[" 6  ", " 6_1 ", " 6_2 ", " 6_3 ", " 6_4 ", " 6_5 ", " 6_6 ", " 6_7 ", " 6_8 ", " 6_9 ", " 6_10"],
[" 7  ", " 7_1 ", " 7_2 ", " 7_3 ", " 7_4 ", " 7_5 ", " 7_6 ", " 7_7 ", " 7_8 ", " 7_9 ", " 7_10"],
[" 8  ", " 8_1 ", " 8_2 ", " 8_3 ", " 8_4 ", " 8_5 ", " 8_6 ", " 8_7 ", " 8_8 ", " 8_9 ", " 8_10"],
[" 9  ", " 9_1 ", " 9_2 ", " 9_3 ", " 9_4 ", " 9_5 ", " 9_6 ", " 9_7 ", " 9_8 ", " 9_9 ", " 9_10"],
["10  ", "10_1 ", "10_2 ", "10_3 ", " 10_4 ", "10_5 ", "10_6 ", "10_7 ", "10_8 ", "10_9 ", "10_10"],
]

for i in tahta:
    print(*i, end="\n\n")

print("Lutfen yapacaginiz atisi dusunerek bekleyiniz...")

time.sleep(1)


tum = [tahta[3][3], tahta[3][4], tahta[3][5], tahta[3][6], tahta[6][7], tahta[7][7], tahta[8][7], tahta[9][7], tahta[6][2], tahta[7][2], tahta[8][2], tahta[5][9], tahta[6][9], tahta[7][9], tahta[1][10], tahta[2][10], tahta[10][3], tahta[10][4], tahta[1][2], tahta[9][9]]
dortluk_1=[tahta[3][3], tahta[3][4], tahta[3][5], tahta[3][6]]
dortluk_2=[tahta[6][7], tahta[7][7], tahta[8][7], tahta[9][7]]
ucluk_1=[tahta[6][2], tahta[7][2], tahta[8][2]]
ucluk_2=[tahta[5][9], tahta[6][9], tahta[7][9]]
ikilik_1=[tahta[1][10], tahta[2][10]]
ikilik_2=[tahta[10][3], tahta[10][4]]
birlik_1=[tahta[1][2]]
birlik_2=[tahta[9][9]]

isabet_4_1 = []
isabet_4_2 = []
isabet_3_1 = []
isabet_3_2 = []
isabet_2_1 = []
isabet_2_2 = []
isabet_1_1 = []
isabet_1_2 = []

rakamlar="0123456789"

atis_sayisi=1

while atis_sayisi < 16:

    if len(isabet_4_1)==4 and len(isabet_4_2)==4 and len(isabet_3_1)==3 and len(isabet_3_2)==3 and len(isabet_2_1)==2 and len(isabet_2_2)==2 and len(isabet_1_1)==1 and len(isabet_1_2)==1:
        print("TEBRIKLER. OYUNU KAZANDINIZ. TUM DUSMAN GEMILERI BATIRDINIZ.")
        quit()

    satir=int(input("Lutfen satir verisini giriniz (1-10 arasi) : "))
    if satir < 0 or satir > 11:
        print("Yanlis veri girdiniz. Lutfen 1 - 10 arasi bir veri giriniz.\n")
        continue

    sutun=int(input("Lutfen sutun verisini giriniz (1-10 arasi) : "))
    if sutun < 0 or sutun > 11:
        print("Yanlis veri girdiniz. Lutfen 1 - 10 arasi bir veri giriniz.\n")
        continue

    kalan_atis = 15 - atis_sayisi

    if tahta[satir][sutun] not in tum:
        print("Atisiniz isabetsiz.", "Kalan atis hakkiniz :", kalan_atis)
        print("Hatanizin sonucunu bekleyin ...\n")
        atis_sayisi+=1
        time.sleep(5)

    if tahta[satir][sutun] in tum:

        if tahta[satir][sutun] in dortluk_1:
            isabet_4_1.append(tahta[satir][sutun])
            if len(isabet_4_1) <= 3:
                print("Tebrikler. 4'luk bir gemiye isabet ettirdiniz.")
                tahta[satir][sutun] = "**** "
                for i in tahta:
                    print(*i, end="\n\n")
            if len(isabet_4_1) == 4:
                print("Tebrikler. 4'luk bir gemiyi batirdiniz.")
                tahta[satir][sutun] = "**** "
                for i in tahta:
                    print(*i, end="\n\n")

        if tahta[satir][sutun] in dortluk_2:
            isabet_4_2.append(tahta[satir][sutun])
            if len(isabet_4_2) <= 3:
                print("Tebrikler. 4'luk bir gemiye isabet ettirdiniz.")
                tahta[satir][sutun] = "**** "
                for i in tahta:
                    print(*i, end="\n\n")
            if len(isabet_4_2) == 4:
                print("Tebrikler. 4'luk bir gemiyi batirdiniz.")
                tahta[satir][sutun] = "**** "
                for i in tahta:
                    print(*i, end="\n\n")

        if tahta[satir][sutun] in ucluk_1:
            isabet_3_1.append(tahta[satir][sutun])
            if len(isabet_3_1) <= 2:
                print("Tebrikler. 3'luk bir gemiye isabet ettirdiniz.")
                tahta[satir][sutun] = " *** "
                for i in tahta:
                    print(*i, end="\n\n")
            if len(isabet_3_1) == 3:
                print("Tebrikler. 3'luk bir gemiyi batirdiniz.")
                tahta[satir][sutun] = " *** "
                for i in tahta:
                    print(*i, end="\n\n")

        if tahta[satir][sutun] in ucluk_2:
            isabet_3_2.append(tahta[satir][sutun])
            if len(isabet_3_2) <= 2:
                print("Tebrikler. 3'luk bir gemiye isabet ettirdiniz.")
                tahta[satir][sutun] = " *** "
                for i in tahta:
                    print(*i, end="\n\n")
            if len(isabet_3_2) == 3:
                print("Tebrikler. 3'luk bir gemiyi batirdiniz.")
                tahta[satir][sutun] = " *** "
                for i in tahta:
                    print(*i, end="\n\n")

        if tahta[satir][sutun] in ikilik_1:
            isabet_2_1.append(tahta[satir][sutun])
            if len(isabet_2_1) <= 1:
                print("Tebrikler. 2'lik bir gemiye isabet ettirdiniz.")
                tahta[satir][sutun] = "  ** "
                for i in tahta:
                    print(*i, end="\n\n")
            if len(isabet_2_1) == 2:
                print("Tebrikler. 2'lik bir gemiyi batirdiniz.")
                tahta[satir][sutun] = "  ** "
                for i in tahta:
                    print(*i, end="\n\n")

        if tahta[satir][sutun] in ikilik_2:
            isabet_2_2.append(tahta[satir][sutun])
            if len(isabet_2_2) <= 1:
                print("Tebrikler. 2'lik bir gemiye isabet ettirdiniz.")
                tahta[satir][sutun] = "  ** "
                for i in tahta:
                    print(*i, end="\n\n")
            if len(isabet_2_2) == 2:
                print("Tebrikler. 2'lik bir gemiyi batirdiniz.")
                tahta[satir][sutun] = "  ** "
                for i in tahta:
                    print(*i, end="\n\n")

        if tahta[satir][sutun] in birlik_1:
            isabet_1_1.append(tahta[satir][sutun])
            print("Tebrikler. 1'lik bir gemiyi batirdiniz.")
            tahta[satir][sutun] = "  *  "
            for i in tahta:
                print(*i, end="\n\n")

        if tahta[satir][sutun] in birlik_2:
            isabet_1_2.append(tahta[satir][sutun])
            print("Tebrikler. 1'lik bir gemiyi batirdiniz.")
            tahta[satir][sutun] = "  *  "
            for i in tahta:
                print(*i, end="\n\n")
print("15 hata hakkiniz doldu. Ne yazik ki oyunu kaybettiniz.")