with open('zen.txt', mode='r') as f:
    zawartosc = list(f)
    print(zawartosc)
    print('zamknięty?', f.closed)

print('zamknięty?', f.closed)
