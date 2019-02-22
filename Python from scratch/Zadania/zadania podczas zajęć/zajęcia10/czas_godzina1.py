from datetime import time

samo_poludnie = time(12)

print(samo_poludnie)

kwadrans_po_osmej = time(8, 15)

print(kwadrans_po_osmej)

usain_bolt_na_100m = time(0, 0, 9, 580000)  # ostatni argument jest w mikrosekundach
usain_bolt_na_100m = time(second=9, microsecond=580000)  # ostatni argument jest w mikrosekundach

print(usain_bolt_na_100m)

# UWAGA! Ten obiekt nie umożliwia pobrania aktualnej godziny
