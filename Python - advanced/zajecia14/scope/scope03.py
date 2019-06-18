def f_zewnetrzna():
    tekst = '#2'

    def f_wewnetrzna():
        tekst = '#3'
        print(tekst)

    f_wewnetrzna()

    print(tekst)


if __name__ == '__main__':
    tekst = '#1'

    f_zewnetrzna()

    print(tekst)
