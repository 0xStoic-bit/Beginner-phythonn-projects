#Zar atma

import random

Zar = [1,2,3,4,5,6]


bir = 0
iki = 0
uc = 0
dort = 0
bes = 0
alti = 0

for i in range(100):
    sonuc = (random.choice(Zar))
    if sonuc == 1:
        bir +=1
    elif sonuc == 2:
        iki +=1
    elif sonuc == 3:
        uc +=1
    elif sonuc == 4:
        dort+=1
    elif sonuc == 5:
        bes+=1
    elif sonuc == 6:
        alti+=1

toplam = bir+iki+uc+dort+bes+alti

print('\n  ------- Sonuçlar -----')
print(f'bir {bir} defa geldi , {bir/toplam%2}')
print(f'iki {iki} defa geldi , {iki/toplam%2}')
print(f'üç {uc} defa geldi , {uc/toplam%2}')
print(f'dört {dort} defa geldi , {dort/toplam%2}')
print(f'beş {bes} defa geldi , {bes/toplam%2}')
print(f'altı {alti} defa geldi , {alti/toplam%2 }')
