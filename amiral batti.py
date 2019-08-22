import time as zaman
import random

tahta = [["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
         ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
         ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
         ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
         ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
         ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
         ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
         ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
         ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
         ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"]
                                                                                          ]
#***************************************************************************
#sanal tahta ile islerimiz bi hayli kolaylasir.Gemi yerlestirmelerini bu tahta uzerinde yaparak
#karsilastirma yapiyoruz.




sanal_tahta= [["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
              ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
              ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
              ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
              ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
              ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
              ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
              ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
              ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"] ,
              ["___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___" , "___"]
              ]

#*********************************************************************
#         TABLOYU RANDOM HAZIRLAMA
#X DUZLEMINDE 4,3,2,1 BIRIM GEMI
#Y DUZLEMINDE 4,3,2,1 BIRIM GEMI
#RANDOM OLARAK TABLO OLUSTURUYOR
tablo=[[i,a] for i in range(10) for a in range(10)]


gemiler=[' A ',' K ',' G ',' X ','!!!'] # TEKRAR GIRMEYI ONLEMEK ICIN OLUSTURULAN LISTE
vurulan_gemi=[' A ',' K ',' G ',' X '] #ISABET EDEN GEMILERI TABLOYA YAZABILMEK ICIN OLUSTURULAN TABLO

def temizle():
    for x in tablo :
        sanal_tahta[x[0]][x[1]] = "___"

    return


def sanal_ekran():

    print(' '*10,'GEMILERIN YERLESIMLERI \n')
    print ( '\n' , ' ' * 36 ,
            ' [Y] -->   [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}]'.format ( 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ,
                                                                                    9 ) , '\n' )
    sayac = 0
    for i in sanal_tahta :
        print ( ' ' * 38 , '[X][' , sayac , '] ' , *i , '\n' )
        sayac += 1

def xxxy():
    i=0
    xxxx_y = list(str(random.randrange(10,100)))
    while i<4:
        sanal_tahta[int ( int( xxxx_y[0] ) ) + i][int ( int( xxxx_y[1] ) ) - 1] = 'A'.center ( 3 )
        i += 1
    return

def xxxx():
    while True :
        xxxx_x = list ( str ( random.randrange ( 10 ,50) ) )
        for k in range ( 4 ) :
            if sanal_tahta[int ( int( xxxx_x[0] ) ) - 1][int ( int( xxxx_x[1] ) ) + k] in gemiler:

                return xxxx()
        i = 0
        break
    while i<4:
        sanal_tahta[int ( int( xxxx_x[0] ) ) - 1][int ( int( xxxx_x[1] ) ) + i] = 'A'.center ( 3 )
        i += 1
    return

def xxy():
    while True :
        xxx_y = list ( str ( random.randrange ( 50 , 100 ) ) )

        for k in range ( 3 ) :
            if sanal_tahta[int ( int( xxx_y[0] ) ) + k][int ( int( xxx_y[1] ) )] in gemiler:
                return xxy()
        i = 0
        break
    while i<3:
        sanal_tahta[int ( int( xxx_y[0] ) ) + i][int ( int( xxx_y[1] ) )] = 'G'.center ( 3 )
        i += 1
    return

def xxx():
    while True:
        xxx = list ( str ( random.randrange ( 10,50 ) ) )
        for k in range ( 3 ) :
            if  sanal_tahta[int ( int( xxx[0] ) ) - 1][int ( int( xxx[1] ) ) + k] in gemiler:
                return xxx()
        i = 0
        break
    while i<3:
        sanal_tahta[int ( int( xxx[0] ) ) - 1][int ( int( xxx[1] ) ) + i] = 'G'.center ( 3 )

        i += 1
    return

def xx():
    while True :

        xx = list(str(random.randrange(50,100)))

        for k in range ( 2 ) :
            if sanal_tahta[int ( int ( xx[0] ) ) + k][int ( int ( xx[1] ) ) - 1] in gemiler :
                return xx()
        i=0
        break
    while i<2:
        sanal_tahta[int ( int( xx[0] ) ) + i][int ( int( xx[1] ) ) - 1] = 'K'.center ( 3 )
        i += 1
    return

def xy():

    while True :
        xy = list ( str ( random.randrange (10,50 ) ) )
        for k in range ( 2 ) :
            if sanal_tahta[int ( int( xy[0] ) ) - 1][int ( int( xy[1] ) ) + k] in gemiler:
                return xy()
        i = 0
        break

    while i<2:

        sanal_tahta[int ( int( xy[0] ) ) - 1][int ( int( xy[1] ) ) + i] = 'K'.center ( 3 )
        i += 1

    return

def x():
    while True:
        x = list ( str ( random.randrange (50, 100) ) )

        if sanal_tahta[int ( int ( x[0] ) ) - 1][int ( int ( x[1] ) ) - 1] in gemiler:
            return x()
        else:
            sanal_tahta[int ( int ( x[0] ) ) - 1][int ( int ( x[1] ) ) - 1] = 'X'.center ( 3 )

        break
    return
def y():
    while True:
        y= list ( str ( random.randrange (10, 100) ) )

        if sanal_tahta[int ( int ( y[0] ) ) - 1][int ( int ( y[1] ) ) - 1] in gemiler :
            return y()
        else:
            sanal_tahta[int ( int ( y[0] ) ) - 1][int ( int ( y[1] ) ) - 1] = 'X'.center ( 3 )

        break
    return

while True:
    try:
        xxxy (); xxxx ();xxy ();xxx ();xx ();xy (); x ();y ();sanal_ekran()
        break
    except:
        temizle()
        continue


#*****************************************************************************************************
#OYUN TARIFI PRINT ILE YAZDIRILIYOR

print("""

************************************************************************************************
                            AMIRAL BATTI
             Deniz olarak varsayacagimiz 10x10'luk bir tablomuz var.
           Bu tabloda

                          2 adet 4 birimlik A
                          2 adet 3 birimlik G
                          2 adet 2 birimlik K
                          2 adet 1 birimlik X

           gemiler mevuttur.Bu gemiler x ve y ekseni dogrultusunda olabilir.

           Sizden istenilen tablo uzerindeki herhangi bir noktaya hamlede bulunun
           ve gemileri vurmaya calisin.Gemilerin herhangi bir noktasina isabet ederse
           ekranda bunu '' A ',' K ',' G ',' X ' goreceksin.Ayni sekilde bosa atis yaptiginda da '!''!''!'
           goreceksin.Her atis oncesi 3 saniye beklemelisin.Daha once yapmis oldugun
           hamleler icin uyari alacaksin.
           Toplamda 15 yanlis hamle hakkin var. Eger tum gemileri vurursan oyunu kazanirsin.
           Atis konumu  x,y koordinat duzeni seklindedir.[x][y],05 gibi bir deger girersen
           x=0,y=5 seklinde konumlandirir.

************************************************************************************************



simdi oyununuz basliyor...............................................
""",'\n'*3)
#*************************************************************************************
bos=[]           #BOS ATISLAR ICIN LISTE
tam_isabet=[]    #ISABETLI ATISLAR ICIN LISTE
hamle=14         #HAMLE SAYISI
#****************************************************************************************
#                 ISABET EDEN ATISLAR ICIN FONKSIYON
def hedef(nisan):
    global tam_isabet
    isabet=list(nisan)#inputtan 99 gibi gelen sayi[9,9] seklinde listeye donusturulur
    # yapilan atislar ayni yere isabet ederse uyari verme dongusu
    if tahta[int(isabet[0])][int(isabet[1])] in gemiler:
        print('Hey... iyimisin buraya daha once ates ettin')
        return
    # yapilan atis SANAL TAHTADA ' A ',' K ',' G ',' X ' degerlerine gelirse normal tahtada
    # ayni noktaya gonderen fonksiyon
    else:

        if sanal_tahta[int(isabet[0])][int(isabet[1])] in vurulan_gemi:
            tam_isabet=[isabet]
            return tam_isabet   #tam_isabet listesi fonksiyonun cagirildigi yere dondurulur
#****************************************************************************************
#                       BOS ATISLAR ICIN FONKSIYON
def iska(bosa):
    global bos
    global hamle
    iska=list(bosa) #inputtan 23 gibi gelen sayi[2,3] seklinde listeye donusturulur
    #yapilan atislar ayni yere isabet ederse uyari verme dongusu
    if tahta[int(bosa[0])][int(bosa[1])] in gemiler:
        return
    #yapilan atis SANAL TAHTADA X degerlerinin disinda bir yere('___') gelirse normal tahtada
    #ayni noktaya gonderen fonksiyon
    else:
        if sanal_tahta[int(iska[0])][int(iska[1])]==('___'):
            bos = [iska]
            hamle-=1       #Hamle sayisi bosa giderse 1 azalir
            return bos #bos listesi fonksiyonun cagirildigi yere dondurulur

#****************************************************************************************
            #EKRANA YAZDIRMA FONKSIYONU
def ekran():
    global tahta
    global hamle

    print(' '*30,hamle+1,'Hamleniz kaldi','\n'*3) #hamle sayisi gosterme

    #OYUN TABLOSU ekrani gosterme
    print ('\n', ' ' * 36 , ' [Y] -->   [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}]'.format(0,1,2,3,4,5,6,7,8,9) ,'\n')
    sayac=0
    for i in tahta:

        print(' '*38,'[X][',sayac,'] ' ,*i,'\n')
        sayac += 1
#****************************************************************************************


ekran()

while True:
#***********************************************************************
#      INPUT ALMA VE HATALARI DUZELTME

    oku=input('\n'"""Lutfen  konumunuzu xy (01)
gibi giriniz[cikis=Q]-->""")
    zaman.sleep ( 3 )
    if oku.upper()=='Q':
        print('oyundan cikiliyor............')
        zaman.sleep(2)
        break
    elif oku.isdigit()==False or len(oku)!=2:
        print('lutfen x ve y degerini xy (15) seklinde giriniz')
        continue
#*****************************************************************************

    # HAMLE =0 olunca oyunu durdurma dongusu
    elif hamle == 0 :
        print ( 'uzgunum ahbap hamle hakkin kalmadi ne yazik ki kaybettin' )
        zaman.sleep ( 2 )
        sanal_ekran ()
        print('\n''Bu sefer olmadi bir dahakine bol sanslar byeee........')
        
        zaman.sleep ( 2 )
        break
#**********************************************************************************
    #return ile gelen Tam_isabet listesi  degerlerini dondurdugu icin
    #tahta tablosunda ' A ',' K ',' G ',' X ' degerlerini yazdirma dongusu
    elif hedef(oku)==tam_isabet:

        #tahta uzerinde hedefi bulan ' A ',' K ',' G ',' X ' degerlerini yazdirma
        for x in tam_isabet :
            tahta[int ( x[0] )][int ( x[1] )] = sanal_tahta[int ( x[0] )][int ( x[1] )]
            print('bravo hedefi 12 den vurdun ')

        ekran ()
        #tum gemiler vurulunca ' A ',' K ',' G ',' X ' degerleri tamamlanmis oldugundan oyunu
        # kazandigini gosteren dongu
        #tum ' A ',' K ',' G ',' X ' degerlerini tahtanin icinden okutuyoruz ve sum komutu ile hepsini topluyoruz
        # 20 olunca oyun kazanilir
        if sum ( [oge.count ( ' A ' ) for satirlar in tahta for oge in satirlar]+
                 [oge.count ( ' G ' ) for satirlar in tahta for oge in satirlar] +
                 [oge.count ( ' K ' ) for satirlar in tahta for oge in satirlar] +
                 [oge.count ( ' X ' ) for satirlar in tahta for oge in satirlar]

                 ) == 20:
            print("""
            **********************************************************
                         TEBRIKLER        KAZANDINIZ

            **********************************************************


            Game over.................................................
            """)
            zaman.sleep(2)
            break
        continue
#************************************************************************
    # return ile gelen bos listesi bosa atis degerlerini dondurdugu icin
    # tahta tablosunda ! degerlerini yazdirma dongusu
    elif iska(oku)==bos:


        for i in bos :
            tahta[int ( i[0] )][int ( i[1] )] = '!!!'.center ( 3 )

        ekran ()
        continue


