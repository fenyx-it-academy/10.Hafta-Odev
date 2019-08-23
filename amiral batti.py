# yanina eklenemeyen kodlarin aciklamalari kodlardan hemen sonra altlarina yazildi..

from time import sleep      # ekrana zaman bekletme yerlestirecegimiz icin gomdugumuz komut..


print("""
      =============================================="
      |                                            |
      |                                            |
      |             AMIRAL BATTI OYUNU             |
      |                  V 2.3                     |
      |               HOSGELDINIZ                  |
      |                                            |
      ==============================================\n\n""")


liste = [
["  ",     "a",    "b",     "c",     "d",     "e",     "f",     "g",     "h",     "i",     "j"],
["1"," \u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001"],
["2"," \u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001"],
["3"," \u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001"],
["4"," \u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001"],
["5"," \u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001"],
["6"," \u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001"],
["7"," \u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001"],
["8"," \u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001"],
["9"," \u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001"],
["10","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001"]
]
# Liste ici liste yapmak zorunda kalindi..unicode kullanildi..


for i in liste:     #Listeyi ilk bastaki ekrana basmak icin,,
    print(*i)

liste2 = [
[" ",     "a",    "b",     "c",     "d",     "e",     "f",     "g",     "h",     "i",     "j", "\n"],
["1","\u2605","\u0001","\u2605","\u2605","\u2605","\u0001","\u0001","\u0001","\u0001","\u0001","\n"],
["2","\u2605","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\n"],
["3","\u2605","\u0001","\u0001","\u0001","\u0001","\u2605","\u2605","\u2605","\u0001","\u0001","\n"],
["4","\u2605","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u2605","\n"],
["5","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\n"],
["6","\u0001","\u0001","\u0001","\u0001","\u0001","\u2605","\u2605","\u0001","\u0001","\u2605","\n"],
["7","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\n"],
["8","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\n"],
["9","\u0001","\u0001","\u2605","\u2605","\u0001","\u0001","\u2605","\u2605","\u2605","\u2605","\n"],
["10","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001","\u0001"]
]

print("\n")     # Guzel Gorunsun diye..



genelsayac = 0      # 15 deneme hakki sona erdiginde bilelim diye konulan sayac

kazanmasayac=0      # toplam gemiler bulundugunda bilelim diye konulan sayac

def engelleme(a,b):         # daha once acilan veya denenen kareye hamle yapilmasini englellemek icin yazildi..
    z = liste[0].index(sutunnharfi)
    if liste[satirnuamrasi-1][z]!='\u0001' :
        print('Lutfen Bos Bir Alana Oynayiniz!')


def goster(listeadi):       # hamlelerden sonra goruntuyu basmak icin yapildi..
    for i in listeadi:      # Liste ici liste oldugu icin for kullandik..
        print(*i)

def hamle(satir,sutun):             # yapilan hamlenin satir ve sutuna gore kesistigi kareyi bulan fonksiyon
    z= liste[0].index(sutunnharfi)

    global genelsayac           # sayaclari disardan aliyoruz islemek icin,,
    global kazanmasayac


    if liste2[satirnuamrasi][z]=="\u0001":      # yapilan hamle isabet etmediyse sayaci bir artir ve denenen
        genelsayac+=1                           #kareyi X ile isaretle iki listede de..sonra ekrani bas..
        liste[satirnuamrasi][z]="X"
        liste2[satirnuamrasi][z] = "X"
        print("Tekrar Deneyiniz! Kalan Deneme Hakkiniz :",15-genelsayac)
        goster(liste)
        sleep(1)                            # ekrani basitiktan sonra 5 sn bekle..
    

    elif liste2[satirnuamrasi][z]=="\u2605":                    # Hamle dogru ise listelerde geminin parcasini goster
        print("Geminin bir parcasini buldunuz! Devam ediniz")   # sayaci 1 artir ve yeni ekrani bas ve 5 sn sonra
        liste[satirnuamrasi][z]="\u2605"                        #donguye geri don..
        liste2[satirnuamrasi][z] = "X"
        kazanmasayac+=1
        goster(liste)
        sleep(5)

    else:
        engelleme(sutunnharfi,satirnuamrasi)    # zaten yukaridaki secenekler olmuyorsa geriye ayni kareye hamle yapma
                                                # kaliyor egger boyle ise fonksiyonu calistir ve engelle..
    goster(liste)


while True:
    satirnuamrasi = int(input("Lutfen Satir numarasini Giriniz : "))
    sutunnharfi = input("Lutfen Sutun harfini Giriniz : ")

    hamle(satirnuamrasi,sutunnharfi)    # yukaridaki fonksiyona gore hamleni yap.

    if kazanmasayac==20:                        # gemizlerin toplam kapladigi yer 20 karedir.bu yuzden 20 kere
        "Tebrikler! Butun Gemileri Buldunuz !"  #dogru hamle olursa basari ver
        input("Oyundan Cikmak Icin q ya basiniz, Yeni bir oyuna "
              "girmek icin herhangi bir tusa basiniz : ")
        if input == "q":
            break
        else:
            continue

    if genelsayac==15:          # oyunda 15 hak verdik.bu nedenle 15 kere hatali hamle sonunda hepsi bulunmamissa bitir.
        print("Uzgunuz ! Hakkiniz KAlmadi KAYBETTINIZ")
        input("Oyundan Cikmak Icin q ya basiniz, Yeni bir oyuna "
              "girmek icin herhangi bir tusa basiniz : ")
        if input=="q":
            break
        else:
            continue

hamle(satirnuamrasi,sutunnharfi)


# Kodu yazarken satir ve sutun inputlarinin kesistigi yeri bulma ve engelleme fonsiyonu zorladi..
# UNICODE kullanilan yildiz isaretini ekrana bastiginda siralama hizalamasi biraz bozuluyor, harf girsekte
#  bozuluyor.bunu unutmazsam derste hatirlatcam,,













