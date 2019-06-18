def f_zewnetrzna():
    tekst = '#2'

    def f_wewnetrzna():
        tekst = '#3'

        def f_wewnetrzna_wewnetrzna():
            nonlocal tekst
            tekst = '#4'
            print(tekst)

        f_wewnetrzna_wewnetrzna()

        print(tekst)

    f_wewnetrzna()

    print(tekst)


if __name__ == '__main__':
    tekst = '#1'

    f_zewnetrzna()

    print(tekst)
