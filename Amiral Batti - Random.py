
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



def birim2_4():  # 4 birimlik 2 gemi icin 
  rastgele=random.sample(tablo[1:8][1:8],2)  #2 rastgele liste sectik
  in1=tablo.index(rastgele[0])    #Ilk listenin indexi 
  in2=tablo.index(rastgele[1])    #Ikinci listenin indexi 
  
  while True:   # Eger tablo2de in1 sutunu ve sonrasinda gelen 4 satir 0 ise
    ind2=random.randint(1,7)        # Sutun icin 1 7 arasinda rastgele sayi tuttuk (Yatay gemi olusturmak icin)
    if tablo2[in1][ind2]==0 and tablo2[in1][ind2+1]==0 and tablo2[in1][ind2+2]==0 and tablo2[in1][ind2+3]==0: # Sutun degerlerini artirdik 
      tablo2[in1][ind2]=1   # gemileri sectik
      tablo2[in1][ind2+1]=1
      tablo2[in1][ind2+2]=1
      tablo2[in1][ind2+3]=1
      break                  # donguden cikiyoruz 
    else:
      continue               # degilse donguye devam et 
  
  while True:
    ind2=random.randint(1,7)   # Satir icin 1 7 arasinda rastgele sayi tuttuk   (Dikey gemi olusturmak icin)
    if tablo2[in2][ind2]==0 and tablo2[in2+1][ind2]==0 and tablo2[in2+2][ind2]==0 and tablo2[in2+3][ind2]==0:  # Satir degerlerini artirdik
      tablo2[in2][ind2]=1
      tablo2[in2+1][ind2]=1
      tablo2[in2+2][ind2]=1
      tablo2[in2+3][ind2]=1
      break
    else:
      continue

def birim2_3():   # 3 birimlik 2 gemi icin
  rastgele=random.sample(tablo[1:8][1:8],2)  #2 liste sectir
  in1=tablo.index(rastgele[0])
  in2=tablo.index(rastgele[1])
  while True: 
    ind2=random.randint(1,8)
    if tablo2[in1][ind2]==0 and tablo2[in1][ind2+1]==0 and tablo2[in1][ind2+2]==0:
      tablo2[in1][ind2]=1
      tablo2[in1][ind2+1]=1
      tablo2[in1][ind2+2]=1
      break
    else:
      continue
  while True:
    ind2=random.randint(1,8)
    if tablo2[in2][ind2]==0 and tablo2[in2+1][ind2]==0 and tablo2[in2+2][ind2]==0:
      tablo2[in2][ind2]=1
      tablo2[in2+1][ind2]=1
      tablo2[in2+2][ind2]=1
      break
    else:
      continue

def birim2_2():  # 2 birimlik 2li gemi icin 
  rastgele=random.sample(tablo[1:8][1:8],2)  #2 liste sectir
  in1=tablo.index(rastgele[0])
  in2=tablo.index(rastgele[1])  
  while True:
    ind2=random.randint(1,10)
    if tablo2[in1][ind2]==0 and tablo2[in1][ind2+1]==0:
      tablo2[in1][ind2]=1
      tablo2[in1][ind2+1]=1
      break
    else:
      continue
  
  while True:
    ind2=random.randint(1,10)
    if tablo2[in2][ind2]==0 and tablo2[in2+1][ind2]==0:
      tablo2[in2][ind2]=1
      tablo2[in2+1][ind2]=1
      break
    else:
      continue

def birim2_1():  # 1 birimlik 2 gemi icin
  rastgele=random.sample(tablo[1:8][1:8],2)  
  in1=tablo.index(rastgele[0])
  in2=tablo.index(rastgele[1])  
  while True:
    ind1=random.randint(1,10)
    ind2=random.randint(1,10)
    if tablo2[in1][ind1]==0 and tablo2[ind2][in2]==0:
      tablo2[in1][ind1]=1
      tablo2[ind2][in1]=1
      break
    else:
      continue

def kontrol(tablo):
  kontrol=[x for i in tablo for x in i if x=="\U0001F6A2"]
  return len(kontrol)


hak=15
print("""Amiral Batti Oyununa Hosgeldiniz...
Tabloda;
4 birimlik 2 gemi,
3 birimlik 2 gemi,
2 birimlik 2 gemi ve
1 birimlik 2 gemi bulunmaktadir. 
Hedefleri harf ve sayilari kullanarak secebilirsiniz.
15 deneme hakkiniz vardir.
Her yanlis hedefte hakkiniz 1 azalmaktadir..

Basarilar...""")
birim2_4()
birim2_3()
birim2_2()
birim2_1()
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
        tablo[sutun_dic[sutun]][satir]="\U0001F6A2"
        print("Gemi vuruldu...")
    if tablo2[sutun_dic[sutun]][satir]==0 and tablo[sutun_dic[sutun]][satir]==0:     # Gemilerin olmadigi yerde ise ve tabloda daha once isaretlenmemisse
        tablo[sutun_dic[sutun]][satir]="X"
        tablo2[sutun_dic[sutun]][satir]="X"
        hak -= 1
        print("Yanlis hamle...5 sn bekleyin..")
        if hak!=0:
            print(hak,"hakkiniz kaldi...")
        time.sleep(5)


    if kontrol(tablo)==20:
        print("Tebrikler....Kazandiniz..")
        break
    if hak==0:
        print("Hakkiniz kalmadi oyunu kaybettiniz...")
        break

  

