import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(Path(__file__).parent / ".env")


class ConfigBase:
    """This is the configuration base class from which the
    others are derived
    """
    SECRET_KEY = bytearray(os.getenv("SECRET_KEY"), "UTF-8")


class ConfigDevelopment(ConfigBase):
    """Get the development configuration information for the application
    """
    FLASK_DEBUG = 1
    DEBUG_TB_ENABLED = bool(int(os.getenv("DEBUG_TB_ENABLED")))
    DEBUG_TB_INTERCEPT_REDIRECTS = bool(int(os.getenv("DEBUG_TB_INTERCEPT_REDIRECTS")))


class ConfigProduction(ConfigBase):
    """Get the production configuration information for the application
    """
    FLASK_DEBUG = 0
