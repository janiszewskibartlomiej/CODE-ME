from flask import Flask

from auth import auth_bp
from tabela import tabela_bp

app = Flask(__name__)
app.secret_key = 'tajny-klucz-9523'
app.register_blueprint(auth_bp)  # tu jest zmiana
app.register_blueprint(tabela_bp)

if __name__ == '__main__':
    app.run(debug=True)
