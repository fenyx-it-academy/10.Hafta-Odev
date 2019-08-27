
import random
import time
tablo=[
      [0,1,2,3,4,5,6,7,8,9,10],
      ["A",0,0,0,0,0,0,0,0,0,0],
      ["B",0,0,0,0,0,0,0,0,0,0],
      ["C",0,0,0,0,0,0,0,0,0,0],
      ["D",0,0,0,0,0,0,0,0,0,0],
      ["E",0,0,0,0,0,0,0,0,0,0],
      ["F",0,0,0,0,0,0,0,0,0,0],
      ["G",0,0,0,0,0,0,0,0,0,0],
      ["H",0,0,0,0,0,0,0,0,0,0],
      ["I",0,0,0,0,0,0,0,0,0,0],
      ["J",0,0,0,0,0,0,0,0,0,0]
      ]
tablo2=[
        [0,1,2,3,4,5,6,7,8,9,10],
      ["A",0,0,0,0,0,0,0,0,0,0],
      ["B",0,0,0,0,0,0,0,0,0,0],
      ["C",0,0,0,0,0,0,0,0,0,0],
      ["D",0,0,0,0,0,0,0,0,0,0],
      ["E",0,0,0,0,0,0,0,0,0,0],
      ["F",0,0,0,0,0,0,0,0,0,0],
      ["G",0,0,0,0,0,0,0,0,0,0],
      ["H",0,0,0,0,0,0,0,0,0,0],
      ["I",0,0,0,0,0,0,0,0,0,0],
      ["J",0,0,0,0,0,0,0,0,0,0]
      ]

def tablo_goster():
    for i in tablo:
        print("\t".expandtabs(30),*i,end="\n"*2)



def birim(birimsayisi):   
  for i in range(2):   # 2 tane istenilen birimde olusturmasi icin for dongusu kurduk 
    rastgele_yatay_dikey=random.choice(["yatay","dikey"])          # yatay dikey mi olacagini rastgele sectik
    if rastgele_yatay_dikey=="yatay":    #yataysa 
      while True: 
        kontrol=0    
        rastgele=random.sample(tablo2[1:],1)  #1 rastgele liste sectik
        satirindex=tablo2.index(rastgele[0])    #Listenin indexi
        sutunindex=random.randint(1,len(tablo2)-birimsayisi)        # Sutun icin 1 tablonun uzunlugunun birimsayisi eksigince rastgele index sectik
        for x in range(birimsayisi):
          if tablo2[satirindex][sutunindex+x]==0:
            kontrol+=1
        if kontrol==birimsayisi:
          for y in range(birimsayisi):
            tablo2[satirindex][sutunindex+y]=1
          break                      # tabloya gemileri yerlestirdik 
        else:                                                       # degilse yani onceden secilmis herhangi bir gemi ile cakisiyorsa 
          continue                                                  # ayni islemleri tekrar yapmasi icin dongunun basina dondu 
    else:    # dikeyse 
      while True:
        kontrol=0
        rastgele=random.sample(tablo2[1:(len(tablo2)-birimsayisi)+1],1)  #1 rastgele liste sectik
        satirindex=tablo2.index(rastgele[0])    #Listenin indexi
        sutunindex=random.randint(1,10)
        for x in range(birimsayisi):
          if tablo2[satirindex+x][sutunindex]==0:
            kontrol+=1
        if kontrol==birimsayisi:
          for y in range(birimsayisi):
            tablo2[satirindex+y][sutunindex]=1
          break
        else:
          continue    


def kontroll(tablo):
  kontrol=[x for i in tablo for x in i if x=="\U0001F6A2"]
  return len(kontrol)

def cozum_tablosu():
  print("Gemi Tablosunu ve Yanlis hedef vuruslarinizi gorebilirsiniz...")
  liste=[]
  for satir in tablo2[1:]:
    satir2 = ["+" if item == 1 else item for item in satir]
    liste+=[satir2]
      
  for x in liste:
    print("\t".expandtabs(30),*x,end="\n"*2)


hak=15
print("""Amiral Batti Oyununa Hosgeldiniz...
Tabloda;
4 birimlik 2 gemi,
3 birimlik 2 gemi,
2 birimlik 2 gemi ve
1 birimlik 2 gemi bulunmaktadir. 
Hedefi vuramadiginizda X,
vurdugunuzda + isareti ile tabloda gorebileceksiniz.
Hedefleri harf ve sayilari kullanarak secebilirsiniz.
15 deneme hakkiniz vardir.
Her yanlis hedefte hakkiniz 1 azalmaktadir..

Basarilar...""")
birim(4)
birim(3)
birim(2)
birim(1)
gemi=0
while True:
    tablo_goster()
    try:
        satir=int(input("Satir Secimi(1-10):"))
        sutun=input("Sutun Secimi(A-J):").upper()
        if satir>10 or satir<1:
            print("Yanlis secim yaptiniz")
            continue
        if not sutun in "ABCDEFGHIJ":
            print("Yanlis secim yaptiniz")
            continue
    except ValueError:
        print("Yanlis tercih yaptiniz.")
        continue
    satir=int(satir)
    sutun_dic={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10}
    
    if tablo2[sutun_dic[sutun]][satir]=="X":     # Yani daha once isaretlenmisse
        print("Daha once bu degeri girmistiniz...")
        continue
    if tablo2[sutun_dic[sutun]][satir]==1 and tablo[sutun_dic[sutun]][satir]==0:     # Gemilerin oldugu yerse ve ilk tabloda bossa
        tablo[sutun_dic[sutun]][satir]="+"
        print("Gemi vuruldu...")
        gemi+=1
    if tablo2[sutun_dic[sutun]][satir]==0 and tablo[sutun_dic[sutun]][satir]==0:     # Gemilerin olmadigi yerde ise ve tabloda daha once isaretlenmemisse
        tablo[sutun_dic[sutun]][satir]="X"
        tablo2[sutun_dic[sutun]][satir]="X"
        hak -= 1
        print("Yanlis hamle...5 sn bekleyin..")
        if hak!=0:
            print(hak,"hakkiniz kaldi...")
        time.sleep(5)


    if kontroll(tablo)==20:
        print("Tebrikler....Kazandiniz..")
        print(gemi,"tane gemiyi vurdunuz...:))")
        cozum_tablosu()
        break
    if hak==0:
        print("Hakkiniz kalmadi oyunu kaybettiniz...")
        print("Ama",gemi," tane gemiyi vurdunuz..")
        cozum_tablosu()
        break

  

