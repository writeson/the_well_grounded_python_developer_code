from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", now=datetime.now())


def main():
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
