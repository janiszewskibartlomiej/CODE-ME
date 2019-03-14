class Szkatulka:
    def __init__(self, sekret):
        self.sekret = sekret

    def __enter__(self):
        return self

    def __exit__(self, *args):
        del self.sekret


with Szkatulka('hasło') as s:
    print(s)
    print(s.sekret)

print(s)
# print(s.sekret)
