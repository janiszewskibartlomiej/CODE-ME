from datetime import datetime
import time
obecnie = {'Python': 'SQL', 'w szkole CODE:ME': 'in infoShare Academy'}
staz = 'FNX Group'
k = 'Tester oprogramowania'
c = 'ISTQB FL'
teraz = datetime.now()
print('Teraz jest:',teraz)
if teraz <= datetime(2018,11,30):
    nr1 = '\nUkończyłem kurs: {}. Posiadam certyfikat: {}.' \
          '\nObecnie odbywam staż w {}.'.format(k, c, staz)
    print(nr1)
    if teraz <= datetime(2018,10,31):
        nr2 = '\nUczę się języka {}'.format(' '.join(obecnie))
        print(nr2)
    else:
        nr3 = '\nUkończyłem również kurs: {}.'.format(' '.join(obecnie))
        print(nr3)
else:
    nr4 = '\nOdbyłem staż w FNX Group i Jestem otwarty na nowe wyzwania :). \n\nUkończyłem m.in. kurs: {}, {}.' \
          '\nPosiadam certyfikat: {} oraz {}.'.format(' '.join(obecnie), k, c, 'Python')
    print(nr4)
if datetime(2018,11,14) < teraz < datetime(2019,1,16):
    nr5 = '\nI\'m lerning ', obecnie['Python'],' ', obecnie['w szkole CODE:ME']
    print(nr5)
nr6 = '\n\nDużą radość sprawia mi, jak kod zacznie w końcu działać ! :}\n'
for element in nr6:
    print(element, end='')
    time.sleep(0.1)
while True:
    pytanie = input('\nCzy chcesz wiedzieć jakie znam programy ? [napisz Tak lub Nie]: ')
    if pytanie == 'tak' or pytanie == 'Tak':
        znam = '\nProgramy które znam to: Python, Pycharm, Git, Selenium IDE, Katalon Recorder,' \
               '\nJira, Enterprise Architect, Photoshop, MS FrondPage, Slack. Uczę się również Selenium WebDriver.\n'
        print(znam)
        break
while True:
    meetup = input('\nCzy chcesz wiedzieć jaki jestem? [napisz Tak lub Nie]:')
    if meetup == 'tak' or meetup == 'Tak':
        jestem = '\nSpotkajmy się i porozmawiajmy, to najlepszy sposób aby potwierdzić że jestem:\n' \
               'Komunikatywny, Obowiązkowy, Punktualny, Pogodny,\n' \
               'posiadam zdolności Analityczne, ' \
               'Dyplomatyczne oraz lubię pracować w Team\'ie.'
        print(jestem)
        break