from time import sleep
liste=[['\t'*10,'  ','a','b','c','d','e','f','g','h','k','l'],
['\t'*10,'1','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003'],
['\t'*10,'2','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003'],
['\t'*10,'3','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003'],
['\t'*10,'4','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003'],
['\t'*10,'5','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003'],
['\t'*10,'6','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003'],
['\t'*10,'7','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003'],
['\t'*10,'8','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003'],
['\t'*10,'9','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003'],
['\t'*10,'10','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\u0003','\n']]
liste2=[['','','-','-','-','-','-','-','-','-','-','-','\n'],
['','','-','-','-','-','x','x','x','x','-','-','\n'],
['','','-','-','-','-','-','-','-','-','x','-','\n'],
['','','-','x','x','-','-','-','-','-','-','-','\n'],
['','','-','-','-','-','-','-','-','-','-','x','\n'],
['','','-','-','-','x','x','x','-','-','-','x','\n'],
['','','-','-','x','-','-','-','-','-','-','x','\n'],
['','','-','-','x','-','-','-','-','-','-','x','\n'],
['','','-','-','-','-','-','x','-','-','-','-','\n'],
['','','-','-','x','x','x','-','-','-','-','-','\n']]
#amiral batti oyunu icin iki farkli liste hazilradik ilk liste kullanicinin oyun boyunca
#gorecegi liste ikinci listede gemilerin yeri ve kontrol mekanizmasinin calistigi liste
sayac=15
kazanma=0
#iki tane sayacaimiz var sayac isminde olan 15 den geriye sayarak kalan haklari takip ediyor
#diger sayac da kontrol mekanizmasinda her dogru sonuc sonrasi artiyor ve bizim gemilerimizin
#kampladigi toplam alan 20 ye esit oldugunda oyunun kazanilmasini sagliyor
def engelleme(a,b):
    z = liste[0].index(x)
    if liste[y-1][z]!='\u0003' :
        print('Ayni yere birden fazla deneme yapilamaz!')
#engelleme fonksiyonu ayni yere birden fazla giris yapilmaya calisildiginda
#kontrol edip kullaniciya bildiriyor
def goruntuleme(listeadi):
    for i in listeadi:
        print(*i)
#goruntuleme fonksiyonu ile kullaniciya gosterecegimiz listeyi her defasinda
#for dongusu ile ugrasmamak icin olusturduk
def konum(a,b):
    global kazanma
    global sayac
    z=liste[0].index(x)
#konum fonksiyonu ile  oyununun isleyisini belirledik burda kulanicidan aldigimiz
#girdinin dogru mu yanlis mi veya ayni mi oldugunu inceliyor
#yukarida yazdigimiz engelleme foksiyonunu burada kullandik
    if liste2[y-1][z]=='x':
        print('Gemiyi vurdunuz!')
        liste[y][z]='x'
        liste2[y - 1][z] = 'O'
        kazanma+=1


    elif liste2[y-1][z]=='-':
        sayac-=1
        liste[y][z]='O'
        liste2[y-1][z]='O'
        print(f'Tekrar deneyin!,Kalan Hakkiniz {sayac}')
        sleep(5)
    else:
        engelleme(x,y)

    goruntuleme(liste)

while True:
#while dongusu ile kullanicidan input aldik ve bu inputu yukarida yazdigimiz konum fonksiyonuna verdik
#ve kazanma ve kaybetme durumunu inceledik
    x = input('Sectiginiz sutun harfini giriniz: ')
    y = int(input('Sectiniginiz satirin numarasini giriniz: '))
    konum(x,y)

    if sayac==0:
        bitis=input('15 defa hatali giris yaptiniz,oyuna yeniden baslamak icin e\'ye cikmak icin q\'ya ')
        if bitis=='e':
            sayac=15
            continue
        elif bitis=='q':
            print('Programdan cikiliyor!')
            break
    if kazanma==20 :
        print('Tebrikler basardiniz...')
        break
#kullanicinin kaybetmesi durumunda oyuna yeniden baslamak istiyor mu yoksa cikmak mi istiyor onu sorduk
#gelen inputa gorede program hareket ediyor
