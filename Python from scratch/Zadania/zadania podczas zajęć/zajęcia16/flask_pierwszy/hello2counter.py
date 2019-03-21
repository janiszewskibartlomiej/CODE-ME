from flask import Flask

app = Flask(__name__)
counter = 0

@app.route('/')
def hello():
    global counter
    counter += 1
    return f'Hello, World! odwiedzono: {counter} razy.'

if __name__ == "__main__":
    app.run()