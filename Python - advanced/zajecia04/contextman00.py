f = open('zen.txt', mode='r')
zawartosc = list(f)
print(zawartosc)
print('zamknięty?', f.closed)

f.close()

print('zamknięty?', f.closed)
