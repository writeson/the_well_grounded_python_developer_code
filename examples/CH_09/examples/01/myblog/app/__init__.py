from flask import Flask
from flask_bootstrap import Bootstrap


# global instances
bs = Bootstrap()


def create_app():
    """Initialize the Flask core application"""

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # initialize the plugins
    bs.init_app(app)

    with app.app_context():
        from . import home
        app.register_blueprint(home.home_bp)

        return app
