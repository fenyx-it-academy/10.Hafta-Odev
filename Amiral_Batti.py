"""
ODEV: AMIRAL BATTI
Deniz olarak varsayacagimiz 10x10'luk bir tablo olusturun (X-O-X oyununa benzer). Bu tabloya 2 adet 4 birimlik,
2 adet 3 birimlik, 2 adet 2 birimlik ve 2 adet 1 birimlik gemiler yerlestirin.
Yerlestirdiginiz gemileri kullanici gormeyecek. Kullanicidan tablo uzerindeki herhangi bir noktaya hamlede bulunmasini isteyin.
Kullanicinin hamlesi gemilerin herhangi bir noktasina isabet ederse kullaniciya tablo uzerinde bunu gosterin.
Ayni sekilde bosa atis yaptiginda da kullaniciya tablo uzerinde bunu gosterin ve kullanicinin 5 sn boyunca hamle yapmasini engelleyin.
Kullanici daha once hamle yapmis oldugu bir noktaya tekrar hamlede bulunursa bunu engelleyin.
Kullaniciya toplamda 15 yanlis hamle hakki verin. Kullanici tum gemileri vurdugunda oyunu bitirin.
Oyunu mumkun oldugunca fonksiyonlar kullanarak yapmanizi istiyoruz.
BONUS(ISTEGE BAGLI): Yukaridaki versiyonda gemiler sabit. Oyunu her actigimizda gemilerin yeri degismiyor. Isteyenler gemilerin random yerlestirildigi bir versiyonunu yapabilir.
"""
import random
import time
tablo=[["O" for i in range(0,10) ] for j in range(0,10)]
gemiler=[]
def gemi_olusturma():
    gemi_tablosu = [[[i,j] for j in range(0,10)] for i in range(0,10)]
    dort_birimlik_gemiler = []
    uc_birimlik_gemiler = []
    iki_birimlik_gemiler = []
    bir_birimlik_gemiler = []
    for j in range(0, 2):
        a = random.randint(0, 4)
        for i in range(4):
                b=0
                kordinat=gemi_tablosu[a][b]
                b+=1
                dort_birimlik_gemiler.append(kordinat)
                k=-1
                for l in gemi_tablosu:
                    k += 1
                    for j in l:
                        if j == kordinat:
                           gemi_tablosu[k].remove(j)
        a = random.randint(0, 3)
        for i in range(3):
                b=0
                kordinat=gemi_tablosu[a][b]
                b+=1
                uc_birimlik_gemiler.append(kordinat)
                k = -1
                for l in gemi_tablosu:
                    k += 1
                    for j in l:
                        if j == kordinat:
                            gemi_tablosu[k].remove(j)
        a = random.randint(4, 7)
        for i in range(2):
                b=0
                kordinat=gemi_tablosu [a][b]
                b += 1
                iki_birimlik_gemiler.append(kordinat)
                k = -1
                for l in gemi_tablosu:
                    k += 1
                    for j in l:
                        if j == kordinat:
                            gemi_tablosu[k].remove(j)
        for i in range(1):
                a = random.randint(6,8)
                kordinat=gemi_tablosu[a][i]
                bir_birimlik_gemiler.append(kordinat)
                k = -1
                for l in gemi_tablosu:
                    k += 1
                    for j in l:
                        if j == kordinat:
                            gemi_tablosu[k].remove(j)

    gemiler.append(dort_birimlik_gemiler[0:4])
    gemiler.append(dort_birimlik_gemiler[4:8])
    gemiler.append(uc_birimlik_gemiler[0:3])
    gemiler.append(uc_birimlik_gemiler[3:6])
    gemiler.append(iki_birimlik_gemiler[0:2])
    gemiler.append(iki_birimlik_gemiler[2:4])
    gemiler.append(bir_birimlik_gemiler[0:1])
    gemiler.append(bir_birimlik_gemiler[1:2])
    return gemiler

hamle_koordinat = []
counter=0
batan_gemiler=[]

def hamle_kontrol(x):
    if [x[0],x[1]] not in hamle_koordinat:
        hamle_koordinat.append([x[0],x[1]])
        return 0
    return 1

def hamle():
    for row in tablo:
        print("                      "," ".join(row))
    print("     Lutfen bir hamle de bununuz")
    x = int(input("     Yukaridan asagiya (1 den 10 a kadar):"))
    y = int(input("     Soldan saga (1 den 10 a kadar):"))
    x = x - 1
    y = y - 1
    return [x, y]

def gemi_batirma(x):
    for i in gemiler:
        for j in i:
            if j==[x[0],x[1]]:
                gemiler.pop(gemiler.index(i))
                return i# gonderilen kordinatlar listede varsa gemiye rastgelmistir.ve geminin kordinatlari donulur
    return 1

def gemiyi_goster(a):
    for i in a:
        tablo[i[0]][i[1]] = "X"#gonderilen kordinatlardaki harfler X ile degistirilir
    for i in tablo:
        print("                      "," ".join(i))

def bosu_goster(x):
    tablo[x[0]][x[1]]="B"#gonderilen kordinatlardaki yerler B ile degistirilir. Alanin bos oldugu anlamina gelir
    for i in tablo:
        print("                      "," ".join(i))

print("""         ------------AMIRAL BATTI OYUNU------------
         -----------2 Adet 4 birimlik--------------
         -----------2 Adet 3 birimlik--------------
         -----------2 Adet 2 birimlik--------------
         -----------2 Adet 1 birimlik--------------
         -----------Gemiler bulunmaktadir----------
         -Toplam 15 yanlis hakkiniz bulunmaktadir--
         ---------------BASARILAR------------------         
""")
try:
    a=gemi_olusturma()#random gemi olusturuluyor
except:
    print("Beklenmeyen bir hata olsutu. Lutfen tekrar deneyiniz!!!!")
    quit()
batan_gemi_sayisi=0
while True:
    print("Kalan yanlis hamle sayiniz:", 15-counter)
    if len(a)>=1:
        if counter==15:#15 hak dolma kontrolu
            print("15 hamle hakkiniz doldu. Oyunu kaybettiniz.\nBulunamayan gemiler Y harfi ile gosterilmistir.")
            for i in gemiler:
                for j in i:
                    tablo[j[0]][j[1]] = "Y"# 15 hak dolduktan sonra bulunamayan gemiler Y harfi ile gosteriliyor.
            for i in tablo:
                print("                      ", " ".join(i))
            break
        else:
            koordinat=hamle()# kullanicinin hamleleri aliniyor.
            if hamle_kontrol(koordinat)==0:# onceden girilen bir kordinat mi diye bakiliyor
                counter += 1 #oynanan hak bir artiriliyor.
                sonuc=gemi_batirma(koordinat)#koordinatlar herhangi bir geminin kordinati mi diye bakiliyor.
                if sonuc!=1:# kordinat bir gemiye aitse
                    gemiyi_goster(sonuc)#gemi tabloya ekleniyor ve gosteriliyor.
                    print("BU HAMLEDE BIR GEMI BATTI. TEBRIKLER. IYI GIDIYORSUNUZ..")
                    batan_gemi_sayisi+=1
                    print("Batan gemi sayisi: {}, kalan gemi sayisi:{}".format(batan_gemi_sayisi,8-batan_gemi_sayisi))
                    counter-=1#oyun hakki azalmasin diye oynanan haklar bir eksiltiliyor.
                elif sonuc==1 and tablo[koordinat[0]] [koordinat [1]] =="O":#oynan kordinat bir gemiye ait degilse ve tabloda bos alansa. B harfi ile degistiriliyor.
                    bosu_goster(koordinat)#tablo yazdiriliyor.
                    print("Bos hamle yaptiginiz icin 5 sn bekleyeceksiniz.")
                    time.sleep(5)#bos hamlede 5 sn bekletiliyor.
                    print ("Oyun devam ediyor.")
                elif sonuc==1 and tablo[koordinat[0]] [koordinat [1]] =="X":#kordinat onceden bulunan bir gemiye ait mi kontrolu yapiliyor.
                    print("Bu alan batirilan bir geminin parcasi.")
                    counter-=1#onceden bulunan bir gemiye aitse hakki azalmasin diye eksiltme yapiliyor.
            elif hamle_kontrol(koordinat)==1:
                print("     !!!!BU HAMLEYI ONCEDEN YAPMISTINIZ!!!")
    else:
        print("     BUTUN GEMILER BATIRILDI....TEBRIKLER")
        break