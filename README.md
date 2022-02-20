# Sky App

## Setup

Creating the virtual environment:

```
python3 -m venv env
```

Activating the virtual environment:

```
source env/bin/activate
```

Installing the modules in the requirements file:

```
pip install -r requirements.txt
```

## Starting Server

```
export FLASK_APP=sky-app
flask run
```

## Running Selenium Functional Test

```
python selenium-test.py
```