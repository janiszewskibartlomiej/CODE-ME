from datetime import datetime

def wypisanie_historii():
      plik = open('uruchomienia.log', 'r')
      zawartosc = plik.read()
      print('Uruchomienia do tej pory: ')
      return zawartosc

def zapisanie_uruchomienia():
    plik = open('uruchomienia.log', 'a')
    teraz = datetime.now()
    uruchomienie = 'Skrypt został uruchomiony: {}\n'.format(teraz)
    plik.write(uruchomienie)
    return uruchomienie

if __name__ == '__main__':
    historia = wypisanie_historii()
    print(historia)
    zapisanie = zapisanie_uruchomienia()
    print(zapisanie)
