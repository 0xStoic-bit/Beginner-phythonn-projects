#Ortalama hesapla

#Alan Kodları
Bilgisayar =1
Güzel_sanatlar =2


Bil_Öğrenciler = []
Gs_Öğrenciler = []

ad = str(input('öğrenci adı girin : '))
soyad = str(input('öğrenci soyadı girin : '))

vize = int(input('Bir Vize  Notu giriniz : '))
final = int(input('Bir Final Notu  girinniz: '))

Alan = int(input('Bir alan Kodu girin (1 = Bilgisayar , 2 = Güzel sanatlar)' ))


OrtalamaBm = vize*0.4 + final*0.6
OrtalamaGs = vize*0.5 + final*0.5

if Alan == Bilgisayar:
    if   100 >=  OrtalamaBm >= 90 :
        print('AA ile geçti')
    elif 90 > OrtalamaBm >= 80 :
        print('BA ile geçti')
    elif 80 > OrtalamaBm >=70:
        print('BB ile geçti')
    elif 70 > OrtalamaBm >=60:
        print('BC ile geçti')
    elif 60 > OrtalamaBm >= 50:
        print('CC ile geçti')
    else:
        print('KALDI YAZ OKULU HAYIRLI OLSUN')
    Bil_Öğrenciler.append(f'{ad} , {soyad}, {OrtalamaBm}')

if Alan == Güzel_sanatlar:
    if 100 >= OrtalamaGs >= 90:
        print('AA ile geçti')
    elif 90 > OrtalamaGs >= 80:
        print('BA ile geçti')
    elif 80 > OrtalamaGs >= 70:
        print('BB ile geçti')
    elif 70 > OrtalamaGs >= 60:
        print('BC ile geçti')
    elif 60 > OrtalamaGs >= 50:
        print('CC ile geçti')
    else:
        print('KALDI YAZ OKULU HAYIRLI OLSUN')
    Gs_Öğrenciler.append(f'{ad} , {soyad} , {OrtalamaGs}')

print(Bil_Öğrenciler)
print(Gs_Öğrenciler)
