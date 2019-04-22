from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates4')


@app.route('/')
def index():
    imie = request.args.get('imie', '')  # jeśli nie ma takiego klucza, daj pusty string
    nazwisko = request.args.get('nazwisko', '')

    context = {'imie': imie, 'nazwisko': nazwisko}

    return render_template('index2.html', **context)
    # return render_template('index2.html', imie=imie, nazwisko=nazwisko)


if __name__ == '__main__':
    app.run(debug=True)
