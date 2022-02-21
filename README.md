# Sky App

For this task I have created a web server using Flask. The initial endpoint that the user is required to go to is /form. 
This page displays a simple form for the user to enter their name into. On submission of the form, the user is redirected to the /success endpoint. The /success endpoint displays a thank you message containing the name entered into the form.

The test that I have created is a Selenium functional test. It goes through the journey created with the Flask web server, and ensures each part runs correctly, without returning errors.

## Setup

Creating the virtual environment:

```
python3 -m venv env
```

Activating the virtual environment:

```
source env/bin/activate
```

Installing the modules from the requirements file:

```
pip install -r requirements.txt
```

## Starting Server

```
export FLASK_APP=sky-app
flask run
```

## Running Selenium Functional Test

NOTE: Chrome is a requirement for the Selenium test to run

```
python selenium-test.py
```