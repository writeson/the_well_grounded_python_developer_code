import os
import yaml
from pathlib import Path
from flask import Flask, send_from_directory
from dynaconf import FlaskDynaconf
import logging
import logging.config


def create_app():
    """Initialize the Flask app instance"""

    app = Flask(__name__)
    dynaconf = FlaskDynaconf(extensions_list=True)

    with app.app_context():

        # create a route to the favicon.ico file
        @app.route('/favicon.ico')
        def favicon():
            return send_from_directory(
                os.path.join(app.root_path, 'static'),
                'favicon.ico',
                mimetype="image/vnd.microsoft.icon"
            )

        # initialize plugins
        os.environ["ROOT_PATH_FOR_DYNACONF"] = app.root_path
        dynaconf.init_app(app)

        # turn the secret key into a bytearray
        app.config["SECRET_KEY"] = bytearray(app.config["SECRET_KEY"], "UTF-8")

        _configure_logging(app, dynaconf)

        # import the routes
        from . import intro

        # register the blueprints
        app.register_blueprint(intro.intro_bp)

        return app


def _configure_logging(app, dynaconf):
    # configure logging
    logging_config_path = Path(app.root_path).parent / "logging_config.yaml"
    with open(logging_config_path, "r") as fh:
        logging_config = yaml.safe_load(fh.read())
        logging_config["handlers"]["console"]["level"] = logging_config.get(
            dynaconf.settings["ENV"], {}).get("level", "INFO"
        )
        logging_config["loggers"][""]["level"] = logging_config.get(
            dynaconf.settings["ENV"], {}).get("level", "INFO"
        )
        logging.config.dictConfig(logging_config)
