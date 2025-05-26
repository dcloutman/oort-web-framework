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

## Environment Variables

Environment variables are key-value pairs used to configure application settings such as database credentials, API keys, or debug modes. For Oort, these variables are stored in a `.env` file located in the root directory of your project (the same directory as this `README.md`). The `.env` file is not included in the distribution or committed to the repository by default, ensuring that sensitive information remains confidential.

To get started, copy the provided `env-example` file to `.env` and edit it to suit your environment:

```bash
cp env-example .env
```

You should create separate `.env` files for different environments (development, QA, testing, production, etc.), each with appropriate settings. Never commit production passwords or other secrets to your code repository. The `.env` file is used by Docker Compose and other tools to load configuration values at runtime, keeping sensitive or environment-specific information separate from your source code.

### MySQL Docker Compose Configuration
Oort's Docker Compose setup allows you to control MySQL port exposure and mapping with the following environment variables in your `.env` file:

- `MYSQL_EXTERNAL_PORT`: The port on your host machine to expose MySQL (default: 3306).
- `MYSQL_INTERNAL_PORT`: The port inside the container for MySQL (default: 3306).
- `MYSQL_EXPOSE_EXTERNAL_PORT`: Set to `true` to expose MySQL externally, or `false` to disable external exposure (default: true).

If you set `MYSQL_EXPOSE_EXTERNAL_PORT=false`, MySQL will not be accessible from outside the Docker network.

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
*v0.0.1*

This version is alpha quality.

Please note that v0.0.0 is not stable and subject to change. All releases earlier than 1.0.0 will likely introduce breaking changes, so be prepared for occasional paradigm shifts when using alpha or beta versions of this meta-framework.

(c)2025 David Cloutman
Licensed under the MIT license.

