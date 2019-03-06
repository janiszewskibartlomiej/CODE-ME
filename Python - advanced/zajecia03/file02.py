f = open('zen.txt', mode='r')

zawartosc = list(f)
# zawartosc = f.readlines()

# Obie powyższe linijki robią to samo.
# Obie jednak nie zadziałają razem. Każda wysyca iterator.

print(zawartosc)

# Z danych w zmiennej `zawartosc` możemy skorzystać wielokrotnie.
