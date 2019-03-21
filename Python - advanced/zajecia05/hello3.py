from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    print('metoda:', request.method)
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
