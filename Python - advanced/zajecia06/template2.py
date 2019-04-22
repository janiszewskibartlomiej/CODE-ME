from flask import Flask, render_template

app = Flask(__name__)


@app.route('/strona_a')
def strona_a():
    return render_template('index2a.html')


@app.route('/strona_b')
def strona_b():
    return render_template('index2b.html')


if __name__ == '__main__':
    app.run(debug=True)
