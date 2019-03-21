from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def odczyt():
    # spróbuj: http://127.0.0.1:5000?a=123&b=456

    argumenty = request.args
    for klucz, wartosc in argumenty.items():
        print(f'{klucz}: {wartosc}')
    return f'argumenty: {argumenty}'


if __name__ == "__main__":
    app.run()
