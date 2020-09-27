from setuptools import setup, find_packages

setup(
    author="Doug Farrell",
    description="Example programs for The Well-Grounded Python Developer chapter 7",
    name="examples",
    version="0.1.0.dev0",
    packages=find_packages(),
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
    long_description=open("README.md").read(),
    install_requires=[
        "flask==1.1.2",
    ],
    # entry_points={
    #     "console_scripts": [
    #         "example_01 = examples.01:main",
    #         "example_02 = examples.02:main",
    #         "example_03 = examples.03:main",
    #     ]
    # }
)
