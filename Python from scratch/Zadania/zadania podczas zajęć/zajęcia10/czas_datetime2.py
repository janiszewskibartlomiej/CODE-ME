from datetime import datetime

teraz = datetime.now()

print(teraz)

teraz_utc = datetime.utcnow()  # UTC = Coordinated Universal Time (https://pl.wikipedia.org/wiki/Uniwersalny_czas_koordynowany)

print(teraz_utc)

print(teraz - teraz_utc)  # za każdym razem wynik będzie trochę inny
