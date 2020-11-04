# Python+Flask RESTful template using MongoDB
![python 3.9](https://img.shields.io/badge/python-3.9-blue)
[![build](https://img.shields.io/github/workflow/status/fsjunior/python-flask-restful-mongodb-template/build)](https://github.com/fsjunior/python-flask-restful-mongodb-template/actions?query=workflow%3Abuild)
[![Codecov](https://img.shields.io/codecov/c/gh/fsjunior/python-flask-restful-mongodb-template)](https://codecov.io/gh/fsjunior/python-flask-restful-mongodb-template)
[![maintainability](https://img.shields.io/codeclimate/maintainability/fsjunior/python-flask-restful-mongodb-template)](https://codeclimate.com/github/fsjunior/python-flask-restful-mongodb-template)
[![quality gate](https://img.shields.io/sonar/quality_gate/fsjunior_python-flask-restful-mongodb-template?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=fsjunior_python-flask-restful-mongodb-template)
![GitHub last commit](https://img.shields.io/github/last-commit/fsjunior/python-flask-restful-mongodb-template)

*Documentação também disponível em [português](README.pt.md) 🇧🇷.*

A simple and powerful 🐍+flask RESTful template/seed with MongoDB. Feel free to clone this repository and use this code as you wish.

**Warning**: this project is not finished yet and some important features may still be missing. Please see the [Roadmap](#roadmap) for more details.

## What this template/seed have 

- Bleeding edge [Python 3.9](https://docs.python.org/3.9/whatsnew/3.9.html);
- [Flask](flask.palletsprojects.com) micro-framework;
- RESTful API with pagination and Swagger/ReDoc OpenAPI specification using the incredible [flask-smorest](https://flask-smorest.readthedocs.io/en/latest/);
- Schemas with [marshmallow](https://marshmallow.readthedocs.io/en/stable/);
- ODM with [mongoengine](http://mongoengine.org/);
- Testing and coverage reports with [pytest](https://docs.pytest.org/en/stable/) and [pytest-cov](https://github.com/pytest-dev/pytest-cov);
- Coverage report upload and badging with [codecov](https://codecov.io/);
- Static typing enforcement with [mypy](https://github.com/python/mypy);
- PEP8 style enforcement with [flake8](https://gitlab.com/pycqa/flake8);
- Code formatting enforcement with [black](https://github.com/psf/black);
- Import sorting with [isort](https://pypi.org/project/isort/);
- Security analysis with [bandit](https://github.com/PyCQA/bandit);
- Dependencies and environment management [poetry](https://python-poetry.org/);
- Continuous Integration with [github actions](https://github.com/features/actions).

## Roadmap

- [x] CI working;
- [x] 100% testing code coverage;
- [x] Simple restful API;
- [x] OpenAPI/Swagger/Redoc documentation.
- [x] Make project use environment variables and .env files;
- [x] Pagination;
- [x] Migrations/seeding;
- [x] Simple requests caching support
- [ ] Customized error messages;
- [ ] Some authorization method;
- [ ] CD example to a PaaS.

## Getting started

After cloning this repository for your project, init the `poetry` environment:

```shell
~ $ poetry init
```

There is a `docker-compose.yml` file with a pre-configurated MongoDB service that can 
be used for **testing and development only**. To run the tests, you will need to start it:

```shell
~ $ docker-compose up
```

You will also need a `.env` for local development and testing. You can copy the 
`dotenv.test` file for this purpose.

```shell
~ $ cp dotenv.test .env
```

### CLI

#### Run in development mode

```shell
~ $ make run-dev
```

(Don't forget the Mongo service and the .env file 😉)

#### Check all linting and tests

This will run check linting (`isort`, `flake8` and `black`), static typing check (`mypy`)
security analysis (`bandit`) and coverage tests (`pytest --cov`). 

```shell
~ $ make check-all
```

You can also run these steps separately with `check-lint`, `check-typing`, `check-security` 
and `coverage` make targets. 

To fix the lint, you can run:

```shell
~ $ make fix-lint
```

#### Create a migration

```shell
~ $ make generate-migrations
```

The generated migration will be placed in the `migrations` folder in the root directory 
and it is generated with [pymongo-migrate](https://github.com/stxnext/pymongo-migrate). 
The connection string to MongoDB service used will be the one present in `.env` file.


### Content

You need to explore the files and folders structure to understand what is going on and 
what you have to change to adapt the template to your project. Here some basic info to help:

There are two parent folders: `app` and `test`. As you may have guessed, `app` contains the 
app files and `test` have all the tests and fixtures. The `test` folder structure is 
mirrored from `app`, so it is easy to find where the tests are.

Inside the `app` folder, there are three sub-folders: 

- `api` which contains API sub-folders `schema` (for schemas), `rest` (for RESTful views)
and `query` (for queries).
- `common` with common files like a settings file.
- `model` with the MongoDB collection models.

The files and folders structure pattern that I tried to use is always create specific 
files for specific resources and create a common module/file if that code will be used by 
different resources.

In the root directory, there are other important files as well:

A `Procfile` with web and release (to apply the migrations) targets.

The `run.py`, the entry point of the service.

A `Makefile` with the CLI commands.

The `setup.cfg` for linting configuration.

## Other configurations

This template is configured to use codecov to analysis the code coverage. 
If you would like to do it too, you need to create a [codecov](https://codecov.io/) 
account e associate it with your project.

## FAQ

### Can I use this template in a production environment?

Probably, but with caution. Always do a quality analysis with tools like 
[sonarcloud](sonarcloud.io) before deploying. You should also have in mind that this 
template do not provide everything for a production environment. For example, the 
`docker-compose.yml` provided is not suitable for a production environment.

### Why don't you create a cookiecutter template?

Besides I like cookiecutter, I believe that this seed/template is so simple and easy to understand and customize that there is no need to create a cookiecutter template for it. 

### Can I contribute to this project?

Of course! If you would like to see a new feature, please open a new issue. 

## License

Created and maintened by Francisco de Souza Júnior (2020).

Licensed under the [MIT License](https://github.com/fsjunior/python-flask-restful-mongodb-template/blob/main/LICENSE).