# Uwaga, ten plik jest zapisem linii, które najlepiej przetestować w REPL'u (interaktywnej konsoli Pythonowej)

# Rzutowanie typu 'str' na typ 'bool'
liczba = int('24')
type(liczba)  # otrzymaliśmy zmienną typu 'int

# to nie działa, gdy string będzie niepoprawnie sformatowany
int('24.6')  # zakomentuj (lub usuń) tę linię, aby cały program zadziałał

# z liczby można stworzyć stringa (typ 'str')
str(35)

# tak samo można ze stringa stworzyć liczbę zmiennoprzecinkową
float('555')
float('555.7')

# przetestuj rzutowanie na typ 'bool' dla różnych typów danych i różnych ich wartości

bool(13)  # True
bool(0)  # False
bool('tekkst') # True
bool('') # False
bool(' ') # True, gdyż ten string zawiera jeden znak (spację)
bool(10.23) # True
bool(0.0) # False
bool(0.00000001)  # True
bool(None)  # False
