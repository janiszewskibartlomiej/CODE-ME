a = 'tekst'
b = a

print(a is b)  # porównanie, czy a i b to TEN SAM obiekt

a = 'inny tekst'

print(a is b)

# UWAGA! Nigdy nie używaj wyrażenia `is` do porównywania WARTOŚCI obiektów
