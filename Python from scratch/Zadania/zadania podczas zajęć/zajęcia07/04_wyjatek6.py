lista_trzyelementowa = ['a', 'b', 'c']

try:
    niezadeklarowana_nazwa
    czwarty_element = lista_trzyelementowa[13]
    wynik_dzielenia_przez_zero = 13 / 0
except ZeroDivisionError:
    print('Ktoś próbował dzielić przez zero!')
except IndexError:
    print('Ktoś próbował sprawdzić wartość pod indeksem, którego nie ma!')
# except Exception as ex:
#     print('Ktoś próbował zrobić coś innego, konkretnie to:', ex)
except:  # proszę tak nie pisać
    print('Zdarzyło się coś, co mogło być przydatne. '
          'Uciszając wszystko tracimy bardzo ważną część działania Pythona!')

print('Program działa dalej.')