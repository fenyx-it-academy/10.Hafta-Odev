import random
import time
print("AMIRAL BATTI OYUNU".center(50))

while True:
    menu = int(input("""    1- RANDOM GEMI EKLEME 
    2- OYUNA BASLAMA
    3- GEMI YERLESIMINI GORME
    
    Lutfen Yapmak Istediginiz Islemin Numarasini Giriniz :"""))

    if menu==1:

        tahta_gemi = [ ["---" for i in range(10)] for i in range(10)]       #geminin yerlestirildigi tahta
        tahta1 = [(a, b) for a in range(10) for b in range(10)]             #10*10 tahta icin koordinat listesi
        durum = "c"
        while durum!="b" :
            gemi_buyuk = int(input("\nLutfen gemi buyuklugunu giriniz (en fazla 10 birim) :"))
            gemi_miktar = int(input("\nLutfen gemi miktarini giriniz :"))
            gemi_liste = []                     # girilen buyuklukte geminin bos bir tahta uzerinde yerlesebilecek tum ihtimalleri barindiran liste
            alt_liste = []                      # girilen buyuklukte gemi icin bir ihtimal barindiran ara liste. bu ihtimallerin birlesimi "gemi_liste" yi olusturuyor
            for c in range(10-gemi_buyuk+1):    # gemi buyuklugune gore bos 10x10 luk bir tahta icin tum ihtimalleri liste halinde veren dongu
                for a in range(10):
                    alt_liste = []
                    for b in range(gemi_buyuk):
                        b=b+c
                        alt_liste+=[(a,b)]
                    gemi_liste += [alt_liste]

            for c in range(10 - gemi_buyuk + 1):
                for a in range(10):
                    alt_liste = []
                    for b in range(gemi_buyuk):
                        b = b + c
                        alt_liste += [(b, a)]
                    gemi_liste += [alt_liste]

            # yeni_liste = [[(a, b + c) for b in range(gemi_buyuk)] for a in range(10) for c in
            #               range(10 - gemi_buyuk + 1)] + [[(b + c, a) for b in range(gemi_buyuk)] for a in range(10) for
            #                                              c in range(10 - gemi_buyuk + 1)]



            tahmin_liste =[]                # mevcut tahtadaki bos yerler ile tum ihtimalleri barindiran listedeki ortak elemanlarin listesi. mevcut tahtadaki gemimizi yerlestirebilecegemiz ihtimallerin listesi
            yerlesim_liste=[]               # tahmin_liste sinden random larak secilen geminin yerlestirilecegi son konunlari barindiran liste.
            for i in range(gemi_miktar):
                for i in gemi_liste:
                    if set(i).issubset(set(tahta1)):
                        tahmin_liste+= [i]
                if tahmin_liste!=[]:
                    tahmin = random.choice(tahmin_liste)
                    for a in tahmin:
                        tahta1.remove(a)
                    yerlesim_liste+=[tahmin]
                    tahmin_liste = []
            if len(yerlesim_liste)==0:
                print("\n\nBU MIKTAR VE BUYUKLUKTE GEMI YERLESTIRECEK YER BULUNMAMAKTADIR. LUTFEN DAHA KUCUK EBAT DENEYINIZ\n")
                time.sleep(2)
            elif 0<len(yerlesim_liste)<gemi_miktar:
                print(f"\nBU BUYUKLUKTE SADECE {len(yerlesim_liste)} ADET GEMI ICIN YER BULUNMKATADIR\n")
                time.sleep(2)
            elif len(yerlesim_liste)==gemi_miktar:
                for v in yerlesim_liste:
                    for n in v:
                        tahta_gemi[n[0]][n[1]]="<0>"

            durum = input("\nTekrar Gemi Eklemek Icin herhangi bir tusu --- Ana Menu icin 'B' Tusuna basiniz : \n").lower()

    elif menu==2:

        tahta = [["---" for i in range(10)] for i in range(10)]

        sonuc_liste=[]
        dogru_hamle_liste=[]
        yanlis_hamle_liste=[]
        satir_sayisi=-1
        sutun_sayisi=-1
        for a in tahta_gemi:
            satir_sayisi+=1
            sutun_sayisi=-1
            for b in a:
                sutun_sayisi+=1
                if b=="<0>":
                    sonuc_liste+=[(satir_sayisi,sutun_sayisi)]

        def giris():
            global sutun
            global satir
            atlama = True
            dongu_giris = True
            while dongu_giris == True:
                try:
                    if atlama == True:
                        satir = int(input("\nSatir Numarasini Giriniz [1, 2, 3 .... ,10] : \n"))
                        if 0>satir or satir>10:
                            print("\nLutfen 1 ile 10 arasinda bir sayi giriniz....\n")
                        else:
                            atlama=False
                    if atlama==False:
                        sutun = int(input("\nSutun Numarasini Giriniz [1, 2, 3 .... ,10] : \n"))
                        if 0>sutun or sutun>10:
                            print("Lutfen 1 ile 10 arasinda bir sayi giriniz....")
                        else:
                            dongu_giris=False
                except ValueError:
                    print("Lutfen 1 ile 10 arasinda bir sayi giriniz....")

            sutun = sutun - 1
            satir = satir - 1

        while True:
            for d in tahta:
                print("\t".expandtabs(30), *d, end="\n")
            giris()

            if tahta[satir][sutun]=="<0>" or tahta[satir][sutun]==" X ":
                print("\n ?????? BU ALANA DAHA ONCE HAMLE YAPTINIZ LUTFEN TEKRAR DENEYINIZ ?????? \n")
            else:
                if tahta_gemi[satir][sutun]=="<0>":
                    print("\n<<<<<< TEBRIKLER BASARILI BIR HAMLE YAPTINIZ >>>>>>\n")
                    tahta[satir][sutun] = "<0>"
                    dogru_hamle_liste+=[(satir,sutun)]
                    time.sleep(2)

                else :
                    print("\n!!!!!! UZGUNUM BASARISIZ BIR HAMLE YAPTINIZ !!!!!!\n")
                    tahta[satir][sutun]= " X "
                    yanlis_hamle_liste+=[(satir,sutun)]
                    time.sleep(5)

            if set(sonuc_liste)==set(dogru_hamle_liste):
                print("\n<<<<<< TEBRIKLER OYUNU KAZANDINIZ >>>>>> ")
                break
            elif len(yanlis_hamle_liste)==15:
                print("\n !!!!! UZGUNUZ OYUNU KAYBETTINIZ !!!!!!")
                break

    if menu==3:
        for d in tahta_gemi:
            print("\t".expandtabs(30), *d, end="\n")

