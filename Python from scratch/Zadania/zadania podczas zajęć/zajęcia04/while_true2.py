while True:
    odpowiedz = input('Napisz [koniec] jeśli chcesz zakończyć program: ')

    if odpowiedz == 'koniec':
        break  # 'break' powoduje wyjście z pętli
        #exit()  - przerywa program wię cnei wydrukuje się koniec programu

    print('Wpisano:', odpowiedz)

print('Koniec programu!')