from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


dependencies = [
    "wheel",
    "autopep8",
    "coverage"
],


test_dependencies = [
    'coverage',
    'pytest',
    'pytest-cov',
    'pytest-html',
    'pytest-runner',
    'pytest-sugar',
    'pytest-env',
    'pytest-flake8',
    'flake8'
]

setup(
    name="chapter_4",
    version="0.0.1",
    author="Doug Farrell",
    author_email="doug.farrell.writer@gmail.com",
    description="Example programs for Chapter 4",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/writeson/the_well_grounded_python_developer_code",
    packages=find_packages(where="chapter_4"),
    package_dir={"": "chapter_4"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    setup_requires=[
        'pytest-runner'
    ],
    install_requires=dependencies,
    tests_require=test_dependencies,
    entry_points={
        'console_scripts': [
            "example_1=chapter_4.example_1:main",
            "example_2=chapter_4.example_2:main",
            "example_3=chapter_4.example_3:main",
        ]
    }
)
