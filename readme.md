# A Flask of Cough Syrup

A Flask project made from mistakes.

## Stack

##### Common:
 - make
 - virtualenv
 - Flask

##### Development:
 - Flake 8

##### Testing:
 - Py.test
 - Flask-Testing
 - Splinter + Selenium

## Configuration

##### Environment Variables and how to setup

run `make setup-mac` to setup environment variables on **Mac OS** platform.

run `make setup-linux` to setup environment variables on **Linux** platform.

There is no Windows support yet.

Environment Variables:

`SYRUP_DATABASE_URL`: Database connection string.

`SYRUP_CONFIG`: Configuration class to be used. If this variable is not specified, `DevelopmentConfig` will be used. Look under `etc/config.py` to see available config classes.

##### Config files

 - Configurations are made through Python classes in files located under `etc/`
 - Config files are contextual, meaning that they have specific values for each environment, separated by different classes.

##### Application startup
 - This project uses [Application factory](http://flask.pocoo.org/docs/0.11/patterns/appfactories/) pattern. That means that every instance of the application is generated through a function that will configure these instances. This configurations include plugin integrations, blueprints registering, choosing different config files, etc.

## Running the project

 - `make venv`
    - to create a virtual environment


 - `make install-dev`
    - to install development dependencies


- `make run-dev`
    -  To run project in dev mode

## Requirements
Requirements specifications are separate files located under `requirements` folder.

**Important:** never paste `pip freeze` output on requirement files.

## Templating
 - The template engine is Jinja2, Flask's default.
 - All templates and macro files are `.html` files.
