from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World!'


@app.route('/echo')
@app.route('/echo/<text>')
def echo_page(text=None):

    text_from_url = request.args.get('text-field')

    if text:
        return f'Echo: {text}'
    elif text_from_url:
        return f'Echo z parametrów url: {text_from_url}'

    return 'coś poszło nie tak :/'


@app.route('/template/')
def template():
    return render_template('template.html')


if __name__ == '__main__':
    app.run()
