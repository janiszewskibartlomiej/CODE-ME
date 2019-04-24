from flask import Flask, render_template

app = Flask(__name__, template_folder='menu_templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logo1')
def logo1():
    return render_template('logo1.html')


@app.route('/logo2')
def logo2():
    return render_template('logo2.html')


if __name__ == '__main__':
    app.run(debug=True)
