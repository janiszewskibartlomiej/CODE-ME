from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    context = {}
    liczba_str = request.args.get('liczba')

    if liczba_str is not None:
        try:
            liczba = int(liczba_str)
            context['liczba'] = liczba
        except ValueError:
            context['error'] = f'Wartość: "{liczba_str}" nie jest liczbą całkowitą'

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
