import os
from app import create_app

app = create_app(os.environ["FLASK_ENV"])
app.logger.info("MyBlog is running")
