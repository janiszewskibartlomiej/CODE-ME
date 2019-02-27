#https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes
#bardzo ważne ! wiemy co mają dane protokoły w sobie!

from iter02 import ParzysteLiczby

p_licz = ParzysteLiczby()

# klasy ParzysteLiczby można teraz użyć wszędzie, gdzie przyjmowany jest obiekt Iterable
print(list(p_licz))


# Tu już nic nie ma!
print(list(p_licz))
