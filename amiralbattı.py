# coding=utf-8
import random
from time import sleep
tahta = [['A',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['B',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['C',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['D',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['E',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['F',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['G',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['H',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['K',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['L',"_", "_", "_","_", "_", "_","_", "_", "_","_"]]

gemiler=[['<','=','=','>'],
['<','=','=','>'],
['<', '=', '>'],
['<', '=', '>'],
['<', '>'],
['<', '>'],
['O'],
['O']]

satır_sozluk={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'K':8,'L':9}

tahta_gemiler=[['A',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['B',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['C',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['D',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['E',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['F',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['G',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['H',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['K',"_", "_", "_","_", "_", "_","_", "_", "_","_"],
['L',"_", "_", "_","_", "_", "_","_", "_", "_","_"]]

def tahta_kontrol():
    #Gemileri yerlestirilecek yerin bos oldup-olmadıgının kontrolu
    global konum_satir,konum_sutun,kontrol
    #degiskenleri fonksiyon dısında kullanailmek icin globallestirme
    for j in range(len(i)):
        #58.satırdaki i-ler gemilerdir. gemilerin uzunlugu boyunca dongu
        if tahta_gemiler[konum_satir][konum_sutun+j]!='_':
            #tahtadan random secilen bir noktadan itibaren
            #gemi karakter sayısınca tahtanın bos olup olmadıgının kontrolu
            konum_satir = random.randint(0, 9)
            konum_sutun = random.randint(1, 11 - len(i))
            #if bloguna girdiginde yani tahta,gemi karakterlerinin denk geldigi
            #yerler boyunca bos degilse random olarak yeni bir koordinat secilir
            kontrol=0
            #donguden cıkmak icin kontrol degiskeni
            return
        else:
            kontrol=1

def oyuncu_hamle():
    #oyuncunun yaptıgı hamleleri isleyen fonksiyon
    global tahta,atis_sayisi,isabetli_atis
    #degiskenleri globallestirme
    if tahta_gemiler[satır_sozluk[satir]][sutun]=='_':
        #tahta uzerinde koordinatları girilen yer bos ise
        tahta[satır_sozluk[satir]][sutun]='X'
        tahta_gemiler[satır_sozluk[satir]][sutun]='X'
        #isabetsiz atis ifadesi 'X'in iki tahtaya da islenmesi
        atis_sayisi-=1
        #oyuncunun atis hakkını bir azalt
    elif tahta[satır_sozluk[satir]][sutun] in ['X','+']:
        #oyuncu aynı yere atis yaparsa uyarı ver
        print('Aynı hedefe atış yaptınız.')
        sleep(2)

    else:
        tahta[satır_sozluk[satir]][sutun]='+'
        tahta_gemiler[satır_sozluk[satir]][sutun]='+'
        #yukardaki durumlar gecerli degilse isabetli bir atis vardır
        #isabetli atis uyarısı'+'nın tataya islenmesi
        isabetli_atis+=1

def ekrana_yazdirma(veri):
    #veri olarak girilecek listeyi ekrana yazdıran foksiyon

    print("\t".expandtabs(50), ' _ _ _ _ _ _ _ _ _ _')
    for i in veri:
        print("\t".expandtabs(50), end='')
        print(*i, '', sep='|')
    print("\t".expandtabs(50), ' 0 1 2 3 4 5 6 7 8 9')
print('''Amiralbattı oyunu yükleniyor...
Bu oyunda altı adet gemiyi vurmaya çalışacaksınız. Toplam 15 
yanlıs atis yapma hakkınız var. Atışlarınızı yaparken sırasıyla
birincisi harf ve ikincisi rakam olacak şekilde iki karakterli 
veri girişi yapınız. Örneğin; A1,K9,E4 gibi... Harf seçiminiz
(A,B,C,D,E,F,G,H,K,L) listesinden, rakam ise 0-9 arası bir
değer olmalıdır. Not:Gireceğiniz harfler büyük harf olmak 
zorunda değildir.\n\n''')

for i in gemiler:
    #gemi listesinden herbir gemi icin dongu
    konum_satir=random.randint(0,9)
    konum_sutun=random.randint(1,11-len(i))
    #random satir ve sutun belirleme
    while True:
        tahta_kontrol()
        #fonksiyon ile gemilerin yerlestirilecegi yerin uygunlugunun kontrolu
        if kontrol==1:
            #foksiyon icinde kullanılan ve global yapılan kontrol degiskeni 1
            #ise gemilerin icin randon secilen koordinatlar uygundur aksi
            #halde gemiler icin foksiyon ile yeni koordinat belirlenir.
            break
            #while dongusunden cıkılır
    for j in range(len(i)):
        #gemi uzunlugu kadar dongu
        tahta_gemiler[konum_satir][konum_sutun+j]=i[j]
        #tahta_gemiler listesine koorninat biligleriyle gemileri yerlestirme

atis_sayisi=15
#oyuncunun toplam yapabilecegi bos atis sayısı
isabetli_atis=0
#Bütün gemilerin vurulup-vurulmadığını kontrol eder

ekrana_yazdirma(tahta)
#ilk defa tahtanın ekrana yazdırılması
while atis_sayisi!=0:
    #atis sayısı sıfırlanana kadar dongu
    atis=input('Atışınızı yapınız.')
    #oyuncudan atis icin veri girisi

    if len(atis)!=2 or atis[0].upper() not in satır_sozluk.keys()\
        or atis[1] not in ['0','1','2','3','4','5','6','7','8','9']:
        #oyuncu uyugun olmayan bir veri girdiginde uyarı
        print('Yanlış veri girdiniz. Yeniden ',end='')

    else:
        satir =atis[0].upper()
        # girilen verinin ilk karakteri satir degiskenine upper yapılıp atanır
        sutun =int(atis[1])+1
        #girilen verinin ikinci karakteri int yapılıp bir fazlası sutun degiskenine atnır
        #bu degerin bir artırılma sebebi tahtanın ilk sutununda harflerin yer almasıdır
        oyuncu_hamle()
        #oyuncunun hamlesinin foksiyonla islenmesi
        print('\n' * 8)
        ekrana_yazdirma(tahta)
        print('\n' * 3)
        #tahtanın foksiyon ile ekrana yazdırılması
        #sleep(3)
        #oyunu 3 sn dondurmak akısı bozdugu icin yorum satırı olarak eklendi

    if isabetli_atis==20:
        #tüm hedeflerin vurulması durumu
        print('\n' * 8)
        print('Tebrikler,tüm hedefler vurldu.')
        ekrana_yazdirma(tahta_gemiler)
        print('\n' * 3)
        #gemilerin bulundugu tahtanın fonksiyonla ekrana yazılması
        quit()
        #while dongusunden cıkıs
print('Başaramadınız,tüm hedefler vurulmadı.')
ekrana_yazdirma(tahta_gemiler)
#15 isabetsiz atis durmunda oyuncuya sonucu bildirme ve
#gemilerin bulundugu tahtanın foksiyonla ekrana yazdırılması










