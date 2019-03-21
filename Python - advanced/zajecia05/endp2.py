from flask import Flask

app = Flask(__name__)


@app.route('/echo/<dane>')
def echo_page(dane):
    return f'Echo: {dane}'


if __name__ == "__main__":
    app.run()
