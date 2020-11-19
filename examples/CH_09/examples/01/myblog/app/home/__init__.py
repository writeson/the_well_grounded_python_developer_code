from flask import Blueprint

home_bp = Blueprint('home_bp', __name__,
               static_folder="static",
               static_url_path="/home/static",
               template_folder="templates"
               )

from app.home import home
