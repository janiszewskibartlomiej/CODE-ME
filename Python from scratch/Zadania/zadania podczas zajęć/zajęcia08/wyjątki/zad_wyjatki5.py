# Ten program musi być uruchomiony z konsoli (nie z PyCharma)
# Zwróć uwagę na brak bloku 'except'. Mając blok 'finally' nie jest on potrzebny.

print('Początek programu')

try:
    while True:
        print('NIESKOŃCZONA PĘTLA! Naciśnij: Ctrl+C')
finally:
    print('Ta linijka będzie zawsze wykonana')

print('Koniec programu')  # Ta linijka nigdy nie zostanie wykonana.
