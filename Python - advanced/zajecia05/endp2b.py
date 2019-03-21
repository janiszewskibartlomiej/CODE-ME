from flask import Flask

app = Flask(__name__)


@app.route('/echo/<int:liczba>')
def echo_page(liczba):
    print(type(liczba))
    return f'Podana liczba to: {liczba}'


if __name__ == "__main__":
    app.run()
