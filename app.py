from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World!:)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def display_in_fahrenheit(celsius=""):
    """Takes temperature in Celsius and displays it in Fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"Input celsius: {celsius}\nOutput Fahrenheit: {fahrenheit}"


if __name__ == '__main__':
    app.run()
