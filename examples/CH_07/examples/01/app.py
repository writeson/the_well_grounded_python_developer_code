from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


def main():
    app.run()


if __name__ == "__main__":
    app.run()
