from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bs = Bootstrap(app)

from app.home import home_bp
app.register_blueprint(home_bp)
