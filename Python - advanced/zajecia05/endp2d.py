from flask import Flask

app = Flask(__name__)

lista = ['Ambroży', 'Barnaba', 'Celina', 'Danuta', 'Eligiusz', 'Felicja']


@app.route('/osoby/<int:indeks>')
def odczyt_z_listy(indeks):
    try:
        osoba = lista[indeks]
        return f'Osoba pod indeksem {indeks} to {osoba}'
    except IndexError:
        return f'Nie ma indeksu {indeks} w liście'


if __name__ == "__main__":
    app.run()
