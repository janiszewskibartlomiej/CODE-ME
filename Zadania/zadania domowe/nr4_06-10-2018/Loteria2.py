
wszystkie_zaklady = []

def dodaj_zaklad(zaklad):
    wszystkie_zaklady.append(zaklad)
    return

if __name__ == '__main__':
    print('Lista zakładów to: ',wszystkie_zaklady)

moj_zaklad = [1, 2, 3, 4]

dodaj_zaklad(moj_zaklad)

if __name__ == '__main__':
    print('Lista zakładów to: ',wszystkie_zaklady)