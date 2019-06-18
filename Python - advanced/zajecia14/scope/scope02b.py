def drukuj():
    print(tekst)  # to nie zadziała!
    tekst = 'Complex is better than complicated.'
    print(tekst)


if __name__ == '__main__':
    tekst = 'Simple is better than complex.'
    drukuj()
