from flask import Blueprint

auth_bp = Blueprint(
    "auth_bp", __name__,
    static_folder="static",
    static_url_path="/auth/static",
    template_folder="templates"
)

from . import auth
