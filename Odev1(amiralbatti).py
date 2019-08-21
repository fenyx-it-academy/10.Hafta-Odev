#ODEV: AMIRAL BATTI
#Deniz olarak varsayacagimiz 10x10'luk bir tablo olusturun (X-O-X oyununa benzer). Bu tabloya 2 adet 4 birimlik, ' \
#2 adet 3 birimlik, 2 adet 2 birimlik ve 2 adet 1 birimlik gemiler yerlestirin. Yerlestirdiginiz gemileri kullanici
#gormeyecek. Kullanicidan tablo uzerindeki herhangi bir noktaya hamlede bulunmasini isteyin. Kullanicinin hamlesi
#gemilerin herhangi bir noktasina isabet ederse kullaniciya tablo uzerinde bunu gosterin. Ayni sekilde bosa atis
#yaptiginda da kullaniciya tablo uzerinde bunu gosterin ve kullanicinin 5 sn boyunca hamle yapmasini engelleyin.
#Kullanici daha once hamle yapmis oldugu bir noktaya tekrar hamlede bulunursa bunu engelleyin. Kullaniciya toplamda
#15 yanlis hamle hakki verin. Kullanici tum gemileri vurdugunda oyunu bitirin.
#Oyunu mumkun oldugunca fonksiyonlar kullanarak yapmanizi istiyoruz.
#BONUS(ISTEGE BAGLI): Yukaridaki versiyonda gemiler sabit. Oyunu her actigimizda gemilerin yeri degismiyor.
#Isteyenler gemilerin random yerlestirildigi bir versiyonunu yapabilir.


print("""*********** AMIRAL BATTI************
Oyun Kurallari:
-oyunda toplam 8 adet gemi vardir.
-2 adet 4 birimlik, 2 adet 3 birimlik, 2 adet 2 birimlik ve 2 adet 1 birimlik.
-toplam 15 hatali yer secme hakkiniz vardir.
-atis yapilacak konum secerken once satir icin 0 ile 9 arasinda sonra sutun icin 0 ile 9 arasinda bir secim yapiniz.
-tabloda 'X' karavana atisi, '#' tamamiyla batmis gemiyi, 'O' bir birimi vurulmus gemiyi gosterir. 
oyun basliyor basarilar...""",end='\n'*2)

from time import sleep				
sleep(2)
deniz=[]												
for i in range(10):										
    deniz.append(["-"]*10)							# oyun icin gerekli 10'a 10'luk tablo olusturuldu.
def gemibatti():
    print("Bir gemi batti.")
def print_deniz(deniz):
    for i in deniz:
        print("\t".expandtabs(40),"  ".join(i))		# tabloyu istedigimiz zaman cikti almak icin tablo ciktisi veren fonksiyon yazildi.
import random as ran   								# bu bloklarda gemiler rastgele tabloya yerlestirmek icin bazi degerler degiskenler atandi.
gemi1ax=ran.randint(0,0)
gemi1ay=ran.randint(5,9)
gemi1bx=ran.randint(5,5)
gemi1by=ran.randint(0,4)
gemi2ax=ran.randint(8,9)
gemi2ay=ran.randint(5,8)
gemi2bx=ran.randint(0,3)
gemi2by=ran.randint(0,1)
gemi3ax=ran.randint(5,7)
gemi3ay=ran.randint(5,7)
gemi3bx=ran.randint(0,2)
gemi3by=ran.randint(2,3)
gemi4ax=ran.randint(6,9)
gemi4ay=ran.randint(0,1)
gemi4bx=ran.randint(1,1)
gemi4by=ran.randint(5,9)
# bu bolumde gemilerin konumlari belirlendi.							
gemiler_konum=[[gemi1ax,gemi1ay],[gemi1bx,gemi1by],[gemi2ax,gemi2ay],[gemi2ax,gemi2ay+1],[gemi2bx,gemi2by],
               [gemi2bx+1,gemi2by],[gemi3ax,gemi3ay],[gemi3ax,gemi3ay+1],[gemi3ax,gemi3ay+2],[gemi3bx,gemi3by],
               [gemi3bx+1,gemi3by],[gemi3bx+2,gemi3by],[gemi4ax,gemi4ay],[gemi4ax,gemi4ay+1],
               [gemi4ax,gemi4ay+2],[gemi4ax,gemi4ay+3],[gemi4bx,gemi4by],[gemi4bx+1,gemi4by],
               [gemi4bx+2,gemi4by],[gemi4bx+3,gemi4by]] 
print(gemiler_konum)
tahmin_sayisi=15
print("Toplam karavana atis sayiniz:",tahmin_sayisi)
print_deniz(deniz)
print("_" * 75)
while True:
    try:																					   #try ile hatalar engellendi.
        satir=int(input("Lutfen 0(dahil) ile 9(dahil) araliginda bir sayi giriniz(Satir):"))   # kullanicidan konum tahmini istendi.
        sutun=int(input("Lutfen 0(dahil) ile 9(dahil) araliginda bir sayi giriniz(Sutun):"))
        if 0>sutun or sutun>9 or 0>satir or satir>9:										   # if blogunda range disi secimler engellendi.
            print("Lutfen verilen deger araliginda bir giris yapiniz!!!",end="\n"*2)
            sleep(2)
            continue
    except:
        print("Lutfen girisinizi kontrol ediniz!!!",end="\n"*2)
        continue
    if deniz[satir][sutun]=="X" or deniz[satir][sutun]=='O':							# ayni yere atis yapilmasi engellendi.
        print("Buraya zaten atis yaptiniz! Lutfen yeni bir konum seciniz!",end='\n'*2)
        continue
    if [satir,sutun] in gemiler_konum:							# bu if blogunda gemi vuruldugunda yapilacaklar yazildi.
        print("Bravo!")
        deniz[satir][sutun]="O"
        gemiler_konum.remove([satir,sutun])
        if deniz[gemi1ax][gemi1ay] == "O":						# bu bolumde gemilerin butun birimleri vuruldugunda geminin battigi soylendi.
            gemibatti()
            deniz[gemi1ax][gemi1ay] = "#"
        elif deniz[gemi1bx][gemi1by] == "O":
            gemibatti()
            deniz[gemi1bx][gemi1by] = "#"
        elif deniz[gemi2ax][gemi2ay] == "O" and deniz[gemi2ax][gemi2ay + 1] == "O":
            gemibatti()
            deniz[gemi2ax][gemi2ay] = "#"
            deniz[gemi2ax][gemi2ay + 1] = "#"
        elif deniz[gemi2bx][gemi2by] == "O" and deniz[gemi2bx + 1][gemi2by] == "O":
            gemibatti()
            deniz[gemi2bx][gemi2by] = "#"
            deniz[gemi2bx + 1][gemi2by] = "#"
        elif deniz[gemi3ax][gemi3ay] == "O" and deniz[gemi3ax][gemi3ay + 1] == "O" and deniz[gemi3ax][gemi3ay + 2] == "O":
            gemibatti()
            deniz[gemi3ax][gemi3ay] = "#"
            deniz[gemi3ax][gemi3ay + 1] = "#"
            deniz[gemi3ax][gemi3ay + 2] = "#"
        elif deniz[gemi3bx][gemi3by] == "O" and deniz[gemi3bx + 1][gemi3by] == "O" and deniz[gemi3bx + 2][gemi3by] == "O":
            gemibatti()
            deniz[gemi3bx][gemi3by] = "#"
            deniz[gemi3bx + 1][gemi3by] = "#"
            deniz[gemi3bx + 2][gemi3by] = "#"
        elif deniz[gemi4ax][gemi4ay] == "O" and deniz[gemi4ax][gemi4ay + 1] == "O" \
                and deniz[gemi4ax][gemi4ay + 2] == "O" and deniz[gemi4ax][gemi4ay + 3] == "O":
            gemibatti()
            deniz[gemi4ax][gemi4ay] = "#"
            deniz[gemi4ax][gemi4ay + 1] = "#"
            deniz[gemi4ax][gemi4ay + 2] = "#"
            deniz[gemi4ax][gemi4ay + 3] = "#"
        elif deniz[gemi4bx][gemi4by] == "O" and deniz[gemi4bx+1][gemi4by] == "O" \
                and deniz[gemi4bx+2][gemi4by] == "O" and deniz[gemi4bx+3][gemi4by] == "O":
            gemibatti()
            deniz[gemi4bx][gemi4by] = "#"
            deniz[gemi4bx + 1][gemi4by] = "#"
            deniz[gemi4bx + 2][gemi4by] = "#"
            deniz[gemi4bx + 3][gemi4by] = "#"
        print_deniz(deniz)
        print("_" * 75)
    else:															# karavana atis yapildiginda borda X yazdirildi.
        deniz[satir][sutun]="X"
        tahmin_sayisi -= 1
        print("Karavana! Kalan atis sayiniz:",tahmin_sayisi)
        print_deniz(deniz)
        print("_" * 75)
        sleep(0)
    if gemiler_konum==[]:											# gemiler konum tamamen bos oldugunda tum gemilerin battigi yazdirildi.
        print("******TEBRIKLER******","\n","Butun gemileri batirdiniz.")
        break
    if tahmin_sayisi==0:											# tahmin sayisi 0 oldugunda oyun bitirildi.
        print("Ne yazikki atis hakkiniz bitmistir, Oyun sona erdi.")
        deniz[gemi1ax][gemi1ay]="O"                                 # oyun bitiminde gemilerin yerini gostermek icin.
        deniz[gemi1bx][gemi1by]="O"
        deniz[gemi2ax][gemi2ay]="O"
        deniz[gemi2ax][gemi2ay + 1]="O"
        deniz[gemi2bx][gemi2by]="O"
        deniz[gemi2bx + 1][gemi2by]="O"
        deniz[gemi3ax][gemi3ay]="O"
        deniz[gemi3ax][gemi3ay + 1]="O"
        deniz[gemi3ax][gemi3ay + 2]="O"
        deniz[gemi3bx][gemi3by]="O"
        deniz[gemi3bx + 1][gemi3by]="O"
        deniz[gemi3bx + 2][gemi3by]="O"
        deniz[gemi4ax][gemi4ay]="O"
        deniz[gemi4ax][gemi4ay + 1]="O"
        deniz[gemi4ax][gemi4ay + 2]="O"
        deniz[gemi4ax][gemi4ay + 3]="O"
        deniz[gemi4bx][gemi4by]="O"
        deniz[gemi4bx + 1][gemi4by]="O"
        deniz[gemi4bx + 2][gemi4by]="O"
        deniz[gemi4bx + 3][gemi4by]="O"
        print_deniz(deniz)
        break

