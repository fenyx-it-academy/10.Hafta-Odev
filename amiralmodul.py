''' bu kod amiral batti oyununun fonksiyonlaridir '''

#tablonun her bir kutucugu ikili sayi listesinden olusuyor.tum kutucuklar tek bir liste icinde 00 01 43 56..gibi
def tabloilk():
    tbl=[]
    for i in range(10):
        for j in range(10):
            tbl.append(str(i)+str(j))

    return tbl


def yazdir(a,g):                          #bir satir ele alindiginda 00   01   02   03 ...aralari 3 bosluklu yaziyor
    for i in range(10):
        print(g[i+a], end=' '*3)
    print("\n")

def gorunen(grnn):                              #her bir satirin kutucuk numaralrini 3er boslukla yaziyor
    print('')                       #tablodan once bir satir bosluk yapar
    yazdir(0, grnn)                 #1.satir
    yazdir(10, grnn)                #2.satir
    yazdir(20, grnn)                #3.satir
    yazdir(30, grnn)
    yazdir(40, grnn)
    yazdir(50, grnn)
    yazdir(60, grnn)
    yazdir(70, grnn)
    yazdir(80, grnn)
    yazdir(90, grnn)

from amiralrandomcozum import*
#simdilik cozum alttaki gibi olsun
#cozum = ['00', '05', '06', '07', '19', '22', '29', '32', '39', '42',
#      '55', '56', '57', '70', '81', '82', '83', '84', '96', '97']

def cozumtablosu():                 #15 hakkini bitirip oyunu bitiren oyuncuya cozumu gosterir
    tson = tabloilk().copy()
    for i in cozum:                #cozum listesindeki kutukcuklari bul

        yer=int(i)                  #bu kumede sayilar str seklindeydi.integer yap
        tson[yer]="X "              #gemilerin bulundugu yeri X ile goster

    return tson

