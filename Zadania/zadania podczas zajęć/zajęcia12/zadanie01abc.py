from datetime import datetime

def wypisanie_historii():
    try:
        with open('uruchomienia.log', 'r') as plik:
          zawartosc = plik.read()
          print('Uruchomienia do tej pory: ')
    except FileNotFoundError:
        print('Brak historii uruchomień')
    return zawartosc

def zapisanie_uruchomienia():
    with open('uruchomienia.log', 'a') as plik:
        teraz = datetime.now()
        uruchomienie = 'Skrypt został uruchomiony: {}\n'.format(teraz)
        plik.write(uruchomienie)
    return uruchomienie

if __name__ == '__main__':
    historia = wypisanie_historii()
    print(historia)
    zapisanie = zapisanie_uruchomienia()
    print(zapisanie)
