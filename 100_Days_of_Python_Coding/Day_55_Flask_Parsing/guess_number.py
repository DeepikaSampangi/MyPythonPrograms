from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/user/<name>")
def greet(name):
    return "Hello "+name


if __name__ == "__main__":
    app.run()
