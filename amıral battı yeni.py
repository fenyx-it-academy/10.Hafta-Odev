import random
import time as zaman
koordinat_x_y=[(a, b) for b in range( 10 ) for a in range( 10 )]
sanal_tahta=[["___" for b in range( 10 )] for a in range( 10 )]
tahta=[["___" for b in range( 10 )] for a in range( 10 )]

gemi_yatay=[]
gemi_dikey=[]
depo      =[]
torba     =[]

def gemi_hazirlama():

    gemi = random.randint ( 1 , 5 )
    sec=random.randint(0,1)
    if sec==0:
        gemi_yatay = [[(a , b + c) for b in range ( gemi )] for a in range ( 10 ) for c in range ( 10 - gemi + 1 )]
        return gemi_yatay
    if sec==1:
        gemi_dikey = [[(b + c , a) for b in range ( gemi )] for a in range ( 10 ) for c in range ( 10 - gemi + 1 )]
        return gemi_dikey

def temizle(secime_git):

    silme = []
    asagi_sil = [[((a + 1) % 10 , b) for b in range ( 10 )] for a in range ( 10 )]
    yukari_sil = [[((a + 9) % 10 , b) for b in range ( 10 )] for a in range ( 10 )]
    sag_sil = [[(a , b + 1) for b in range ( 10 )] for a in range ( 10 )]
    sol_sil = [[(a , b - 1) for b in range ( 10 )] for a in range ( 10 )]
    for i in secime_git :
        if 0 < i[0] < 9  and i in koordinat_x_y :
            silme+=[asagi_sil[i[0]][i[1]]]
            silme+= [yukari_sil[i[0]][i[1]]]
        if 0<i[1]<9 and i in koordinat_x_y :
            silme += [sag_sil[i[0]][i[1]]]
            silme += [sol_sil[i[0]][i[1]]]
        if i[0]==0 and i in koordinat_x_y:
            silme += [asagi_sil[i[0]][i[1]]]
        if i[0]==9 and i in koordinat_x_y:
            silme += [yukari_sil[i[0]][i[1]]]
        if i[1]==0 and i in koordinat_x_y:
            silme += [sag_sil[i[0]][i[1]]]
        if i[1]==9 and i in koordinat_x_y:
            silme += [sol_sil[i[0]][i[1]]]

    silme.extend(secime_git)

    for i in set(silme):
        if i in koordinat_x_y:
            koordinat_x_y.remove( i )
    return

def screen():
    kaclik_gemi=[]

    for i in depo :
        kaclik_gemi += [len ( i )]
        for yaz in i :
           sanal_tahta[yaz[0]][yaz[1]] =('X').center(3)

    print ( """
           GEMILER(8 ADET)

    {} adet 5 lik  Ucak gemisi
    {} adet 4 luk  Kruvazor
    {} adet 3 luk  Denizalti
    {} adet 2 lik  mayin gemisi
    {} adet 1 lik  hucum bot
 """.format(kaclik_gemi.count(5),kaclik_gemi.count(4),kaclik_gemi.count(3),kaclik_gemi.count(2),kaclik_gemi.count(1)) )

    for i in sanal_tahta :
        print ( ' ' * 40 , *i , '\n' )


gemiadeti=0

while gemiadeti<8:

        gemi_hazirlama()
        for  i in gemi_hazirlama():

            if set(i).issubset( set( koordinat_x_y ) ):#tahtanin icinde alt kume olarak varmi
                 torba+=[i]

        if torba!=[]:
            secime_git=random.choice(torba)
        torba=[]
        depo.append(secime_git)
        temizle(secime_git)
        gemiadeti+=1

screen()
#__________________________________________________________________________________________________-

print ( """

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
""" , '\n' * 3 )
# *************************************************************************************
bos = []  # BOS ATISLAR ICIN LISTE
tam_isabet = []  # ISABETLI ATISLAR ICIN LISTE
hamle =14  # HAMLE SAYISI


# ****************************************************************************************
#                 ISABET EDEN ATISLAR ICIN FONKSIYON
def hedef(nisan) :
    global tam_isabet
    isabet = list ( nisan )  # inputtan 99 gibi gelen sayi[9,9] seklinde listeye donusturulur
    # yapilan atislar ayni yere isabet ederse uyari verme dongusu
    if tahta[int ( isabet[0] )][int ( isabet[1] )] ==('X').center(3)  :
        print ( 'Hey... iyimisin buraya daha once ates ettin' )
        return
    # yapilan atis SANAL TAHTADA ' A ',' K ',' G ',' X ' degerlerine gelirse normal tahtada
    # ayni noktaya gonderen fonksiyon
    else :

        if sanal_tahta[int ( isabet[0] )][int ( isabet[1] )]==('X').center(3) :
            tam_isabet = [isabet]
            return tam_isabet  # tam_isabet listesi fonksiyonun cagirildigi yere dondurulur


# ****************************************************************************************
#                       BOS ATISLAR ICIN FONKSIYON
def iska(bosa) :
    global bos
    global hamle

    iska = list ( bosa )  # inputtan 23 gibi gelen sayi[2,3] seklinde listeye donusturulur
    # yapilan atislar ayni yere isabet ederse uyari verme dongusu
    if tahta[int ( bosa[0] )][int ( bosa[1] )]==('!!!').center(3) :
        print ( 'Hey... iyimisin buraya daha once ates ettin' )
        return
    # yapilan atis SANAL TAHTADA X degerlerinin disinda bir yere('___') gelirse normal tahtada
    # ayni noktaya gonderen fonksiyon
    else :

        if sanal_tahta[int ( iska[0] )][int ( iska[1] )] == ('___').center(3) :
            bos = [iska]
            hamle -= 1  #
                       # Hamle sayisi bosa giderse 1 azalir
            return bos  # bos listesi fonksiyonun cagirildigi yere dondurulur


# ****************************************************************************************
# EKRANA YAZDIRMA FONKSIYONU
def ekran() :
    global tahta
    global hamle

    print ( ' ' * 30 , hamle + 1 , 'Hamleniz kaldi' , '\n' * 3 )  # hamle sayisi gosterme

    # OYUN TABLOSU ekrani gosterme
    print ( '\n' , ' ' * 36 ,
            ' [Y] -->   [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}]'.format ( 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ,
                                                                                    9 ) , '\n' )
    sayac = 0
    for i in tahta :
        print ( ' ' * 38 , '[X][' , sayac , '] ' , *i , '\n' )
        sayac += 1


# ****************************************************************************************


ekran ()

while True :
    # ***********************************************************************
    #      INPUT ALMA VE HATALARI DUZELTME

    oku = input ( '\n'"""Lutfen  konumunuzu xy (01)
gibi giriniz[cikis=Q]-->""" )
    zaman.sleep ( 1 )
    if oku.upper () == 'Q' :
        print ( 'oyundan cikiliyor............' )
        zaman.sleep ( 2 )
        break
    elif oku.isdigit () == False or len ( oku ) != 2 :
        print ( 'lutfen x ve y degerini xy (15) seklinde giriniz' )
        continue
    # *****************************************************************************

    # HAMLE =0 olunca oyunu durdurma dongusu
    elif hamle == 0 :

        print ( 'uzgunum ahbap yine iskaladin hamle hakkin kalmadi ne yazik ki kaybettin' )
        zaman.sleep ( 2 )
        screen ()
        print ( '\n''Bu sefer olmadi bir dahakine bol sanslar byeee........' )

        zaman.sleep ( 2 )
        break
    # **********************************************************************************
    # return ile gelen Tam_isabet listesi  degerlerini dondurdugu icin
    # tahta tablosunda ' A ',' K ',' G ',' X ' degerlerini yazdirma dongusu
    elif hedef ( oku ) == tam_isabet :

        for x in tam_isabet :
            tahta[int ( x[0] )][int ( x[1] )] = sanal_tahta[int ( x[0] )][int ( x[1] )]
            print ( 'bravo hedefi 12 den vurdun ' )

        ekran ()

        if sum ( [oge.count ( ' X ' ) for satirlar in tahta for oge in satirlar]) ==\
            sum ( [oge.count ( ' X ' ) for satirlar in sanal_tahta for oge in satirlar] ):
            print ( """
            **********************************************************
                         TEBRIKLER        KAZANDINIZ

            **********************************************************


            Game over.................................................
            """ )
            zaman.sleep ( 2 )
            break
        continue
    # ************************************************************************
    # return ile gelen bos listesi bosa atis degerlerini dondurdugu icin
    # tahta tablosunda ! degerlerini yazdirma dongusu
    elif iska ( oku ) == bos :

        for i in bos :
            tahta[int ( i[0] )][int ( i[1] )] = '!!!'.center ( 3 )
        print('ne yazik ki iska gectin..')
        ekran ()
        continue


