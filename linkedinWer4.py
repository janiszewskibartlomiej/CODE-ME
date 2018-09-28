obecnie = {'Python': 'SQL', 'w szkole CODE:ME': 'in infoShare Academy'}
staz = 'FNX Group'
k = 'Tester oprogramowania'
c = 'ISTQB FL'
while True:
    dzien = input('Wpisz dzień: ')
    miesiac = input('Wpisz miesiąc: ')
    rok = input('Wpisz rok: ')
    try:
        l_z_dzien = int(dzien)
        l_z_miesiac = int(miesiac)
        l_z_rok = int(rok)
        break
    except ValueError:
        print('Wprowadzone wartość nie są liczbami całkowitymi, proszę wpisać je ponownie!')
if l_z_dzien <= 30 and l_z_miesiac <= 11 and l_z_rok <= 2018:
    print('Ukończyłem kurs: {}. Posiadam certyfikat: {}.\n'
          '\nObecnie odbywam staż w {}.'.format(k, c, staz), end='\n')
    if l_z_dzien <= 31 and l_z_miesiac <= 10 and l_z_rok <= 2018:
        print('\nUczę się języka {}'.format(' '.join(obecnie)))
    else:
        print('\nUkończyłem, również kurs: {}.'.format(' '.join(obecnie)))
else:
    print('Odbyłem staż w FNX Group. Ukończyłem m.in. kurs: {}, {}. '
          '\nPosiadam certyfikat: {}.'
          '\n\nJestem otwarty na nowe wyzwania :)'.format(' '.join(obecnie), k, c))
print('\nDużą radość sprawia mi, jak kod zacznie działać ! :}')
znam = ['\nProgramy które znam to: Python, Pycharm, Git, Selenium IDE, Katalon Recorder,'
        '\nJira, Enterprise Architect, Photoshop, MS FrondPage, Slack']
while True:
    pytanie = input('\nCzy chcesz wiedzieć jakie znam programy ? [napisz T lub N]: ')
    if pytanie == 't' or pytanie == 'T':
        for programy in znam:
            print(programy)
        break
while True:
    meetup = input('\nCzy chcesz wiedzieć jaki jestem? [napisz T lub N]:')
    if meetup == 't' or meetup == 'T':
      jestem = ('\nSpotkajmy się i porozmawiajmy, to najlepszy sposób aby potwierdzić że jestem:\n'
                'Komunikatywny, Obowiązkowy, Punktualny, Pogodny,\n'
                'posiadam zdolności Analityczne,'
                ' Dyplomatyczne oraz lubię pracować w Team\'ie.')
      print(jestem)
      break