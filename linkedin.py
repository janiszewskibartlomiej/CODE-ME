staz = 'FNX Group'
obecnie = {'Python od podstaw w szkole CODE:ME'}
k = 'Tester oprogramowania'
c = 'ISTQB FL'

d = int(input('Wpisz dzień: '))
m = int(input('Wpisz miesiąc: '))
r = int(input('Wpisz rok: '))

if d <= 30 and m <= 11 and r <= 2018:
   print('Ukończyłem kurs: {}. Posiadam certyfikat: {}.''\n'
         'Obecnie odbywam staż w {}.'.format(k,c,staz,))
   if d<=31 and m<=10 and r<=2018:
       print('Uczę się również: {}'.format(obecnie))

else:
    print('Odbyłem staż w FNX Group. Ukończyłem kurs: {}, {}.''\n'
          'Posiadam certyfikat: {}.''\n'
          'Jestem otwarty na nowe wyzwania :)'.format(obecnie,k,c))

print('\n''Dużą radość sprawia mi, jak kod zacznie działać ! :}')