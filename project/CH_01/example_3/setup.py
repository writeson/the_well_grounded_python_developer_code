from setuptools import setup

setup(
    name='example_3',
    version='1.0.0',
    packages=['application'],
    entry_points={
        'console_scripts': [
            'example_3 = application.__main__:main'
        ]
    }
)
