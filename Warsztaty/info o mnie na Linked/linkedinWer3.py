obecnie = {'Python': 'SQL', 'w szkole CODE:ME': 'in infoShare Academy'}
staz = 'FNX Group'
k = 'Tester oprogramowania'
c = 'ISTQB FL'

while True:
    dzien = input('Wpisz dzień: ')
    miesiac = input('Wpisz miesiąc: ')
    rok = input('Wpisz rok: ')
    try:
        liczba_z_dzien = int(dzien)
        liczba_z_miesiac = int(miesiac)
        liczba_z_rok = int(rok)
        break
    except ValueError:
        print('Wprowadzone wartość nie są liczbami całkowitymi, proszę wpisać je ponownie!')

if liczba_z_dzien <= 30 and liczba_z_miesiac <= 11 and liczba_z_rok <= 2018:
    print('Ukończyłem kurs: {}. Posiadam certyfikat: {}.\n'
          '\nObecnie odbywam staż w {}.'.format(k, c, staz), end='\n')
    if liczba_z_dzien <= 31 and liczba_z_miesiac <= 10 and liczba_z_rok <= 2018:
        print('\nUczę się języka {}'.format(' '.join(obecnie)))
    else:
        print('\nUkończyłem, również kurs: {}.'.format(' '.join(obecnie)))
else:
    print('Odbyłem staż w FNX Group. Ukończyłem m.in. kurs: {}, {}. '
          '\nPosiadam certyfikat: {}.'
          '\n\nJestem otwarty na nowe wyzwania :)'.format(' '.join(obecnie), k, c))

if liczba_z_dzien >= 14 and liczba_z_miesiac >= 11 and liczba_z_rok >= 2018:
    print('\nI\'m lerning', obecnie['Python'], obecnie['w szkole CODE:ME'])
print('\nDużą radość sprawia mi, jak kod zacznie działać ! :}')

znam = ['\nProgramy które znam to: Python, Pycharm, Git, Selenium IDE, Katalon Recorder,'
        '\nJira, Enterprise Architect, Photoshop, MS FrondPage, Slack, Skitch, Podio']

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
