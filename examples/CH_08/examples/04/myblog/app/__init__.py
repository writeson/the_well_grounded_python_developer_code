from flask import Flask

app = Flask(__name__)

from app.home import home_bp
app.register_blueprint(home_bp)
