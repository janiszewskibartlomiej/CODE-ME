from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def wprowadz():

    return render_template('wprowadz.html')

list = []

@app.route('/wynik', methods=['post'])
def wynik():
    liczba1 = int(request.form.get('lp1'))
    liczba2 = int(request.form.get('lp2'))
    wynik = liczba1 * liczba2
    historia ={'pierwsza_liczba':liczba1, 'druga_liczba': liczba2, 'wynik_wyswietlany': wynik}

    list_z_historii =[x for x in historia.values()]
    list.append(list_z_historii)

    return render_template('wynik.html', **historia, lista =list)


if __name__ == '__main__':
    app.run(debug=True)
