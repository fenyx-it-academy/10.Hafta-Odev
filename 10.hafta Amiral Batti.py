from random import randint          #randomun sadece randint fonksiyonu cagrilir.
import time                         ##Bir de zamamlama icin time fonk. cagirilir.
tahta = []


for i in range(10):                 #Tahtamizin 10*10 seklinde bir alan olmasini sagliyoruz.
    tahta.append(["0"]*10)
def goster(tahta):
    for satir in tahta:             #İki fonksiyon tanimlayip tahtayi sekillendirelim ve
        print (" ".join(satir))     #Gemi secimleri icin 'rand' diye bir tanimlama yapalim.
def rand(tahta):
    return randint(1,len(tahta)-1)
print("-" * 50)
print("""
                Amiral Batti Oyunu
        Gemileri batirmak icin satir ve sutun
       degerleri giriniz. Satir ve sutun olarak
        10x10'luk bir tathta belirlenmistir.
            Degerleri buna gore giriniz.
            Denizde 8 adet gemi bulunmakta ve
        bunlari batirmak icin 15 hata yapmabilme
              hakkiniz bulunmaktadir...
              
                  Bol Sanslar!!!
        """)
print("-" * 50)

goster(tahta)                       #8 adet randomla belirlenen gemi sectik.
gemi1_satir =rand(tahta)
gemi1_sutun =rand(tahta)
gemi2_satir =rand(tahta)
gemi2_sutun =rand(tahta)
gemi3_satir =rand(tahta)
gemi3_sutun =rand(tahta)
gemi4_satir =rand(tahta)
gemi4_sutun =rand(tahta)
gemi5_satir =rand(tahta)
gemi5_sutun =rand(tahta)
gemi6_satir =rand(tahta)
gemi6_sutun =rand(tahta)
gemi7_satir =rand(tahta)
gemi7_sutun =rand(tahta)
gemi8_satir =rand(tahta)
gemi8_sutun =rand(tahta)
sayac=0

try:
    while sayac<16:                                         #Oyuncunun 15 hata yapma hakki olabilecegi sayac kurduk.
        tahmin_satir = int(input("Satir giriniz: "))
        tahmin_sutun = int(input("Sütun giriniz: "))        #İnputlari alip bunlari gemilerin bulunduklari yerle karsilastirdik.
        if ((tahmin_satir == gemi1_satir and tahmin_sutun == gemi1_sutun)\
            or (tahmin_satir == gemi2_satir and tahmin_sutun == gemi2_sutun)\
            or (tahmin_satir == gemi3_satir and tahmin_sutun == gemi3_sutun)\
            or (tahmin_satir == gemi4_satir and tahmin_sutun == gemi4_sutun)\
            or (tahmin_satir == gemi5_satir and tahmin_sutun == gemi5_sutun)\
            or (tahmin_satir == gemi6_satir and tahmin_sutun == gemi6_sutun)\
            or (tahmin_satir == gemi7_satir and tahmin_sutun == gemi7_sutun)\
            or (tahmin_satir == gemi8_satir and tahmin_sutun == gemi8_sutun)):
            print("Tebrikler!!! Tam İsabet!!!")
            tahta[tahmin_satir-1][tahmin_sutun-1] = "X"     #Gemiyi tutturdugumuzda'X' isareti ile tahtaya isaret koyacagiz.
            goster(tahta)
        else:
            if (tahmin_satir < 0 or tahmin_sutun < 0) or (tahmin_satir >10 or tahmin_sutun >10): #1-10 arasi tahimin belirlenebilecegi soylenmisti.
                print("Denizin dışına bos atis yapildi...\n1-10 atasi deger giriniz...")
                
            elif tahta[tahmin_satir - 1][tahmin_sutun - 1] == "X" or tahta[tahmin_satir - 1][tahmin_sutun - 1] == "-":
                print("Daha once tahmin etmistiniz...")
                goster(tahta)

            else:                                           #15 hata yapma hakki bittiginde oyun sonlandiriliyor.
                if sayac==14:
                    print("Game Over!!!")
                    quit()
                else:                                       #Hedef tutturulamadiginda '-' atis yapilan yer isaretlenir.
                    sayac+=1
                    print("Hedefi tutturamadiniz...")
                    tahta[tahmin_satir - 1][tahmin_sutun - 1] = "-"
                    goster(tahta)
                    print(15-sayac,"hakkiniz kaldi","5 saniye bekletiliyorsunuz...")    #Her hatada oyunvu 5sn. bekletilir.
                    time.sleep(5)                    
                    continue
except:
    print("Lutfen bos birakmayiniz...")

