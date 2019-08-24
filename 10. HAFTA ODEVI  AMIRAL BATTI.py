import random
import time
print('\u272A'*16,"AMIRAL BATTI",'\u272A'*16,sep="")

print("""
*******************************************************
*******************************************************

            AMIRAL BATTI OYUNUNA HOSGELDINIZ

*******************************************************
*******************************************************
_________Oyunumuzda 2 adet4'lu Ucak gemimiz____________
______2 adet 3'lu, 2 adet 2'li, 2 adet de tekli________
_________Destroyerimiz 10X10 bir denizde yatay_________
___________veya dikey olarak konumlanmistir____________
________Lutfen tablodan atis tahmininizi yapiniz_______
*******************************************************
*******************************************************
""")
tahta = [''," 1", " 2", " 3"," 4", " 5", " 6"," 7", " 8", " 9","10\n",
         "11", "12", "13","14", "15", "16","17", "18", "19","20\n",
         "21", "22", "23","24", "25", "26","27", "28", "29","30\n",
         "31", "32", "33","34", "35", "36","37", "38", "39","40\n",
         "41", "42", "43","44", "45", "46","47", "48", "49","50\n",
         "51", "52", "53","54", "55", "56","57", "58", "59","60\n",
         "61", "62", "63","64", "65", "66","67", "68", "69","70\n",
         "71", "72", "73","74", "75", "76","77", "78", "79","80\n",
         "81", "82", "83","84", "85", "86","87", "88", "89","90\n",
         "91", "92", "93","94", "95", "96","97", "98", "99","100\n",]

def ydortlu():  #Fonksiyonlarimizla yatay ve dikey olarak gemilerimizi konumlandiriyoruz.
    drtlu = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27,
             31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46, 47, 51, 52, 53, 54, 55, 56, 57,
             61, 62, 63, 64, 65, 66, 67, 71, 72, 73, 74, 75, 76,
             77, 81, 82, 83, 84, 85, 86, 87, 91, 92, 93, 94, 95, 96, 97]
    global bos
    bos=[]
    say=random.choice(drtlu)
    bos.append(say)
    bos.append(say+1)
    bos.append(say+2)
    bos.append(say+3)
    return bos
ydortlu()
def ddortlu():                          #Dikey Dortlu gemi.
    drtlu = [x for x in range(1,71)]
    global dbos
    dbos=[]
    say=random.choice(drtlu)
    dbos.append(say)
    dbos.append(say+10)
    dbos.append(say+20)
    dbos.append(say+30)
    return dbos
ddortlu()
def yuclu():                            ##Yatay uclu gemi.
    ucclu=[1,2,3,4,5,6,7,8,11,12, 13, 14, 15, 16, 17,18,21, 22, 23, 24, 25, 26, 27,28,
               31, 32, 33, 34, 35, 36, 37,38,41, 42, 43, 44, 45, 46, 47,48,51 ,52 ,53 ,54 ,55 ,56 ,57,58,
               61, 62, 63, 64, 65, 66, 67,68,71,72, 73, 74, 75, 76,
               77,78,81,82, 83, 84, 85, 86, 87,88,91, 92, 93, 94, 95, 96, 97,98]
    global ubos
    ubos=[]
    say=random.choice(ucclu)
    ubos.append(say)
    ubos.append(say+1)
    ubos.append(say+2)
    return ubos
yuclu()
def duclu():                            ##dikey uclu gemi.
    ucclu=[x for x in range(1,81)]
    global dubos
    dubos=[]
    say=random.choice(ucclu)
    dubos.append(say)
    dubos.append(say+10)
    dubos.append(say+20)
    return dubos
duclu()
def yikili():                               ##yatay ikili gemi.
    ikli = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27, 28,29,
                 31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,51,52,53,54,55,56,57,58,59,
                 61, 62, 63, 64, 65, 66, 67, 68,69, 71, 72, 73, 74, 75, 76,
                 77, 78,79, 81, 82, 83, 84, 85, 86, 87, 88,89,91,92,93,94,95,96,97,98,99]
    global yibos
    yibos = []
    say = random.choice(ikli)
    yibos.append(say)
    yibos.append(say + 1)
    return yibos
yikili()
def dikili():                               ##dikey ikili gemi.
    ikli = [x for x in range(1,91)]
    global dibos
    dibos = []
    say = random.choice(ikli)
    dibos.append(say)
    dibos.append(say + 10)
    return dibos
dikili()
def tekli():                                   #Tekli gemiler.
    tkli = [x for x in range(1,101)]
    global tbos
    tbos = []
    say = random.choice(tkli)
    tbos.append(say)
    say1 = random.choice(tkli)
    tbos.append(say1)
    return tbos
tekli()
                            #Eksiklik=Gemilerin birbiriyle cakismasi durumlari ayarlanmadi!
secim=[]                    #Kullanicinin girdigi degerleri ve vurdugu gemileri bu dosyaya atip sorguluyoruz.
deneme=0
while deneme<15:            #Kullaniciya 15 hak verdik. 15 hakki bitirdiginde dongumuz sonlanacak.
    while True:             #dongu icinde kullanici dogru atis,hatali girse
        print("\n")         #veya ayni atisi yapsa da donecek dongumuz.
        for i in tahta:
            print(i, end=" ")
        print("Kalan hakkiniz:",(15-deneme))
        secim1 = (input('Seciminiz:'))
        if secim1.isnumeric()==False:
            print("Lutfen sayi giriniz.")
            continue
        elif int(secim1)<0 or int(secim1)>101:
            print("0 ile 100 arasinda secim yapiniz.")
            continue
        elif secim1 in secim or int(secim1) in secim:
            print("Bu atisi zaten yaptiniz")
            continue
        else:
            secim.append(int(secim1))
            time.sleep(1)
        for i in tahta:                                                 #Burada artik kul. giris yaptigi degeri
            if not(bos==dbos==ubos==dubos==yibos==dibos==tbos==[]):     #olusturdugumuz gemilerden herhangi birinin
                if int(secim1) in bos:                                  #icerisinde olup olmadigini sorguluyoruz.
                    for i in bos:
                        secim.append(i)
                        print(i,"Ucak Gemisi Vurdunuz!",end="")
                        del tahta[int(i)]
                        tahta.insert(int(i), '\u272A')
                    bos.clear()
                    break
                elif int(secim1) in dbos:
                    for i in dbos:                                      #sayet atisimiz herhangi bir gemiye isabet etmisse
                        secim.append(i)                                 #bu geminin tamamini tahtaya yazip, "secim" dosyasina kaydederek
                        print(i,"Ucak Gemisi Vurdunuz!",end="")         #ayni gemiye tekrar atis yapilmasini engelliyoruz.
                        del tahta[int(i)]
                        tahta.insert(int(i), '\u272A')
                    dbos.clear()
                    break
                elif int(secim1) in ubos:
                    for i in ubos:
                        secim.append(i)
                        print(i,"Kruvazor Vurdunuz!",end="")
                        del tahta[int(i)]
                        tahta.insert(int(i), '\u272A')
                    ubos.clear()
                    break
                elif int(secim1) in dubos:
                    for i in dubos:
                        secim.append(i)
                        print(i, "Kruvazor Vurdunuz!", end="")
                        del tahta[int(i)]
                        tahta.insert(int(i), '\u272A')
                    dubos.clear()
                    break
                elif int(secim1) in yibos:
                    for i in yibos:
                        secim.append(i)
                        print(i,"Destroyer Vurdunuz!",end="")
                        del tahta[int(i)]
                        tahta.insert(int(i), '\u272A')
                    yibos.clear()
                    break
                elif int(secim1) in dibos:
                    for i in dibos:
                        secim.append(i)
                        print(i,"Destroeyer Vurdunuz!",end="")
                        del tahta[int(i)]
                        tahta.insert(int(i), '\u272A')
                    dibos.clear()
                    break
                elif int(secim1) in tbos:
                    for i in tbos:
                        if int(i)==int(secim1):
                            print(i,"Hafif gemi Vurdunuz!",end="")
                            del tahta[int(i)]
                            tahta.insert(int(i), '\u272A')
                            tbos.remove(int(i))
                        else:
                            pass
                    break
            else:                                                       #Tum gemiler vuruldugunda oyun bitecek
                print("Tebrikler...Tum gemileri batirdiniz")            #sayet gemiler cakismamissa (!)
                quit()
        else:
            print("Hoop! Karavana...")                                  #bosa atis durumu, denem hakkinin azalmasi...
            deneme += 1
            del tahta[int(secim1)]
            tahta.insert(int(secim1), "?")
            break
print("Hakkiniz bitti, Tekrar deneyin!")
