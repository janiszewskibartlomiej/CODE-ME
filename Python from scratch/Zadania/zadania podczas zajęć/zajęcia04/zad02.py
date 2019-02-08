
while True:
    wyraz = input("Podaj wyraz: ")
    if wyraz == '':
        break
    if ' ' in wyraz:
        print('Wpisano spację, przerwano działanie ')
        continue

    print('Wpisany wyraz ma długość:', len(wyraz), 'znaków')


