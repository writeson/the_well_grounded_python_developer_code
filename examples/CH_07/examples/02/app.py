from pathlib import Path
from flask import Flask, render_template

template_path = Path(".") / "templates"
app = Flask(__name__, template_folder=template_path)


@app.route("/")
def home():
    return render_template("index.html")


def run():
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
