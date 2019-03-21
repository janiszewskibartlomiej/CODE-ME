from flask import Flask,request

app = Flask(__name__)


@app.route('/odczyt')
def odczyt_z_pliku():
    try:
        with open('baza.txt') as f:
            dane = f.read()
            return f'Dane w bazie to: "{dane}"'
    except FileNotFoundError:
        return 'Najpierw zapisz coś do bazy!'


@app.route('/zapis')
def zapis_do_pliku():
    dane = request.args.get('dane')
    if dane is None:
         return 'Brak danych do zapisu'
    else:

        with open('baza.txt', mode='a') as f:
            f.write(f'{dane}\n')
            return f'Zapisano do bazy dane: "{dane}"'


if __name__ == "__main__":
    app.run()
