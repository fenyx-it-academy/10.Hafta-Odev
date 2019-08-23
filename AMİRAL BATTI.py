from random import randint
import time


print("AMİRAL BATTI OYUNUNA HOŞ GELDİNİZ...")
print("oyunumuzda 2 adet 4 birimlik gemi\n 2 adet 3 birimlik gemi \n 2 adet 2 birimlik gemi \n 2 adet 1 birimlik gemi \n mevcuttur...")
print("toplam 15 hakkınız vardır...")

batık_gemi = 0

hak = 16

tablo =[["_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
        ["_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
        ["_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
        ["_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
        ["_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
        ["_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
        ["_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
        ["_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
        ["_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
        ["_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"]]




def deniz(tablo):

      ayır=1

      print("  1 2 3 4 5 6 7 8 9  10 ")

      for i in tablo:
          print(str(ayır)+" "+" ".join(i))  ##satır sutun  olarak ayırdım..
          ayır+=1


def gemiler(tablo):
      return randint(4,len(tablo)-1)
deniz(tablo)
gemi_birimlikler=gemiler(tablo)
gemi_1birimlik=range(1),gemiler(tablo)
gemi_1birimlik2=range(1),gemiler(tablo)
gemi_2birimlik=gemiler(tablo)
gemi_2birimlik2=gemiler(tablo)
gemi_3birimlik=gemiler(tablo)
gemi_3birimlik2=gemiler(tablo)
gemi_4birimlik=gemiler(tablo)
gemi_4birimlik2=gemiler(tablo)



for i in range(16):
        hak-=1
        print(hak,"kallınız kaldı..")
        print("*"*35)
        satir=int(input("1-10 arasında satır giriniz:"))
        sutun=int(input("1-10 arasında sutun giriniz:"))
        deniz(tablo)
        if (satir==gemi_birimlikler and sutun==gemi_birimlikler and satir==gemi_1birimlik and  sutun==gemi_1birimlik and satir==gemi_1birimlik2 and sutun==gemi_1birimlik2\
             and satir==gemi_2birimlik and sutun==gemi_2birimlik and satir==gemi_2birimlik2 and sutun==gemi_2birimlik2\
             and satir==gemi3birimlik and sutun==gemi_3birimlik and satir==gemi_3birimlik2 and sutun==gemi_3birimlik2\
             and satir==gemi_4birimlik and sutun==gemi_4birimlik and satir==gemi_4birimlik2 and sutun==gemi_4bitimlik2):
             deniz(tablo)
             if tablo[satir - 1][sutun - 1] == "/":
                print("*" * 35)
                print("Zaten tahmin ettiniz")
                deniz(tablo)
                
             else:
                print("*" * 35)
                print("Tebrikler gemiyi batırdınız!")
                tablo[satir - 1][sutun - 1] = "/"
                print("*" * 35)
                deniz(tablo)
                batık_gemi += 1
        else:
            if (satir < 0 or sutun < 0) or (satir >11 or sutun >11):
                print("*" * 35)
                print("Alan sınırları dışında değer girdiniz")
            elif tablo[satir - 1][sutun - 1] == "X":
                print("*" * 35)
                print("Zaten tahmin ettiniz")
                print("*" * 35)
                deniz(tablo)
            else:
                print("*" * 35)
                print("Vuramadınız")
                tablo[satir - 1][sutun - 1] = "X"
                print("*" * 35)
                deniz(tablo)
            if batık_gemi == 3:
                print("*" * 35)
                print("Tebrikler bütün gemileri batırdınız ve oyunu kazandınız")
                print("*" * 35)
                break
            if hak ==0:
                  print("*"*35)
                  print("hakkınız bitti...")
                  print("*"*35)
                  break


                    

                    
            
      
      



      
    
    
