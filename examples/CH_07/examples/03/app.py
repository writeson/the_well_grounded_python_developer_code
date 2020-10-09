from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

visits = 0


@app.route("/")
def home():
    global visits
    now = datetime.now()
    visits += 1
    return render_template("index.html", now=now, visits=visits)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
