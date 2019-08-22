

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
baslangic_zamani = time()

tablo = tabloilk().copy()
gorunen(tablo)
hak = 15
while True:

    hamle = input(''' ~hamle yapmak icin tablodan bir sayi girin
 ~cikis icin q ya basin:''')
    if hamle == "q":
        break

    elif hamle == '  ' or hamle == "X ":
        print('Tablodaki henuz acilmamis kutucuk numaralarindan secim yapiniz.')
    elif hamle not in tablo:
        print('Tablodaki henuz acilmamis kutucuk numaralarindan secim yapiniz.')
        gorunen(tablo)
    else:
        if hamle in cozum:
            konum = int(hamle)
            tablo[konum] = 'X '
            print(f'{hamle} kutusunda gemi parcasi varmi bir bakayim...')
            sleep(1)
            print("gemimin bir parcsini vurdun.")
            gorunen(tablo)
            if tablo.count('X ') == 20:
                print("...TEBRIKLER...".center(20))
                print("oyunu kazandiniz".center(20))
                break
        else:
            konum = int(hamle)
            tablo[konum] = '  '
            print(f'{hamle} kutusunda gemi parcasi varmi bir bakayim...')
            sleep(1)
            print("gemilerim hala guvende.Iskaladin")
            gorunen(tablo)
            hak -= 1
            print(f'{hak} canin kaldi.')
            if hak == 0:
                print("..Oyun Bitti..")
                print("Hic canin kalmadi")
                print("iste aradiginiz cozum:")
                gorunen(cozumtablosu())

                break





bitirme_zamani = time()
print(f"{baslangic_zamani-bitirme_zamani} sn de oyun tamamladiniz.")
