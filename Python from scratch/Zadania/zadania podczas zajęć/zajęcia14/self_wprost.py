class Klasa:
    def __init__(self):
        self.atrybut = 17

    def dodaj(self, skladnik):
        self.atrybut += skladnik


k = Klasa()
print(k.atrybut)

k.dodaj(100)
print(k.atrybut)

# To jest przykład! Proszę nie używać poniższej składni programach
Klasa.dodaj(k, 100)  # dokładnie to samo co: k.dodaj(100)
print(k.atrybut)
