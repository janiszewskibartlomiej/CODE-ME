from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates5')


@app.route('/', methods=['get', 'post'])
def index():
    imie = request.form.get('imie')
    nazwisko = request.form.get('nazwisko')

    context = {'imie': imie, 'nazwisko': nazwisko}

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
