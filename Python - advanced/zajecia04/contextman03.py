class Szkatulka:
    def __enter__(self):
        return {'nazwa': 'Sekretny Słownik', 'zawartosc': 'klucze i wartości'}

    def __exit__(self, *args):
        pass


with Szkatulka() as s:
    print(s)
    print(s['nazwa'])

# poza 'with' obiekt 's' nadal jest dostępny
print()
print(s['zawartosc'])
