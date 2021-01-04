# Chapter 9 Example Programs

This directory contains the Chapter 8 examples from the book and scripts to install and run those examples.

## Installation

You will need a Python virtual environment to run the programs so that any modules installed by the setup won't interfere with your system Python. The instructions here depend on having the `pyenv` utility installed on your system. To activate a Python virtual environment in this directory take the following steps:

```console
$ cd CH_07
$ pyenv local 3.8.0
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install --upgrade pip
```

Once you have a local Python virtual environment activated your command prompt should be prefixed with `(.venv)`. This indicates the Python system in the current directory is active and ready to run.

To install any necessary modules for this chapter run the setup.py script with the following command line:

```console
python setup.py install
```

The command will pip install any modules necessary to run the example programs in the chapter and create shortcuts to run the example programs.

## Example Programs

To run the example programs just enter the command line shortcut shown in the list below. The list below shows the shortcut command and a brief description of what the command does.

* Example 01 further improves the application structure, adds the Flask Debug Toolbar, improved logging and external configuration information
* Example 02 modifies adds user login to the application without database support