#veri girişi
a1 = int(input('bir sayı giriniz'))
b1 = int(input('bir sayı giriniz'))
c1 = int(inpur('bir sayı giriniz'))

a2 =int(input('bir sayı giriniz'))
b2 = int(input('bir sayı giriniz'))
c2 = int(input('bir sayı giriniz'))

#Diskriminant hesabı
D = a1*b2-a2*b1
Dx = (b1*c2-b2*c1)
Dy = (a1*c2 - a2*c1)


if D !=0:
    x = Dx/D
    y = Dy/D
    print(f'x = {x} , y = {y}')
else:
    print('ya kök yok ya da sonsuz çözüm var lütfen gerçek bir öğretmene danışın')
