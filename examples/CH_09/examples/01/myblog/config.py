import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(Path(__file__).parent / ".env")


class Config:
    """Get the configuration information for the application
    """
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY")
