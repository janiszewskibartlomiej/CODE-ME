from flask import Flask

app = Flask(__name__)

dane = {'counter': 0}


@app.route('/')
def hello():
    dane['counter'] += 1
    return f'Hello, World! odwiedzono: {dane["counter"]} razy.'


if __name__ == "__main__":
    app.run()
