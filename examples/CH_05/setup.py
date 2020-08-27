from setuptools import setup, find_packages

setup(
    author="Doug Farrell",
    description="Example programs for The Well-Grounded Python Developer chapter 5",
    name="examples",
    version="0.1.0dev",
    packages=find_packages(),
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
    long_description=open("README.md").read(),
    install_requires=[
        "arcade==2.3.14",
    ],
    entry_points={
        "console_scripts": [
            "example_01 = examples.01:main",
            "example_02 = examples.02:main",
            "example_03 = examples.03:main",
            "example_04 = examples.04:main",
            "example_05 = examples.05:main",
            "example_06 = examples.06:main",
            "example_07 = examples.07:main",
        ]
    }
)
