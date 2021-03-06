from setuptools import setup, find_packages

setup(
    author="Doug Farrell",
    author_email="doug.farrell@somewhere.com",
    url="https://github.com/writeson/the_well_grounded_python_developer_code/tree/integration/examples/CH_08",
    description="Example programs for The Well-Grounded Python Developer chapter 8",
    name="examples",
    version="0.1.0.dev0",
    packages=find_packages(),
    include_package_data=True,
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
    long_description=open("README.md").read(),
    python_requires=">=3.8.0",
    install_requires=[
        "flask==1.1.2",
        "flask-bootstrap4==4.0.2",
        "gunicorn==20.0.4",
        "waitress==1.4.4"
    ],
)
