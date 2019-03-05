from random import sample

karty = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠', '2♣', '3♣', '4♣',
         '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥',
         '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦',
         'J♦', 'Q♦', 'K♦', 'A♦']
print(len(karty))
cart = sample(karty, k=1)

print(type(cart))
for symbol in karty:
    print( symbol, end='')
    if cart == symbol:
        karty.remove(cart[0])

#print(karty)

print('\n', cart)
print(len(karty))
print(karty)
print(cart[0] in karty)
print(len(karty))