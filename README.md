# Oort: a Python Meta-Framework for Web Applications
Oort is a meta-framework that builds on top of the highly successful Flask framework to create a more robust, object-oriented toolkit for developers who want to build extensible and maintainable web applications in Python with ease.

At its core, Oort utilizes controller objects via the mature FlaskClassful library. Oort provides out-of-the-box scripting to autoload controller classes for FlaskClassful, allowing developers to launch new controller classes without the overhead of modifying core framework files, such as app.py. Launching a new endpoint should be as simple as writing a class with the correct naming convention and saving it in the correct directory.

## Setup
When running for the first time, you will need to install and execute the virtual environment. Exectute the following commands from this directory:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Development Server
You should only run the server in its virtual environment. The virtual environment is started from this directory with the command:

```bash
virtualenv venv/bin/activate
```

This will amend your PATH environment variable to use the locally installed `python`, `pip`, and Python packages, rather than the globally installed versions.

To run the server in development mode, use the `run-dev.sh` script.

To exit the virtual environment, issue the `deactivate` command.

```bash
deactivate
```

## Controllers
Controllers are at the core of Oort. They create application end-points and provide object methods to handle each of the HTTP request methods (GET, POST, PUT, DELETE, etc.) by leveraging the capabilities of the Flask Classful library.

Controllers reside in the `controllers` directory. The module initiation (__init__.py) will automatically detect any file with a name matching the pattern `\*Controller.py` and then register them with the Flask application. No intervention from the developer is required to register a new controller with the Flask application.

## Version info:
v0.0.0

(c)2023 David Cloutman
Licensed under the MIT license.
