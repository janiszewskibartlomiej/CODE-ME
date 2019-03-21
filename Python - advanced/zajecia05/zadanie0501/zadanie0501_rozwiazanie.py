from flask import Flask

app = Flask(__name__)


@app.route('/odczyt')
def odczyt_z_pliku():
    try:
        with open('baza.txt') as f:
            dane = f.read()
            return f'Dane w bazie to: "{dane}"'
    except FileNotFoundError:
        return 'Najpierw zapisz coś do bazy!'


@app.route('/zapis/<dane>')
def zapis_do_pliku(dane):
    with open('baza.txt', mode='w') as f:
        f.write(dane)
        return f'Zapisano do bazy dane: "{dane}"'


if __name__ == "__main__":
    app.run()
