from flask import Flask

app = Flask(__name__)

from app.intro import intro_bp
app.register_blueprint(intro_bp)
