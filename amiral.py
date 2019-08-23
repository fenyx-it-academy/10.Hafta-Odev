

from amiralmodul import*
from time import*


print("...AMIRAL BATTI OYUNUNA HOSGELDINIZ...")
print("""Bu tabloda:
- 2 adet 4 birimlik, 
- 2 adet 3 birimlik, 
- 2 adet 2 birimlik ve 
- 2 adet 1 birimlik gemiler yerlestirilmistir.
Gemilerin yerlerini dogru tahmin ettiginizde X ile gosterilecek.
Bulmak icin 15 caniniz var.Kolay gelsin.""")
baslangic_zamani = time()               #oyun baslama zamanini tutar

tablo = tabloilk().copy()               #00 01 02 gibi numaralardan olusan listeyi copy
gorunen(tablo)
hak = 15                                #oyunucunun 15 hakki var
while True:


    # oyuncunun hamlesi
    hamle = input(''' ~hamle yapmak icin tablodan bir sayi girin 
 ~cikis icin q ya basin:''')

    # hamle cikis istiyorsa cikis yapar
    if hamle == "q":
        break

    # tabloda zamanla "  " ve "X " olacak.isabet eden ya da etmeyen kutular.
    elif hamle == '  ' or hamle == "X ":
        print('Tablodaki henuz acilmamis kutucuk numaralarindan secim yapiniz.') #daha onceki secimlerden tekrar yaptirmiyor

    # tabloda olmayan sayi isaret veya yazi girilirse tekrar hamle istiyor
    elif hamle not in tablo:
        print('Tablodaki henuz acilmamis kutucuk numaralarindan secim yapiniz.')
        gorunen(tablo)

    #oyuncu tabloda acilmamis kutulardan tercih yaptiginda hamle yapiyor
    else:

        #hamle cozum icinde varsa
        if hamle in cozum:
            konum = int(hamle)   #kutucuk numaralari ayni zamanda indexlerdir
            tablo[konum] = 'X '  #tabloda index yardimiyla hamle yapilan kutucugun dolu oldugunu X ile gosteriyor
            print(f'{hamle} kutusunda gemi parcasi varmi bir bakayim...')
            sleep(1)                        #1 sn tabloyu kontrol ediyormus gibi dusunup bekletiyor
            print("gemimin bir parcsini vurdun.")
            gorunen(tablo)                  #tabloyu yeni haliyle ekrana basiyor


            # toplam 20 tane gemi parcasi var.eger 20 si de bulunursa oyuncu oyunu kazandi
            if tablo.count('X ') == 20:
                print("...TEBRIKLER...".center(20))
                print("oyunu kazandiniz".center(20))
                break

        #sartlari saglayan hamle yapildi.fakat cozum listesinde olmayan kutu secildi
        else:
            konum = int(hamle)                            #tablodaki index bulunur
            tablo[konum] = '  '                           #tabloda boslik ile gosterilir
            print(f'{hamle} kutusunda gemi parcasi varmi bir bakayim...')
            sleep(1)                                     #1 sn tabloyu kontrol ediyormus gibi dusunup bekletiyor
            print("gemilerim hala guvende.Iskaladin")
            gorunen(tablo)                                 #tabloyu yeni haliyle ekrana basiyor
            hak -= 1                                       #hakkindan bir tane dusuyor
            print(f'{hak} canin kaldi.')

            # 15 hakkin tamamini kullanmissa
            if hak == 0:
                print("..Oyun Bitti..")
                print("Hic canin kalmadi")
                print("iste aradiginiz cozum:")
                gorunen(cozumtablosu())             #cozum tablosunu ekrana printler

                break





bitirme_zamani = time()
print(f"{baslangic_zamani-bitirme_zamani} sn de oyun tamamladiniz.")
