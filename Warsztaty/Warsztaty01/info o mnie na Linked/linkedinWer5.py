from datetime import datetime

obecnie = {'Python': 'SQL', 'w szkole CODE:ME': 'in infoShare Academy'}
staz = 'FNX Group'
k = 'Tester oprogramowania'
c = 'ISTQB FL'

teraz = datetime.now()
print('Teraz jest:',teraz)

if teraz <= datetime(2018,11,30):
    print('\nUkończyłem kurs: {}. Posiadam certyfikat: {}.\n'
          '\nObecnie odbywam staż w {}.'.format(k, c, staz), end='\n')

    if teraz <= datetime(2018,10,31):
        print('\nUczę się języka {}'.format(' '.join(obecnie)))

    else:
        print('\nUkończyłem również kurs: {}.'.format(' '.join(obecnie)))

else:
    print('\nOdbyłem staż w FNX Group i Jestem otwarty na nowe wyzwania :). \n\nUkończyłem m.in. kurs: {}, {}. '
          '\n\nPosiadam certyfikat: {} oraz {}.'.format(' '.join(obecnie), k, c, 'Python'))


if datetime(2018,11,14) < teraz < datetime(2019,1,16):
    print('\nI\'m lerning', obecnie['Python'], obecnie['w szkole CODE:ME'])

print('\nDużą radość sprawia mi, jak kod zacznie w końcu działać ! :}')

znam = ['\nProgramy które znam to: Python, Pycharm, Git, Selenium IDE, Katalon Recorder,'
        '\nJira, Enterprise Architect, Photoshop, MS FrondPage, Slack, Skitch, Podio. Uczę się również Selenium WebDriver.']

while True:
    pytanie = input('\nCzy chcesz wiedzieć jakie znam programy ? [napisz Tak lub Nie]: ')

    if pytanie == 'tak' or pytanie == 'Tak':
        for programy in znam:
            print(programy)
        break

while True:
    meetup = input('\nCzy chcesz wiedzieć jaki jestem? [napisz Tak lub Nie]:')

    if meetup == 'tak' or meetup == 'Tak':
      jestem = ('\nSpotkajmy się i porozmawiajmy, to najlepszy sposób aby potwierdzić że jestem:\n'
                'Komunikatywny, Obowiązkowy, Punktualny, Pogodny,\n'
                'posiadam zdolności Analityczne,'
                ' Dyplomatyczne oraz lubię pracować w Team\'ie.')
      print(jestem)

      break

moge_pracowac = 'Gdańsku, Gdyni, Sopocie i okolicach Trójmiasta.'
print('\nZe względu na moją elastyczność mogę pracować w: {}'
      .format(moge_pracowac))

