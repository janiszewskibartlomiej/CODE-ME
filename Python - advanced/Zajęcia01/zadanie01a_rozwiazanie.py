class Zespol:
    def __init__(self, nazwa, pts, g_zdob, g_str):
        self.nazwa = nazwa
        self.pts = pts
        self.g_zdob = g_zdob
        self.g_str = g_str

    def __repr__(self):
        return self.nazwa

    def __lt__(self, other):
        if self.pts < other.pts:
            return True
        else:
            return False


if __name__ == '__main__':
    # stan tabeli na 18.02.2019
    tabela = []
    tabela.append(Zespol('Tottenham Hotspur', pts=60, g_zdob=54, g_str=25))
    tabela.append(Zespol('Manchester City', pts=65, g_zdob=74, g_str=20))
    tabela.append(Zespol('Liverpool', pts=65, g_zdob=59, g_str=15))
    tabela.append(Zespol('Manchester United', pts=51, g_zdob=52, g_str=35))

    tabela.sort()
    tabela.reverse()

    print(tabela)
