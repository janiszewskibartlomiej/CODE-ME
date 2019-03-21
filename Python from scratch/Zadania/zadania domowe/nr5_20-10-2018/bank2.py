from konta2 import Konto, KontoOszczednosciowe

k1 = Konto()
k1.wplata(3700)
print(k1)
k1.wyplata(2000)
print(k1)
k1.wyplata(9999)  # wypłata przekraczająca saldo

print()

k2 = KontoOszczednosciowe(1.5)
k2.wplata(4500)
print(k2)
k2.dolicz_odsetki(30)  # po mięsiącu oszczędzania
print(k2)
k2.wyplata(100)
k2.wyplata(100)
k2.wyplata(100)
print(k2)