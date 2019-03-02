from random import sample

karty = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠', '2♣', '3♣', '4♣',
         '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥',
         '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦',
         'J♦', 'Q♦', 'K♦', 'A♦']

cart = sample(karty, k=1)

for index, symbol in enumerate(karty):
    print('[i:', index, 'k:', symbol,']', end='')
    if symbol == cart:
        karty.remove(karty[index])

#print(karty)

print('\n', cart)
print()
print(karty)
print(cart in karty)
