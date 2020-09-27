from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


def run():
    app.run()


if __name__ == "__main__":
    app.run()
