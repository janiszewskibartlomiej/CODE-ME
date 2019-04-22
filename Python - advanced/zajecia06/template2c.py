from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/strona_a')
def strona_a():
    return render_template('index2a.html')


@app.route('/strona_b')
def strona_b():
    return render_template('index2b.html')


@app.route('/inna_strona_b')
def inna_strona_b():
    print('UWAGA! ktoś wszedł na "inną" stronę b')
    return redirect('/strona_b')  # w logach można znaleźć 302 redirect


if __name__ == '__main__':
    app.run(debug=True)
