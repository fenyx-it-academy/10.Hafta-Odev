import random
import time

aciklama=""" Bu bir amiral batti oyunu olup:
       Oyunda 2 adet dort birimlik 
              2 adet 3 birimlik
              2 adet 2 birimlik
              2 adet 1 birimlik
       gemiler yatay yada dikey eksende konumlandirilmistir.
       Oyunda sizden gemilerin yerini tahmin etmeniz istenmektedir.
       Eger gemiyi vurursaniz X vuramazsaniz 0 isereti gorunecektir.
       Ayrica her deneme oncesinde 5 sn kadar bekleme suresi bulunmakta olup 
       bu sureye dikkat etmeniz de gerekmektedir.
       Oyunda 25 yanlis yapma hakkina sahipsiniz.

"""
print(aciklama)



tahtaliste=[["___", "___", "___","___", "___", "___","___", "___", "___","___"],
["___", "___", "___","___", "___", "___","___", "___", "___","___"],
["___", "___", "___","___", "___", "___","___", "___", "___","___"],
["___", "___", "___","___", "___", "___","___", "___", "___","___"],
["___", "___", "___","___", "___", "___","___", "___", "___","___"],
["___", "___", "___","___", "___", "___","___", "___", "___","___"],
["___", "___", "___","___", "___", "___","___", "___", "___","___"],
["___", "___", "___","___", "___", "___","___", "___", "___","___"],
["___", "___", "___","___", "___", "___","___", "___", "___","___"],
["___", "___", "___","___", "___", "___","___", "___", "___","___"]]

tahtasozluk={

   'A1': 0, 'A2': 1, 'A3': 2, 'A4': 3, 'A5': 4, 'A6': 5, 'A7': 6, 'A8': 7, 'A9': 8, 'A10': 9,
   'B1': 10, 'B2': 11, 'B3': 12, 'B4': 13, 'B5': 14, 'B6': 15, 'B7': 16, 'B8': 17, 'B9': 18, 'B10': 19,
   'C1': 20, 'C2': 21, 'C3': 22, 'C4': 23, 'C5': 24, 'C6': 25, 'C7': 26, 'C8': 27, 'C9': 28, 'C10': 29,
   'D1': 30, 'D2': 31, 'D3': 32, 'D4': 33, 'D5': 34, 'D6': 35, 'D7': 36, 'D8': 37, 'D9': 38, 'D10': 39,
   'E1': 40, 'E2': 41, 'E3': 42, 'E4': 43, 'E5': 44, 'E6': 45, 'E7': 46, 'E8': 47, 'E9': 48, 'E10': 49,
   'F1': 50, 'F2': 51, 'F3': 52, 'F4': 53, 'F5': 54, 'F6': 55, 'F7': 56, 'F8': 57, 'F9': 58, 'F10': 59,
   'G1': 60, 'G2': 61, 'G3': 62, 'G4': 63, 'G5': 64, 'G6': 65, 'G7': 66, 'G8': 67, 'G9': 68, 'G10': 69,
   'H1': 70, 'H2': 71, 'H3': 72, 'H4': 73, 'H5': 74, 'H6': 75, 'H7': 76, 'H8': 77, 'H9': 78, 'H10': 79,
   'J1': 80, 'J2': 81, 'J3': 82, 'J4': 83, 'J5': 84, 'J6': 85, 'J7': 86, 'J8': 87, 'J9': 88, 'J10': 89,
   'K1': 90, 'K2': 91, 'K3': 92, 'K4': 93, 'K5': 94, 'K6': 95, 'K7': 96, 'K8': 97, 'K9': 98, 'K10': 99,
}

def tahta():
    global tahtaliste
    k=0
    alfabe=["A","B","C","D","E","F","G","H","J","K"]
    print("\t".expandtabs(32),' ',1,'\t'.expandtabs(1),2,'\t'.expandtabs(1),3,'\t'.expandtabs(1),4,'\t'.expandtabs(1),5,'\t'.expandtabs(1), 6,'\t'.expandtabs(1),7,'\t'.expandtabs(1),8,'\t'.expandtabs(1),9,'\t'.expandtabs(1),10, end="\n"*2)
    for i in tahtaliste:
        print("\t".expandtabs(30),alfabe[k],'', *i, end="\n"*2)
        k+=1

def dortluk():
    liste1=[]
    def belirleme(i,j):
        for i in range(i,j):
            liste1.append([i, i + 1, i + 2, i + 3])
    belirleme(0,7)
    belirleme(10,17)
    belirleme(20,27)
    belirleme(30,37)
    belirleme(40,47)
    belirleme(50,57)
    belirleme(60,67)
    belirleme(70,77)
    belirleme(80,87)
    belirleme(90,97)
    def belirleme1(i,j):
        for i in range(i,j):
            liste1.append([i*10, i*10+10, i*10 + 20, i*10 + 30])
    def belirleme2(i,j):
        for i in range(i,j):
            liste1.append([i*10+1, i*10+11, i*10 + 21, i*10 + 31])
    def belirleme3(i,j):
        for i in range(i,j):
            liste1.append([i*10+2, i*10+12, i*10 + 22, i*10 + 32])
    def belirleme4(i,j):
        for i in range(i,j):
            liste1.append([i*10+3, i*10+13, i*10 + 23, i*10 + 33])
    def belirleme5(i,j):
        for i in range(i,j):
            liste1.append([i*10+4, i*10+14, i*10 + 24, i*10 + 34])
    def belirleme6(i,j):
        for i in range(i,j):
            liste1.append([i*10+5, i*10+15, i*10 + 25, i*10 + 35])
    def belirleme7(i,j):
        for i in range(i,j):
            liste1.append([i*10+6, i*10+16, i*10 + 26, i*10 + 36])
    def belirleme8(i, j):
        for i in range(i, j):
            liste1.append([i * 10 + 7, i * 10 + 17, i * 10 + 27, i * 10 + 37])
    def belirleme9(i, j):
        for i in range(i, j):
            liste1.append([i * 10 + 8, i * 10 + 18, i * 10 + 28, i * 10 + 38])
    def belirleme10(i, j):
        for i in range(i, j):
            liste1.append([i * 10 + 9, i * 10 + 19, i * 10 + 29, i * 10 + 39])
    belirleme1(0,7)
    belirleme2(0,7)
    belirleme3(0,7)
    belirleme4(0,7)
    belirleme5(0,7)
    belirleme6(0,7)
    belirleme7(0,7)
    belirleme8(0,7)
    belirleme9(0,7)
    belirleme10(0,7)
    return liste1

def ucluk():
    liste1=[]
    def belirleme(i,j):
        for i in range(i,j):
            liste1.append([i, i + 1, i + 2])
    belirleme(0,8)
    belirleme(10,18)
    belirleme(20,28)
    belirleme(30,38)
    belirleme(40,48)
    belirleme(50,58)
    belirleme(60,68)
    belirleme(70,78)
    belirleme(80,88)
    belirleme(90,98)
    def belirleme1(i,j):
        for i in range(i,j):
            liste1.append([i*10, i*10+10, i*10 + 20])
    def belirleme2(i,j):
        for i in range(i,j):
            liste1.append([i*10+1, i*10+11, i*10 + 21])
    def belirleme3(i,j):
        for i in range(i,j):
            liste1.append([i*10+2, i*10+12, i*10 + 22])
    def belirleme4(i,j):
        for i in range(i,j):
            liste1.append([i*10+3, i*10+13, i*10 + 23])
    def belirleme5(i,j):
        for i in range(i,j):
            liste1.append([i*10+4, i*10+14, i*10 + 24])
    def belirleme6(i,j):
        for i in range(i,j):
            liste1.append([i*10+5, i*10+15, i*10 + 25])
    def belirleme7(i,j):
        for i in range(i,j):
            liste1.append([i*10+6, i*10+16, i*10 + 26])
    def belirleme8(i, j):
        for i in range(i, j):
            liste1.append([i * 10 + 7, i * 10 + 17, i * 10 + 27])
    def belirleme9(i, j):
        for i in range(i, j):
            liste1.append([i * 10 + 8, i * 10 + 18, i * 10 + 28])
    def belirleme10(i, j):
        for i in range(i, j):
            liste1.append([i * 10 + 9, i * 10 + 19, i * 10 + 29])
    belirleme1(0,8)
    belirleme2(0,8)
    belirleme3(0,8)
    belirleme4(0,8)
    belirleme5(0,8)
    belirleme6(0,8)
    belirleme7(0,8)
    belirleme8(0,8)
    belirleme9(0,8)
    belirleme10(0,8)
    return liste1

def ikilik():
    liste1=[]
    def belirleme(i,j):
        for i in range(i,j):
            liste1.append([i, i + 1])
    belirleme(0,9)
    belirleme(10,19)
    belirleme(20,29)
    belirleme(30,39)
    belirleme(40,49)
    belirleme(50,59)
    belirleme(60,69)
    belirleme(70,79)
    belirleme(80,89)
    belirleme(90,99)
    def belirleme1(i,j):
        for i in range(i,j):
            liste1.append([i*10, i*10+10])
    def belirleme2(i,j):
        for i in range(i,j):
            liste1.append([i*10+1, i*10+11])
    def belirleme3(i,j):
        for i in range(i,j):
            liste1.append([i*10+2, i*10+12])
    def belirleme4(i,j):
        for i in range(i,j):
            liste1.append([i*10+3, i*10+13])
    def belirleme5(i,j):
        for i in range(i,j):
            liste1.append([i*10+4, i*10+14])
    def belirleme6(i,j):
        for i in range(i,j):
            liste1.append([i*10+5, i*10+15])
    def belirleme7(i,j):
        for i in range(i,j):
            liste1.append([i*10+6, i*10+16])
    def belirleme8(i, j):
        for i in range(i, j):
            liste1.append([i * 10 + 7, i * 10 + 17])
    def belirleme9(i, j):
        for i in range(i, j):
            liste1.append([i * 10 + 8, i * 10 + 18])
    def belirleme10(i, j):
        for i in range(i, j):
            liste1.append([i * 10 + 9, i * 10 + 19])
    belirleme1(0,9)
    belirleme2(0,9)
    belirleme3(0,9)
    belirleme4(0,9)
    belirleme5(0,9)
    belirleme6(0,9)
    belirleme7(0,9)
    belirleme8(0,9)
    belirleme9(0,9)
    belirleme10(0,9)
    return liste1
def birlik():
    liste1 = list(map(lambda x: x, range(0, 100)))
    return liste1
def yerler():
    dortluk1=random.sample(dortluk(),2)
    while True:
        ucluk1=random.sample(ucluk(),2)
        ikilik1=random.sample(ikilik(),2)
        birlik1=random.sample(birlik(),2)

        if ucluk1 in dortluk1 or ikilik1 in dortluk1 or ikilik1 in ucluk1 or birlik1 in ikilik1 or birlik1 in ikilik1 or birlik1 in ucluk1 or birlik1 in dortluk1:
            continue
        else:
            break
    return dortluk1,ucluk1,ikilik1,birlik1

liste=yerler()
liste1=[liste[0][0][0],liste[0][0][1],liste[0][0][2],liste[0][0][3],liste[0][1][0],liste[0][1][1],liste[0][1][2],liste[0][1][3],liste[1][0][0],liste[1][0][1],liste[1][0][2],liste[1][1][0],liste[1][1][1],liste[1][1][2],liste[2][0][0],liste[2][0][1],liste[2][1][0],liste[2][1][1],liste[3][0],liste[3][1]]

def giriskontrol():
    global liste1
    liste2 = []
    dogru=[]
    yanlis=[]
    sayac=0
    while sayac<25:
        tahta()
        print("Lutfen giris yapmadan once 5 saniye bekleyiniz!!!!!! ")
        time.sleep(5)
        harf = input("Lutfen oynamak istediginiz yeri 'D6' seklinde seciniz:\t")
        harf=harf.upper()
        if harf[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] and harf[0] in ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K"]:
            deger=tahtasozluk.get(harf)
            if deger in liste1:
                if deger in dogru:
                    print("Daha once ayni tahminde bulunmussunuz")
                    print("{} tahmin hakkiniz kalmistir".format(25 - sayac))
                    continue
                else:
                    dogru.append(deger)
                    liste = []
                    deger = str(deger)
                    for i in deger:
                        liste.append(i)
                    if len(liste)==1:
                        liste.insert(0,0)
                    isaret = "X".center(3)
                    tahtaliste[int(liste[0])][int(liste[1])]=isaret
                    liste1.sort()
                    dogru.sort()
                    print("{} tahmin hakkiniz kalmistir".format(25 - sayac))
                    if dogru==liste1:
                        print("Tebrik ederiz tum gemileri vurdunuz")
                        quit()
                    else:
                        continue
            else:
                if deger in yanlis:
                    print("Daha once ayni tahminde bulunmussunuz")
                    print("{} tahmin hakkiniz kalmistir".format(25 - sayac))
                    continue
                else:

                    sayac+=1
                    print("Malesef yanlis bir tahminde bulundunuz")
                    print("{} tahmin hakkiniz kalmistir".format(25-sayac))
                    yanlis.append(deger)
                    liste = []
                    deger = str(deger)
                    for i in deger:
                        liste.append(i)
                    if len(liste)==1:
                        liste.insert(0,0)
                    isaret = "0".center(3)
                    tahtaliste[int(liste[0])][int(liste[1])] = isaret
                    continue
            continue
        else:
            print("yanlis deger girdiniz lutfen tekrar giriniz:\t")
            print("{} tahmin hakkiniz kalmistir".format(25 - sayac))
            continue
    print("Malesef tum haklarinizi kullandiniz. Tekrar deneyiniz")
    quit()

giriskontrol()
