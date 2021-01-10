from flask import Flask

app = Flask(__name__)

from . import intro
app.register_blueprint(intro.intro_bp)
