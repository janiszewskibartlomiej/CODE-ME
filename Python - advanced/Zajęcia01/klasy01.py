class Kot:
    _lapy = 4    # jest to atrybut prywatnego to podkreślenie

    def __init__(self, imie):  #to jest inicjalizator  -
        # wpinamy się tu w pythona i mówimy inisjalizatorowi co ma tu zrobić
        self.imie = imie

    def daj_glos(self):   # metoda daj głos. zawsze odwoje się do self
        print("Miau!")


if __name__ == '__main__':   # to jest porównanie. nietypowe ezialania pythona rozpoznajemy po 2 podkreśleniach
    # to jest pominjane przy imporcie nie jest brane pod uwage gdy zaimiportujemy cos z pilki klasy01
    k = Kot('Filemon')
    print(k)   # wypisujemy ten obiekt na ekran zwraca:
    # <__main__.Kot object at 0x0123DD70> - to jest tez dander
    k.daj_glos()  # k jest wstawiane pod samego siebie czyli pod selfa. wywolujemy metodę obiektu

    #  __x___ to znaczy dander x tak to nazwano w python
    # wszystkie dandery są związane z protokołem w python
    # interface w python - pod spodem kożysta z dander np inicjalizatora

    # print(k.__dir__())


