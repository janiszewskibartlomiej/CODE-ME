from flask import Flask, render_template

app = Flask(__name__, template_folder='menu_templates2')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logo1')
def logo1():
    return render_template('logo1.html')


@app.route('/logo2')
def logo2():
    return render_template('logo2.html')


@app.route('/logo3')
def logo3():
    # return render_template('logo3.html')  # wersja niepoprawna
    return render_template('logo3b.html')


if __name__ == '__main__':
    app.run(debug=True)
