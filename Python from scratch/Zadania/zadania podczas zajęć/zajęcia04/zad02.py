#
# while True:
#     wyraz = input("Podaj wyraz: ")
#
#     if not wyraz:
#         break

#     if ' ' in wyraz:
#         print('Wpisano spację, przerwano działanie ')
#         continue
#
#     print('Wpisany wyraz ma długość:', len(wyraz), 'znaków')


# druga wersja


while True:
    jakis_tekst = input('Proszę wpisać tekst: ')
    jakis_tekst = jakis_tekst.strip()
    if jakis_tekst == '':
        break
    elif ' ' in jakis_tekst:
        print('Znaleziono spację, wpisz wyraz ponownie:')
        continue
    else:
        x = len(jakis_tekst)
        print('Wpisany wyraz ma długość: ', x)
