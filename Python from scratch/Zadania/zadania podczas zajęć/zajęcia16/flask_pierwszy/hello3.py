from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/echo/<text>')
def echo_page(text):
    return f'Echo: {text}'

if __name__ == "__main__":
    app.run()