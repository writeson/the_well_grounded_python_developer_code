import os
from flask import Flask, send_from_directory
from logging.config import dictConfig


def create_app(environment="production"):
    """Initialize the Flask app instance"""

    # configure logging prior to creating the app instance
    dictConfig(_logging_configuration(environment))

    app = Flask(__name__)
    app.config.from_object(f"config.Config{environment.title()}")

    if environment == "development":
        from flask_debugtoolbar import DebugToolbarExtension
        toolbar = DebugToolbarExtension()
        toolbar.init_app(app)

    with app.app_context():

        # create a route to the favicon.ico file
        @app.route('/favicon.ico')
        def favicon():
            return send_from_directory(
                os.path.join(app.root_path, 'static'),
                'favicon.ico',
                mimetype="image/vnd.microsoft.icon"
            )

        # import the routes
        from . import intro

        # register the blueprints
        app.register_blueprint(intro.intro_bp)

        return app


def _logging_configuration(environment):
    logging_level = "DEBUG" if environment == "development" else "INFO"
    return {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            },
            "access": {
                "format": "%(message)s",
            }
        },
        "handlers": {
            "console": {
                "level": logging_level,
                "class": "logging.StreamHandler",
                "formatter": "default",
                "stream": "ext://sys.stdout",
            }
        },
        "loggers": {
            "": {
                "handlers": ["console"],
                "level": logging_level,
                "propagate": False
            }
        }
    }
