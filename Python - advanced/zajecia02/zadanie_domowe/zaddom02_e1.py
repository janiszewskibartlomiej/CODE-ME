# Bartłomiej Janiszewski

from random import sample

class TaliaKart:
    def __init__(self):

        self._karty = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠', '2♣', '3♣', '4♣',
                       '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥',
                       '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦',
                       'J♦', 'Q♦', 'K♦', 'A♦']

    def __next__(self):

        if self._karty == []:
            raise StopIteration

        cart = sample(self._karty, k=1)

        self._karty.remove(cart[0])

        return self._karty

    def __iter__(self):
        return self


if __name__ == '__main__':
    # tutaj można pisać dowolny kod, nie wpływa to na testy
    a1 = TaliaKart()
    print(list(a1))
    pass

