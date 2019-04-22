from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/strona_a')
def strona_a():
    return render_template('index3a.html')


@app.route('/strona_b')
def strona_b():
    wpis = request.args.get('wpis')
    if wpis:
        print(wpis)
    return render_template('index3b.html')


if __name__ == '__main__':
    app.run(debug=True)
