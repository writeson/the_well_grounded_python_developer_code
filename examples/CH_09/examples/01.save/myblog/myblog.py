import os
from app import create_app

app = create_app(environment=os.environ["FLASK_ENV"])
app.logger.info("MyBlog is running")
