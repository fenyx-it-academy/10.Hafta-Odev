#    ODEV: AMIRAL BATTI

#    Deniz olarak varsayacagimiz 10x10'luk bir tablo olusturun
#    (X-O-X oyununa benzer). Bu tabloya 2 adet 4 birimlik,
#    2 adet 3 birimlik, 2 adet 2 birimlik ve 2 adet 1 birimlik
#    gemiler yerlestirin. Yerlestirdiginiz gemileri kullanici
#    gormeyecek. Kullanicidan tablo uzerindeki herhangi bir
#    noktaya hamlede bulunmasini isteyin. Kullanicinin hamlesi
#    gemilerin herhangi bir noktasina isabet ederse kullaniciya
#    tablo uzerinde bunu gosterin. Ayni sekilde bosa atis
#    yaptiginda da kullaniciya tablo uzerinde bunu gosterin
#    ve kullanicinin 5 sn boyunca hamle yapmasini engelleyin.
#    Kullanici daha once hamle yapmis oldugu bir noktaya tekrar
#    hamlede bulunursa bunu engelleyin. Kullaniciya toplamda
#    15 yanlis hamle hakki verin. Kullanici tum gemileri
#    vurdugunda oyunu bitirin.
#
#    Oyunu mumkun oldugunca fonksiyonlar kullanarak yapmanizi istiyoruz.
#
#    BONUS(ISTEGE BAGLI): Yukaridaki versiyonda gemiler sabit.
#    Oyunu her actigimizda gemilerin yeri degismiyor. Isteyenler
#    gemilerin random yerlestirildigi bir versiyonunu yapabilir.

## zamanlamayi calistirmak icin time fonksiyonunu import ediyoruz
from time import sleep
## gemileri farkli duzende yerlestirmek icin random import ediyoruz
import random

w =   {'a1':'[x]','a2':'[ ]','a3':'[ ]','a4':'[ ]','a5':'[ ]','a6':'[ ]','a7':'[ ]','a8':'[ ]','a9':'[ ]','a10':'[ ]',
       'b1':'[ ]','b2':'[ ]','b3':'[ ]','b4':'[ ]','b5':'[x]','b6':'[x]','b7':'[x]','b8':'[x]','b9':'[ ]','b10':'[ ]',
       'c1':'[ ]','c2':'[ ]','c3':'[ ]','c4':'[ ]','c5':'[ ]','c6':'[ ]','c7':'[ ]','c8':'[ ]','c9':'[ ]','c10':'[ ]',
       'd1':'[ ]','d2':'[x]','d3':'[ ]','d4':'[ ]','d5':'[ ]','d6':'[ ]','d7':'[ ]','d8':'[ ]','d9':'[ ]','d10':'[ ]',
       'e1':'[ ]','e2':'[x]','e3':'[ ]','e4':'[ ]','e5':'[ ]','e6':'[ ]','e7':'[ ]','e8':'[ ]','e9':'[x]','e10':'[ ]',
       'f1':'[ ]','f2':'[x]','f3':'[ ]','f4':'[ ]','f5':'[ ]','f6':'[ ]','f7':'[ ]','f8':'[ ]','f9':'[x]','f10':'[ ]',
       'g1':'[ ]','g2':'[x]','g3':'[ ]','g4':'[x]','g5':'[x]','g6':'[x]','g7':'[ ]','g8':'[ ]','g9':'[x]','g10':'[ ]',
       'h1':'[ ]','h2':'[ ]','h3':'[ ]','h4':'[ ]','h5':'[ ]','h6':'[ ]','h7':'[ ]','h8':'[ ]','h9':'[ ]','h10':'[ ]',
       'k1':'[x]','k2':'[x]','k3':'[ ]','k4':'[ ]','k5':'[ ]','k6':'[ ]','k7':'[ ]','k8':'[ ]','k9':'[ ]','k10':'[x]',
       'l1':'[ ]','l2':'[ ]','l3':'[ ]','l4':'[ ]','l5':'[ ]','l6':'[ ]','l7':'[x]','l8':'[x]','l9':'[ ]','l10':'[ ]',}

y =   {'a1':'[ ]','a2':'[ ]','a3':'[x]','a4':'[x]','a5':'[x]','a6':'[x]','a7':'[ ]','a8':'[ ]','a9':'[ ]','a10':'[ ]',
       'b1':'[x]','b2':'[ ]','b3':'[ ]','b4':'[ ]','b5':'[ ]','b6':'[ ]','b7':'[ ]','b8':'[ ]','b9':'[x]','b10':'[x]',
       'c1':'[ ]','c2':'[ ]','c3':'[ ]','c4':'[ ]','c5':'[ ]','c6':'[ ]','c7':'[ ]','c8':'[ ]','c9':'[ ]','c10':'[ ]',
       'd1':'[ ]','d2':'[ ]','d3':'[ ]','d4':'[ ]','d5':'[ ]','d6':'[ ]','d7':'[ ]','d8':'[x]','d9':'[ ]','d10':'[ ]',
       'e1':'[ ]','e2':'[x]','e3':'[ ]','e4':'[ ]','e5':'[ ]','e6':'[ ]','e7':'[ ]','e8':'[x]','e9':'[ ]','e10':'[ ]',
       'f1':'[ ]','f2':'[x]','f3':'[ ]','f4':'[ ]','f5':'[ ]','f6':'[ ]','f7':'[ ]','f8':'[x]','f9':'[ ]','f10':'[x]',
       'g1':'[ ]','g2':'[ ]','g3':'[ ]','g4':'[ ]','g5':'[ ]','g6':'[ ]','g7':'[ ]','g8':'[x]','g9':'[ ]','g10':'[ ]',
       'h1':'[ ]','h2':'[ ]','h3':'[ ]','h4':'[ ]','h5':'[ ]','h6':'[ ]','h7':'[ ]','h8':'[ ]','h9':'[ ]','h10':'[ ]',
       'k1':'[ ]','k2':'[x]','k3':'[x]','k4':'[x]','k5':'[ ]','k6':'[ ]','k7':'[ ]','k8':'[ ]','k9':'[ ]','k10':'[ ]',
       'l1':'[ ]','l2':'[ ]','l3':'[ ]','l4':'[ ]','l5':'[ ]','l6':'[ ]','l7':'[x]','l8':'[x]','l9':'[x]','l10':'[ ]',}

z =   {'a1':'[ ]','a2':'[ ]','a3':'[ ]','a4':'[ ]','a5':'[ ]','a6':'[ ]','a7':'[x]','a8':'[ ]','a9':'[ ]','a10':'[ ]',
       'b1':'[ ]','b2':'[x]','b3':'[x]','b4':'[x]','b5':'[x]','b6':'[ ]','b7':'[x]','b8':'[ ]','b9':'[ ]','b10':'[x]',
       'c1':'[ ]','c2':'[ ]','c3':'[ ]','c4':'[ ]','c5':'[ ]','c6':'[ ]','c7':'[x]','c8':'[ ]','c9':'[ ]','c10':'[ ]',
       'd1':'[ ]','d2':'[ ]','d3':'[ ]','d4':'[ ]','d5':'[ ]','d6':'[ ]','d7':'[x]','d8':'[ ]','d9':'[ ]','d10':'[ ]',
       'e1':'[ ]','e2':'[ ]','e3':'[ ]','e4':'[ ]','e5':'[ ]','e6':'[ ]','e7':'[ ]','e8':'[ ]','e9':'[x]','e10':'[ ]',
       'f1':'[x]','f2':'[x]','f3':'[x]','f4':'[ ]','f5':'[ ]','f6':'[ ]','f7':'[ ]','f8':'[ ]','f9':'[x]','f10':'[ ]',
       'g1':'[ ]','g2':'[ ]','g3':'[ ]','g4':'[ ]','g5':'[ ]','g6':'[ ]','g7':'[ ]','g8':'[ ]','g9':'[x]','g10':'[x]',
       'h1':'[ ]','h2':'[ ]','h3':'[x]','h4':'[ ]','h5':'[ ]','h6':'[ ]','h7':'[ ]','h8':'[ ]','h9':'[ ]','h10':'[x]',
       'k1':'[ ]','k2':'[ ]','k3':'[x]','k4':'[ ]','k5':'[ ]','k6':'[ ]','k7':'[ ]','k8':'[ ]','k9':'[ ]','k10':'[ ]',
       'l1':'[ ]','l2':'[ ]','l3':'[ ]','l4':'[ ]','l5':'[ ]','l6':'[ ]','l7':'[ ]','l8':'[x]','l9':'[ ]','l10':'[ ]',}


q =   {'a1':'[ ]','a2':'[ ]','a3':'[ ]','a4':'[ ]','a5':'[ ]','a6':'[ ]','a7':'[ ]','a8':'[ ]','a9':'[ ]','a10':'[ ]',
       'b1':'[ ]','b2':'[ ]','b3':'[ ]','b4':'[ ]','b5':'[ ]','b6':'[ ]','b7':'[ ]','b8':'[ ]','b9':'[ ]','b10':'[ ]',
       'c1':'[ ]','c2':'[ ]','c3':'[ ]','c4':'[ ]','c5':'[ ]','c6':'[ ]','c7':'[ ]','c8':'[ ]','c9':'[ ]','c10':'[ ]',
       'd1':'[ ]','d2':'[ ]','d3':'[ ]','d4':'[ ]','d5':'[ ]','d6':'[ ]','d7':'[ ]','d8':'[ ]','d9':'[ ]','d10':'[ ]',
       'e1':'[ ]','e2':'[ ]','e3':'[ ]','e4':'[ ]','e5':'[ ]','e6':'[ ]','e7':'[ ]','e8':'[ ]','e9':'[ ]','e10':'[ ]',
       'f1':'[ ]','f2':'[ ]','f3':'[ ]','f4':'[ ]','f5':'[ ]','f6':'[ ]','f7':'[ ]','f8':'[ ]','f9':'[ ]','f10':'[ ]',
       'g1':'[ ]','g2':'[ ]','g3':'[ ]','g4':'[ ]','g5':'[ ]','g6':'[ ]','g7':'[ ]','g8':'[ ]','g9':'[ ]','g10':'[ ]',
       'h1':'[ ]','h2':'[ ]','h3':'[ ]','h4':'[ ]','h5':'[ ]','h6':'[ ]','h7':'[ ]','h8':'[ ]','h9':'[ ]','h10':'[ ]',
       'k1':'[ ]','k2':'[ ]','k3':'[ ]','k4':'[ ]','k5':'[ ]','k6':'[ ]','k7':'[ ]','k8':'[ ]','k9':'[ ]','k10':'[ ]',
       'l1':'[ ]','l2':'[ ]','l3':'[ ]','l4':'[ ]','l5':'[ ]','l6':'[ ]','l7':'[ ]','l8':'[ ]','l9':'[ ]','l10':'[ ]',}
print("""Asagidaki tablodan uygun alani secerek yer ismini belirtiyorsunuz,
dogru hamleler 'x' ile yanlis hamleler '-' ile isaretlenecektir.
Hazirsaniz baslayalim; \n""")
sleep(5)
print("""Gemilerin yerlestirildigi tablomuz;
1   2   3   4   5   6   7   8   9   10 
a [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
b [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
c [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
d [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
e [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
f [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
g [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
h [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
k [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
l [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n""")
sleep(5)
print("""Gemiler:
Amiral Gemisi : X X X X    (4 lu- 2 adet)
Kruvazor      : X X X      (3 lu- 2 adet)
Muhrip        : X X        (2 lu- 2 adet)
Denizalti     : X          (1 li- 2 adet) \n""")
sleep(5)
amr1=0
amr2=0
kru1=0
kru2=0
muh1=0
muh2=0
sayac=0
basarisiz=0
zorluk=int(input("Oyunun zorluk derecesini seciniz(1:zor, 2:normal veya 3:kolay) : "))
if zorluk==1:
    print("Zorluk derecesi 1, Oyuna basliyoruz..")
    while basarisiz<15:
        kul=input("Tablo uzerindeki herhangi bir noktaya hamlede bulunun :...")
        if kul not in w:
            print("\n","Lutfen gecerli bir tahmin yapiniz!!","\n")
            pass
        if kul in w and w[kul]=='[x]':
            if q[kul] == '[x]':
                print("\n","Bu tahmini kullanmistiniz!!","\n")
                sayac += 1
                if sayac==19:
                    print("""\n--------------------------------------------


         .....K A Z A N D I N I Z!!.....

                    
    --------------------------------------------

    """)
                    break
            else:
                q[kul]='[x]'
                sleep(2)
                
            if kul=='b5' or kul=="b6" or kul=="b7" or kul=="b8":
                amr1+=1
                print("\n","Amiral1'in",amr1,". parcasini vurdunuz","\n")
            if kul=='d2' or kul=="e2" or kul=="f2" or kul=="g2":
                amr2+=1
                print("\n","Amiral2'nin",amr2,". parcasini vurdunuz","\n")
            if kul=='g4' or kul=="g5" or kul=="g6":
                kru1+=1
                print("\n","Kruvazor1'in",kru1,". parcasini vurdunuz","\n")
            if kul=='e9' or kul=="f9" or kul=="g9":
                kru2+=1
                print("\n","Kruvazor2'nin",kru2,". parcasini vurdunuz","\n")
            if kul=='l7' or kul=="l8":
                muh1+=1
                print("\n","Muhrip1'in",muh1,". parcasini vurdunuz","\n")
            if kul=='k1' or kul=="k2":
                muh2+=1
                print("\n","Muhrip2'nin",muh2,". parcasini vurdunuz","\n")
            if kul=='a1':
                print("\n","Denizalti vurdunuz","\n")
            if kul=='k10':
                print("\n","Denizalti vurdunuz","\n")
        else:
            basarisiz+=1
            q[kul]='[-]'
            print("\n",basarisiz,". basarisiz hamleniz ","\n")
            sleep(2)
        
        
        print(              '   1 ',' 2 ' ,' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ',' 10 ' )
        print(         'a', q['a1'],q['a2'],q['a3'],q['a4'],q['a5'],q['a6'],q['a7'],q['a8'],q['a9'],q['a10'])
        print(         'b', q['b1'],q['b2'],q['b3'],q['b4'],q['b5'],q['b6'],q['b7'],q['b8'],q['b9'],q['b10'])
        print(         'c', q['c1'],q['c2'],q['c3'],q['c4'],q['c5'],q['c6'],q['c7'],q['c8'],q['c9'],q['c10'])
        print(         'd', q['d1'],q['d2'],q['d3'],q['d4'],q['d5'],q['d6'],q['d7'],q['d8'],q['d9'],q['d10'])
        print(         'e', q['e1'],q['e2'],q['e3'],q['e4'],q['e5'],q['e6'],q['e7'],q['e8'],q['e9'],q['e10'])
        print(         'f', q['f1'],q['f2'],q['f3'],q['f4'],q['f5'],q['f6'],q['f7'],q['f8'],q['f9'],q['f10'])
        print(         'g', q['g1'],q['g2'],q['g3'],q['g4'],q['g5'],q['g6'],q['g7'],q['g8'],q['g9'],q['g10'])
        print(         'h', q['h1'],q['h2'],q['h3'],q['h4'],q['h5'],q['h6'],q['h7'],q['h8'],q['h9'],q['h10'])
        print(         'k', q['k1'],q['k2'],q['k3'],q['k4'],q['k5'],q['k6'],q['k7'],q['k8'],q['k9'],q['k10'])
        print(         'l', q['l1'],q['l2'],q['l3'],q['l4'],q['l5'],q['l6'],q['l7'],q['l8'],q['l9'],q['l10'])
        print("\n")
        if basarisiz==15:
            print("""\n--------------------------------------------


         .....K A Y B E T T I N I Z!!.....

                    
    --------------------------------------------

    """)
            
if zorluk==2:
    print("Zorluk derecesi 2, Oyuna basliyoruz..")
    while basarisiz<15:
        kul=input("Tablo uzerindeki herhangi bir noktaya hamlede bulunun :...")
        if kul not in y:
            print("\n","Lutfen gecerli bir tahmin yapiniz!!","\n")
            pass
        if kul in y and y[kul]=='[x]':
            if q[kul] == '[x]':
                print("\n","Bu tahmini kullanmistiniz!!","\n")
                sayac += 1
                if sayac==19:
                    print("""\n--------------------------------------------


         .....K A Z A N D I N I Z!!.....

                    
    --------------------------------------------

    """)
                    break
            else:
                q[kul]='[x]'
                sleep(2)
                
            if kul=='a3' or kul=="a4" or kul=="a5" or kul=="a6":
                amr1+=1
                print("\n","Amiral1'in",amr1,". parcasini vurdunuz","\n")
            if kul=='d8' or kul=="e8" or kul=="f8" or kul=="g8":
                amr2+=1
                print("\n","Amiral2'nin",amr2,". parcasini vurdunuz","\n")
            if kul=='l7' or kul=="l8" or kul=="l9":
                kru1+=1
                print("\n","Kruvazor1'in",kru1,". parcasini vurdunuz","\n")
            if kul=='k2' or kul=="k3" or kul=="k4":
                kru2+=1
                print("\n","Kruvazor2'nin",kru2,". parcasini vurdunuz","\n")
            if kul=='b9' or kul=="b10":
                muh1+=1
                print("\n","Muhrip1'in",muh1,". parcasini vurdunuz","\n")
            if kul=='e2' or kul=="f2":
                muh2+=1
                print("\n","Muhrip2'nin",muh2,". parcasini vurdunuz","\n")
            if kul=='f10':
                print("\n","Denizalti vurdunuz","\n")
            if kul=='b1':
                print("\n","Denizalti vurdunuz","\n")
        else:
            basarisiz+=1
            q[kul]='[-]'
            print("\n",basarisiz,". basarisiz hamleniz ","\n")
            sleep(2)
        
        
        print(              '   1 ',' 2 ' ,' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ',' 10 ' )
        print(         'a', q['a1'],q['a2'],q['a3'],q['a4'],q['a5'],q['a6'],q['a7'],q['a8'],q['a9'],q['a10'])
        print(         'b', q['b1'],q['b2'],q['b3'],q['b4'],q['b5'],q['b6'],q['b7'],q['b8'],q['b9'],q['b10'])
        print(         'c', q['c1'],q['c2'],q['c3'],q['c4'],q['c5'],q['c6'],q['c7'],q['c8'],q['c9'],q['c10'])
        print(         'd', q['d1'],q['d2'],q['d3'],q['d4'],q['d5'],q['d6'],q['d7'],q['d8'],q['d9'],q['d10'])
        print(         'e', q['e1'],q['e2'],q['e3'],q['e4'],q['e5'],q['e6'],q['e7'],q['e8'],q['e9'],q['e10'])
        print(         'f', q['f1'],q['f2'],q['f3'],q['f4'],q['f5'],q['f6'],q['f7'],q['f8'],q['f9'],q['f10'])
        print(         'g', q['g1'],q['g2'],q['g3'],q['g4'],q['g5'],q['g6'],q['g7'],q['g8'],q['g9'],q['g10'])
        print(         'h', q['h1'],q['h2'],q['h3'],q['h4'],q['h5'],q['h6'],q['h7'],q['h8'],q['h9'],q['h10'])
        print(         'k', q['k1'],q['k2'],q['k3'],q['k4'],q['k5'],q['k6'],q['k7'],q['k8'],q['k9'],q['k10'])
        print(         'l', q['l1'],q['l2'],q['l3'],q['l4'],q['l5'],q['l6'],q['l7'],q['l8'],q['l9'],q['l10'])
        print("\n")
        if basarisiz==15:
            print("""\n--------------------------------------------


         .....K A Y B E T T I N I Z!!.....

                    
    --------------------------------------------

    """)

if zorluk==3:
    print("Zorluk derecesi 3, Oyuna basliyoruz..")
    while basarisiz<15:
        kul=input("Tablo uzerindeki herhangi bir noktaya hamlede bulunun :...")
        if kul not in z:
            print("\n","Lutfen gecerli bir tahmin yapiniz!!","\n")
            pass
        if kul in z and z[kul]=='[x]':
            if q[kul] == '[x]':
                print("\n","Bu tahmini kullanmistiniz!!","\n")
                sayac += 1
                if sayac==19:
                    print("""\n--------------------------------------------


         .....K A Z A N D I N I Z!!.....

                    
    --------------------------------------------

    """)
                    break
            else:
                q[kul]='[x]'
                sleep(2)
                
            if kul=='a7' or kul=="b7" or kul=="c7" or kul=="d7":
                amr1+=1
                print("\n","Amiral1'in",amr1,". parcasini vurdunuz","\n")
            if kul=='b2' or kul=="b3" or kul=="b4" or kul=="b5":
                amr2+=1
                print("\n","Amiral2'nin",amr2,". parcasini vurdunuz","\n")
            if kul=='f1' or kul=="f2" or kul=="f3":
                kru1+=1
                print("\n","Kruvazor1'in",kru1,". parcasini vurdunuz","\n")
            if kul=='e9' or kul=="f9" or kul=="g9":
                kru2+=1
                print("\n","Kruvazor2'nin",kru2,". parcasini vurdunuz","\n")
            if kul=='g10' or kul=="h10":
                muh1+=1
                print("\n","Muhrip1'in",muh1,". parcasini vurdunuz","\n")
            if kul=='h3' or kul=="k3":
                muh2+=1
                print("\n","Muhrip2'nin",muh2,". parcasini vurdunuz","\n")
            if kul=='f1':
                print("\n","Denizalti vurdunuz","\n")
            if kul=='b10':
                print("\n","Denizalti vurdunuz","\n")
        else:
            basarisiz+=1
            q[kul]='[-]'
            print("\n",basarisiz,". basarisiz hamleniz ","\n")
            sleep(2)
        
        
        print(              '   1 ',' 2 ' ,' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ',' 10 ' )
        print(         'a', q['a1'],q['a2'],q['a3'],q['a4'],q['a5'],q['a6'],q['a7'],q['a8'],q['a9'],q['a10'])
        print(         'b', q['b1'],q['b2'],q['b3'],q['b4'],q['b5'],q['b6'],q['b7'],q['b8'],q['b9'],q['b10'])
        print(         'c', q['c1'],q['c2'],q['c3'],q['c4'],q['c5'],q['c6'],q['c7'],q['c8'],q['c9'],q['c10'])
        print(         'd', q['d1'],q['d2'],q['d3'],q['d4'],q['d5'],q['d6'],q['d7'],q['d8'],q['d9'],q['d10'])
        print(         'e', q['e1'],q['e2'],q['e3'],q['e4'],q['e5'],q['e6'],q['e7'],q['e8'],q['e9'],q['e10'])
        print(         'f', q['f1'],q['f2'],q['f3'],q['f4'],q['f5'],q['f6'],q['f7'],q['f8'],q['f9'],q['f10'])
        print(         'g', q['g1'],q['g2'],q['g3'],q['g4'],q['g5'],q['g6'],q['g7'],q['g8'],q['g9'],q['g10'])
        print(         'h', q['h1'],q['h2'],q['h3'],q['h4'],q['h5'],q['h6'],q['h7'],q['h8'],q['h9'],q['h10'])
        print(         'k', q['k1'],q['k2'],q['k3'],q['k4'],q['k5'],q['k6'],q['k7'],q['k8'],q['k9'],q['k10'])
        print(         'l', q['l1'],q['l2'],q['l3'],q['l4'],q['l5'],q['l6'],q['l7'],q['l8'],q['l9'],q['l10'])
        print("\n")
        if basarisiz==15:
            print("""\n--------------------------------------------


         .....K A Y B E T T I N I Z!!.....

                    
    --------------------------------------------

    """)





           
            

