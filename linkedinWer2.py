obecnie = {'Python': 'SQL', 'w szkole CODE:ME': 'in infoShare Academy'}
staz = 'FNX Group'
k = 'Tester oprogramowania'
c = 'ISTQB FL'

d = int(input('Wpisz dzień: '))
m = int(input('Wpisz miesiąc: '))
r = int(input('Wpisz rok: '))

if d <= 30 and m <= 11 and r <= 2018:
    print('Ukończyłem kurs: {}. Posiadam certyfikat: {}.\n'
          '\nObecnie odbywam staż w {}.'.format(k, c, staz), end='\n')
    if d <= 31 and m <= 10 and r <= 2018:
        print('\nUczę się języka {}'.format(' '.join(obecnie)))
    else:
        print('\nUkończyłem, również kurs: {}.'.format(' '.join(obecnie)))
else:
    print('Odbyłem staż w FNX Group. Ukończyłem m.in. kurs: {}, {}. '
          'Posiadam certyfikat: {}.'
          'Jestem otwarty na nowe wyzwania :)'.format(' '.join(obecnie), k, c), end='\n')

if d >= 14 and m >= 11 and r >= 2018:
    print('\nI\'m lerning', obecnie['Python'], obecnie['w szkole CODE:ME'])

print('\nDużą radość sprawia mi, jak kod zacznie działać ! :}')

znam = ['\nProgramy które znam to: Python, Pycharm, Git, Selenium IDE, Katalon Recorder,'
        '\nJira, Enterprise Architect, Photoshop, MS FrondPage, Slack, Skitch, Podio']

pytanie = input('\nCzy chcesz wiedzieć jakie znam programy ? [napisz Tak lub Nie]: ')

if pytanie == 'tak' or pytanie == 'Tak':
    for programy in znam:
        print(programy)

else:
    print('\nDziękuję i zapraszam do kolejnego pytania:')

meetup = input('\nCzy chcesz wiedzieć jaki jestem? [napisz Tak lub Nie]:')

jestem = ('\nSpotkajmy się i porozmawiajmy, to najlepszy sposób aby potwierdzić że jestem:\n'
          'Komunikatywny, Obowiązkowy, Punktualny, Pogodny,\n'
          'posiadam zdolności Analityczne,'
          ' Dyplomatyczne oraz lubię pracować w Team\'ie.')

if meetup == 'tak' or meetup == 'Tak':
    print(jestem)

else:
    print('\nDziękuję za poświęcony czas. ')

moge_pracowac = 'Gdańsku, Gdyni, Sopocie i okolicach Trójmiasta.'

print('\nZe względu na moją elastyczność mogę pracować w: {}'
      .format(moge_pracowac))
