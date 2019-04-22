from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates4')


@app.route('/')
def index():
    dane_z_formularza = request.args.get('wpis')

    if dane_z_formularza:
        print(dane_z_formularza)

    return render_template('index.html', dane_do_szablonu=dane_z_formularza)


if __name__ == '__main__':
    app.run(debug=True)
