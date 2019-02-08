d = {'marka': None, 'model': 'Mondeo', 'rocznik': 1910}

print(d)

if d['rocznik'] < 1993:
    print('Gratulacje! Twój samochód',d['marka'], 'możę być zarejestrowany jako zabytek.')

else:
    print('Twój samochód', d['marka'], 'jest jeszcze zbyt młody')

d['czy_oryginalny'] = bool

print(d)