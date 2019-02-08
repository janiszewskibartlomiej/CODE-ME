from datetime import datetime
import time

obecnie = {'Python': 'SQL', 'w szkole CODE:ME': 'in infoShare Academy'}
staz = 'FNX Group'
k = 'Tester oprogramowania'
c = 'ISTQB FL'

teraz = datetime.now()
print('Teraz jest:',teraz)
time.sleep(1)

if teraz <= datetime(2018,11,30):
    nr1 = '\nUkończyłem kurs: {}. Posiadam certyfikat: {}.' \
          '\nObecnie odbywam staż w {}.'.format(k, c, staz)
    for element in nr1:
        print(element, end='')
        time.sleep(0.1)
    if teraz <= datetime(2018,10,31):
        nr2 = '\nUczę się języka {}'.format(' '.join(obecnie))
        for element in nr2:
            print(element, end='')
            time.sleep(0.1)
    else:
        nr3 = '\nUkończyłem również kurs: {}.'.format(' '.join(obecnie))
        for element in nr3:
            print(element, end='')
            time.sleep(0.1)
else:
    nr4 = '\nOdbyłem staż w FNX Group i Jestem otwarty na nowe wyzwania :). \n\nUkończyłem m.in. kurs: {}, {}.' \
          '\nPosiadam certyfikat: {} oraz {}.'.format(' '.join(obecnie), k, c, 'Python')
    for element in nr4:
        print(element, end='')
        time.sleep(0.1)

if datetime(2018,11,14) < teraz < datetime(2019,1,16):
    nr5 = '\nI\'m lerning ', obecnie['Python'],' ', obecnie['w szkole CODE:ME']
    for element in nr5:
        print(element, end='')
        time.sleep(0.1)
nr6 = '\n\nDużą radość sprawia mi, jak kod zacznie w końcu działać ! :}\n'
for element in nr6:
    print(element, end='')
    time.sleep(0.1)

while True:
    pytanie = input('\nCzy chcesz wiedzieć jakie znam programy ? [napisz Tak lub Nie]: ')
    time.sleep(0.2)
    if pytanie == 'tak' or pytanie == 'Tak':
        znam = '\nProgramy które znam to: Python, Pycharm, Git, Selenium IDE, Katalon Recorder,' \
               '\nJira, Enterprise Architect, Photoshop, MS FrondPage, Slack, Skitch, Podio. Uczę się również Selenium WebDriver.\n'
        for element in znam:
            print(element, end='')
            time.sleep(0.1)
        break

while True:
    meetup = input('\nCzy chcesz wiedzieć jaki jestem? [napisz Tak lub Nie]:')
    time.sleep(0.2)
    if meetup == 'tak' or meetup == 'Tak':
      jestem = '\nSpotkajmy się i porozmawiajmy, to najlepszy sposób aby potwierdzić że jestem:\n' \
               'Komunikatywny, Obowiązkowy, Punktualny, Pogodny,\n' \
               'posiadam zdolności Analityczne, ' \
               'Dyplomatyczne oraz lubię pracować w Team\'ie.'
      for element in jestem:
          print(element, end='')
          time.sleep(0.1)
      break

moge_pracowac = 'Gdańsku, Gdyni, Sopocie i okolicach Trójmiasta.'
time.sleep(2)
print('\n\nZe względu na moją elastyczność mogę pracować w: {}'
      .format(moge_pracowac))

