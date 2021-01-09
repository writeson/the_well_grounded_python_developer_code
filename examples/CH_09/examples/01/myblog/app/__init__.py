import os
from flask import Flask
from flask import send_from_directory
import logging
from logging.config import dictConfig


def create_app(environment="production"):
    """Initialize the Flask core application"""

    # configure logging prior to creating the app instance
    dictConfig(_logging_configuration(environment))

    # create the flask app instance
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f"config.Config{environment.title()}")

    if environment == "development":
        from flask_debugtoolbar import DebugToolbarExtension
        toolbar = DebugToolbarExtension()
        toolbar.init_app(app)

    # initialize plugins

    # with the app instance context register the blueprints
    with app.app_context():

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
