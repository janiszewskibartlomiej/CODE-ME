from flask import Flask

app = Flask(__name__)

lista = ['Ambroży', 'Barnaba', 'Celina', 'Danuta', 'Eligiusz', 'Felicja']


@app.route('/osoby/<int:indeks>')
def odczyt_z_listy(indeks):
    osoba = lista[indeks]
    return f'Osoba pod numerem {indeks} to {osoba}'


if __name__ == "__main__":
    app.run()
