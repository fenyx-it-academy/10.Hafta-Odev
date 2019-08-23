#10. HAFTA ÖDEV#

import time


print("""Amiral Batti oyununa hosgeldiniz.
Sahada;
**2 tane 4 birim
**2 tane 3 birim
**2 tane 2 birim
**2 tane 1 birim gemimiz yer almaktadir.

Gemi herhangi bir yerinden vurulursa batacaktır.
Girmek istediginiz numaralari dikey ve yatay olarak giriniz.
15 hakkiniz vardir.
BOL SANS...\n\n""")

saha=[
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


dort1=[saha[3][3], saha[3][4], saha[3][5], saha[3][6]]
dort2=[saha[6][7], saha[7][7], saha[8][7], saha[9][7]]
uc1=[saha[6][2], saha[7][2], saha[8][2]]
uc2=[saha[5][9], saha[6][9], saha[7][9]]
iki1=[saha[1][10], saha[2][10]]
iki2=[saha[10][3], saha[10][4]]
bir1=[saha[1][2]]
bir2=[saha[9][9]]
toplam=dort1+dort2+uc1+uc2+iki1+iki2+bir1+bir2

vurma41=[]
vurma42=[]
vurma31=[]
vurma32=[]
vurma21=[]
vurma22=[]
vurma11=[]
vurma12=[]


hak=1

while hak < 16:
    
    try:
        if bool(vurma41)==True and bool(vurma42)==True and bool(vurma31)==True and bool(vurma32)==True and bool(vurma21)==True and bool(vurma22)==True and bool(vurma11)==True and bool(vurma12)==True:
            print("TEBRIKLER KAZANDINIZ!!!")#TUM GEMİLER VURULURSA KAZANIYORUZ#
            break

        dikey=int(input("Lutfen sayi giriniz(1-10 arasi) : "))
        if dikey < 0 or dikey> 10:
            print("Talimatlara uyunuz(sayilar 1-10 arasi olacak!!).\n")
            continue

        yatay=int(input("Lutfen sayi giriniz (1-10 arasi) : "))
        if yatay < 0 or yatay > 10:
            print("Taliatlara uyalim(sayilar 1-10 arasi olacak!!).\n")
            continue

        kalan=15-hak
        if kalan==0:
            print("KAYBETTİNİZ ÜZGÜNÜZ")
            quit()#hakkımız biterse programdan cikiyoruz#

        if saha[dikey][yatay] not in toplam:
            hak+=1
            saha[dikey][yatay]="X"#ISKA GECERSE X KOYUYORUZ#
            print("Karavana", "Kalan atis hakkiniz:   ", kalan)
            print("Taraniyor...\n\n")
            
            time.sleep(5)
            
            

        if saha[dikey][yatay]=="X":
            print("Bu hamleyi yaptiniz tekrar !!","Kalan hak:  ",kalan)#AYNI HAMLEDE UYARI AMA HAK KAYBI OLMASIN#
            continue

        if saha[dikey][yatay] in toplam:

            if saha[dikey][yatay] in dort1:
                vurma41.append(saha[dikey][yatay])
                saha.append(saha[dikey][yatay])
                saha[dikey][yatay] = "**** "
                print("Tebrikler. 4'luk bir gemiyi batirdiniz.")#GEMİNİN HERHANGİ BİR YERİNE CARPARSA TAMAMINI BATIRIYORUZ #
                
                for i in saha:
                    print(*i, end="\n\n\n")#DOGRU TAHMINDE TABLOYU BASIYORUZ#
                

            if saha[dikey][yatay] in dort2:
                vurma42.append(saha[dikey][yatay])
                saha.append(saha[dikey][yatay])
                print("Tebrikler.2. 4'luk gemiyi batirdiniz.")
                saha[dikey][yatay] = "**** "
                for i in saha:
                    print(*i, end="\n\n\n")
                

            if saha[dikey][yatay] in uc1:
                vurma31.append(saha[dikey][yatay])
                saha.append(saha[dikey][yatay])
                print("Tebrikler. 3'luk gemiyi batirdiniz.")
                saha[dikey][yatay] = " *** "
                for i in saha:
                    print(*i, end="\n\n\n")
                
            if saha[dikey][yatay] in uc2:
                vurma32.append(saha[dikey][yatay])
                saha.append(saha[dikey][yatay])
                print("Tebrikler.2. bir  3'luk gemi batirdiniz.")
                saha[dikey][yatay] = " *** "
                for i in saha:
                    print(*i, end="\n\n\n")
                
    
            if saha[dikey][yatay] in iki1:
                vurma21.append(saha[dikey][yatay])
                saha.append(saha[dikey][yatay])
                print("Tebrikler. 2'lik bir gemi batirdiniz.")
                saha[dikey][yatay] = "  ** "
                for i in saha:
                    print(*i, end="\n\n\n")
                

            if saha[dikey][yatay] in iki2:
                vurma22.append(saha[dikey][yatay])
                saha.append(saha[dikey][yatay])
                print("Tebrikler.2. bir  2'lik gemi batirdiniz.")
                saha[dikey][yatay] = "  ** "
                for i in saha:
                    print(*i, end="\n\n\n")
                
            if saha[dikey][yatay] in bir1:
                vurma11.append(saha[dikey][yatay])
                saha.append(saha[dikey][yatay])
                print("Tebrikler. 1'lik bir gemiyi batirdiniz.")
                saha[dikey][yatay] = "  *  "
                for i in saha:
                    print(*i, end="\n\n\n")

            if saha[dikey][yatay] in bir2:
                vurma12.append(saha[dikey][yatay])
                saha.append(saha[dikey][yatay])
                print("Tebrikler.2. bir  1'lik bir gemiyi batirdiniz.")
                saha[dikey][yatay] = "  *  "
                for i in saha:
                    print(*i, end="\n\n\n")
             
    except:
        print("Bir hata olustu tekrar deneyiniz!!")

