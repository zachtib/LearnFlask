# LearnFlask

## A Sandbox for learning the Flask web framework for Python

An example of this application is live at: https://zachtib-flaskapp.herokuapp.com/

## Starting a Flask application the "right way" (WIP)

 1. Install Python 3 if it is not provided by your operating system.
 2. Create a Python virtual environment to contain your project.

    `python3 -m venv .env`

 3. Enter the virtual environment you created (command will be different on Windows using cmd.exe)
    * Mac/Linux: `source .env/bin/activate`
    * Windows: `source .env/Scripts/activate`
 4. Install Flask in the virtual environment: `pip install Flask`
 5. Freeze the project requirements: `pip freeze > requirements.txt`