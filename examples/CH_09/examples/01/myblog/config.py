import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(Path(__file__).parent / ".env")


class ConfigBase:
    """This is the configuration base class from which the
    others are derived
    """
    SECRET_KEY = os.getenv("SECRET_KEY")


class ConfigDevelopment(ConfigBase):
    """Get the development configuration information for the application
    """
    DEBUG = True


class ConfigProduction(ConfigBase):
    """Get the production configuration information for the application
    """
    DEBUG = False    
