from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates0601')


@app.route('/')
def wprowadz():
    return render_template('wprowadz.html')


@app.route('/wynik')
def wynik():
    a = request.args.get('a', None)
    b = request.args.get('b', None)

    if a and b:
        wynik = int(a) * int(b)
        return render_template('wynik.html', a=a, b=b, wynik=wynik)

    return 'jedna z liczb nie została podana'


if __name__ == '__main__':
    app.run(debug=True)
