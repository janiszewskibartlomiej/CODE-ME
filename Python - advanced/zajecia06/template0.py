from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    html = '''
<h1>Strona tytułowa</h1>
<p>Witaj na stronie!</p>
<p>XXXXXXX</p>
    '''
    return html


if __name__ == '__main__':
    app.run()
