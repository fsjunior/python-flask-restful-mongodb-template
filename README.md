# Python+Flask RESTful template using MongoDB
![python 3.9](https://img.shields.io/badge/python-3.9-blue)
[![build](https://img.shields.io/github/workflow/status/fsjunior/python-flask-restful-mongodb-template/build)](https://github.com/fsjunior/python-flask-restful-mongodb-template/actions?query=workflow%3Abuild)
[![Codecov](https://img.shields.io/codecov/c/gh/fsjunior/python-flask-restful-mongodb-template)](https://codecov.io/gh/fsjunior/python-flask-restful-mongodb-template)
[![maintainability](https://img.shields.io/codeclimate/maintainability/fsjunior/python-flask-restful-mongodb-template)](https://codeclimate.com/github/fsjunior/python-flask-restful-mongodb-template)
[![quality gate](https://img.shields.io/sonar/quality_gate/fsjunior_python-flask-restful-mongodb-template?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=fsjunior_python-flask-restful-mongodb-template)
![GitHub last commit](https://img.shields.io/github/last-commit/fsjunior/python-flask-restful-mongodb-template)

A simple and powerful 🐍+flask RESTful template with MongoDB.

## Features

- Bleeding edge [Python 3.9](https://docs.python.org/3.9/whatsnew/3.9.html) (although 
this template probably will work with older Python versions as well);
- [Flask](flask.palletsprojects.com) micro-framework;
- RESTful API with pagination and Swagger/ReDoc OpenAPI specification with [flask-smorest](https://flask-smorest.readthedocs.io/en/latest/);
- Schemas with [marshmallow](https://marshmallow.readthedocs.io/en/stable/);
- ODM with [mongoengine](http://mongoengine.org/);
- Migrations and seeding support with [pymongo-migrate](https://github.com/stxnext/pymongo-migrate);
- 100% code coverage tests using [pytest](https://docs.pytest.org/en/stable/)
and [pytest-cov](https://github.com/pytest-dev/pytest-cov);
- Linting with [pylint](https://github.com/PyCQA/pylint/), 
  [mypy](https://github.com/python/mypy), [black](https://github.com/psf/black) and [isort](https://pypi.org/project/isort/);
- Security analysis with [bandit](https://github.com/PyCQA/bandit);
- Dependencies and environment management [poetry](https://python-poetry.org/);
- [Pre-commit](https://github.com/pre-commit/pre-commit) hooks;
- Continuous Integration with [github actions](https://github.com/features/actions).
- Support for PaaS (Heroku);   
- API examples.


## Getting started

After cloning this repository for your project, init the `poetry` environment and install 
the project dependencies:

```console
~ $ poetry install
```

Install pre-commit hooks:

```console
~ $ pre-commit install
```

A `docker-compose.yml` file is provided with a pre-configurated MongoDB service that can
be used for **testing and development**. To run the tests, you will need to start it:

```console
~ $ docker-compose up -d
```

You will also need a `.env` file for local development and testing. You can copy the
`dotenv.test` file for this purpose.

```console
~ $ cp dotenv.test .env
```

Now you can run the tests

```console
~ $ make coverage
```

Or you can run the template in development mode

```console
~ $ make run-dev
```

Go to your browser to access the Swagger or ReDoc auto-generated docs:

```
http://127.0.0.1:8080/doc/swagger
http://127.0.0.1:8080/doc/redoc
```

### Demo

This template is up and running on http://flask-template.chico.codes 
(with POST, PUT and DELETE disabled for security reasons). 
Try it: http://flask-template.chico.codes/doc/swagger


## The template

Almost every feature here is provided by the libraries that I'm using
(e.g. pagination is provided by flask-smorest and flask-mongoengine).
So, most of the code here is just glue code and library configurations.

Files and folders structure pattern: there are specific files for 
specific resources and a `common` module/file to the that code will 
be used by different resources.

#### Structure

Explore the files and folders structure to understand the code and
what you have to change to adapt the template to your project. 
Here some basic info to help:

There are four parent folders: `migrations`, `postman`, `app` and `test`.
- The folder `migrations` have the migrations that will be executed by the
`release` command in `Procfile`.
- The `postman` folder have a [Postman](https://www.postman.com/) collection. 
- As you may have guessed, `app` contains the app files and
- `test` have all the tests and fixtures. The `test` folder structure is
mirrored from `app`, so it is easy to find where the tests are.

Inside the `app` folder, there are three sub-folders:

- `api` which contains API sub-folders `schema` (for schemas), `rest` (for RESTful views), 
`business` (for business logic) and `exceptions` (for exceptions definitions).
- `common` with common files like a settings file.
- `model` with the MongoDB collection models.

In the root directory, there are other important files as well:

A `Procfile` with web and release (to apply the migrations) targets.

The `run.py`, the entry point of the service.

A `Makefile` with the CLI commands.

The `pyproject.toml` have the entire project configuration (linting, poetry etc).

## CLI

#### Linting and coverage

This will lint and fix (if possible) the code. This will run `isort`, `pylint`, `black`,
`mypy` and `bandit`. Finally, this is also will run the coverage analysis (`pytest --cov`).

```console
~ $ make check-all
```

#### Create a migration

```console
~ $ make generate-migrations
```

The generated migration will be placed in the `migrations` folder in the root directory
and it is generated with [pymongo-migrate](https://github.com/stxnext/pymongo-migrate).
The connection string to MongoDB service used is the one present in `.env` file.

## Other configurations

This template is configured to use codecov to analyze the code coverage.
If you would like to do it too, you need to create a [codecov](https://codecov.io/)
account e associate it with your project.

## FAQ

### Why do you have a requirements.txt if you use Poetry?

The dependency management is made with Poetry, but Heroku buildpack uses the 
`requirements.txt` if you want to deploy in a PaaS. To generate the file with the poetry, run: 

```console
~ $ poetry export -f requirements.txt --output requirements.txt
``` 

### This template is not useful, as you did not use any authentication method for it

Authentication (and authorization) are normally environment dependent. It is
hard to use a library or method that will be suitable for most of the use 
cases. For this reason, I decided to not put any authentication 
(or authorization) method here. 

### Can I use this template in a production environment?

Probably, but with caution. Always do a quality analysis with tools like
[sonarcloud](sonarcloud.io) before deploying. You should also have in mind that this
template does not provide everything for a production environment. For example, the
`docker-compose.yml` provided is not suitable for a production environment.

### Why don't you create a cookiecutter template?

Besides I like cookiecutter, I believe that this seed/template is so simple and easy
to understand and customize that there is no need to create a cookiecutter template
for it.

### Can I contribute to this project?

Of course! If you would like to see a new feature, please open a new issue.

## License

Copyright (c) 2021 Francisco de Souza Júnior.

Licensed under the [MIT License](https://github.com/fsjunior/python-flask-restful-mongodb-template/blob/main/LICENSE).
