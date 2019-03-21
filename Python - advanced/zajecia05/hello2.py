from flask import Flask

app = Flask(__name__)   #pod app jest wszytsko chcemy zwracać


@app.route('/')   # podajemy pod jaką ścieżką będzie dostępna, route i
                    # "/" to konkretny zasób - ścieszka do zasoby
def hello():
    return 'Hello, World!' #ta funkcja musi zawsze zwracać dane - zwrot na stronę


if __name__ == "__main__":
    app.run()
