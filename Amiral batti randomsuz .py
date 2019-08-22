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
      ["A",0,1,0,0,0,0,0,0,0,0],
      ["B",0,1,0,0,0,1,0,0,0,0],
      ["C",0,0,0,0,0,1,0,0,0,0],
      ["D",0,1,1,0,0,1,0,0,0,0],
      ["E",0,0,0,0,0,1,0,0,1,0],
      ["F",0,0,0,0,0,0,0,0,1,0],
      ["G",0,0,1,1,1,1,0,0,1,0],
      ["H",1,0,0,0,0,0,0,0,0,0],
      ["I",0,0,0,0,1,0,0,0,0,0],
      ["J",0,0,1,1,1,0,0,0,0,0]
      ]
# check \u2713
# cross \u2717
def tablo_goster():
  for i in tablo:
    print("\t".expandtabs(30),*i,end="\n"*2)

def kontrol(tablo):
  kontrol=[x for i in tablo for x in i if x=="\U0001F6A2"]
  return len(kontrol)

import time
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
  if tablo2[sutun_dic[sutun]][satir]==0 and tablo[sutun_dic[sutun]][satir]==0:     # Gemilerin olmadigi yerde ise ve tabloda daha once isaretlenmemisse  
    tablo[sutun_dic[sutun]][satir]="X"
    tablo2[sutun_dic[sutun]][satir]="X"
    hak -= 1
    time.sleep(5)

  if kontrol(tablo)==20:
    print("Tebrikler....Kazandiniz")
    break
  if hak==0:
    print("Hakkiniz kalmadi oyunu kaybettiniz...")
    break
  

