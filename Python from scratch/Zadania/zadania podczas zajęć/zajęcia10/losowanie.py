from random import randint, randrange, choice, choices, sample

# wybiera jedną liczbę z przedziału
print(randint(1, 49))

# wybiera jedną liczbę z przedziału, ale działa jak range()
print(randrange(1, 50, 2))  # co druga, od jedynki, do 49 włącznie

elementy = ['arbuz', 'banan', 'cytryna', 'daktyl', 'figa', 'granat']

print(choice(elementy))

print(choices(elementy, k=2))  # uwaga! elementy mogą się powtarzać

print(sample(elementy, 2))  # elementy nie będą się powtarzać

# losowanie jednej litery z wyrazu
wyraz = "Jabłko"
print(choice(wyraz))


