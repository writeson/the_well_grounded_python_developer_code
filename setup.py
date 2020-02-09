from setuptools import setup, find_packages

setup(
    author="Doug Farrell",
    description="This project contains all the example programs for the book",
    name="project",
    version="0.1.0dev",
    packages=find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires=[
        "Flask==1.1.1",
        "SQLAlchemy==1.3.13", 
        "SQLAlchemy-Utils==0.36.1",
        "Flask-SQLAlchemy==2.4.1",
        "marshmallow==3.3.0",
        "marshmallow-sqlalchemy==0.21.0",
        "connexion==2.5.1",
        "python-dateutil==2.8.1",
        "python-dotenv==0.10.5"
    ],
)
