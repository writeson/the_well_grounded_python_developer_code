from setuptools import setup

setup(
    name='example_2',
    version='1.0.0',
    packages=['application'],
    entry_points={
        'console_scripts': [
            'example_2 = application.__main__:main'
        ]
    }
)
