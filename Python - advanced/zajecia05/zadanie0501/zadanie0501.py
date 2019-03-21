from flask import Flask

app = Flask(__name__)

@app.route('/odczyt')
def odczyt_z_pliku():
    try:
        with open('baza.txt', 'r') as plik:
            dane = plik.read()
            return ('Dane w bazie to: {}'.format(dane))
    except:
        return ('Najpierw zapisz coś do bazy')

@app.route('/zapis/<dane>')
def zapis_do_pliku(dane='<dane>'):
    with open('baza.txt', 'a') as plik:
        plik.write(f'{dane}\n')
        return (f'Zapisano do bazy dane: {dane}')


if __name__ == "__main__":
    app.run()
