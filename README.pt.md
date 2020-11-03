# Python+flask RESTful template com MongoDB
![python 3.9](https://img.shields.io/badge/python-3.9-blue)
![Powered by Flask](https://img.shields.io/badge/powered%20by-flask-blue)
[![build](https://img.shields.io/github/workflow/status/fsjunior/python-flask-restful-mongodb-template/build)](https://github.com/fsjunior/python-flask-restful-mongodb-template/actions?query=workflow%3Abuild)
[![Codecov](https://img.shields.io/codecov/c/gh/fsjunior/python-flask-restful-mongodb-template)](https://codecov.io/gh/fsjunior/python-flask-restful-mongodb-template)
![GitHub last commit](https://img.shields.io/github/last-commit/fsjunior/python-flask-restful-mongodb-template)
[![GitHub](https://img.shields.io/github/license/fsjunior/python-flask-restful-mongodb-template)](https://github.com/fsjunior/python-flask-restful-mongodb-template/blob/main/LICENSE)

*README also available in [english](README.md) 🇺🇸🇬🇧.*

Um template/seed simples e poderoso com 🐍+flask para aplicações RESTful usando MongoDB. 
Sinta-se a vontade para clonar esse repositório e usar esse código como você desejar. 

**Aviso**: esse projeto ainda não está terminado e algumas *features* podem estar faltando. 
Por favor, veja a seção de [Roadmap](#roadmap) para mais detalhes.


## O que esse template/seed tem 

- Novíssimo [Python 3.9](https://docs.python.org/3.9/whatsnew/3.9.html);
- [Flask](flask.palletsprojects.com) micro-framework;
- API RESTful com paginação e especificação OpenAPI com Swagger/ReDoc usando o incrível  [flask-smorest](https://flask-smorest.readthedocs.io/en/latest/);
- Esquemas com [marshmallow](https://marshmallow.readthedocs.io/en/stable/);
- ODM com [mongoengine](http://mongoengine.org/);
- Testes e relatórios de cobertura com [pytest](https://docs.pytest.org/en/stable/) e [pytest-cov](https://github.com/pytest-dev/pytest-cov);
- Upload de relatórios de cobertura e badges com [codecov](https://codecov.io/);
- Cumprimento de tipagem estática com [mypy](https://github.com/python/mypy);
- Cumprimento de estilo PEP8 com [flake8](https://gitlab.com/pycqa/flake8);
- Cumprimento de estilo de código com [black](https://github.com/psf/black);
- Ordenação de imports com [isort](https://pypi.org/project/isort/);
- Análise de segurança com [bandit](https://github.com/PyCQA/bandit);
- Gerencimento de ambientes e dependencias com [poetry](https://python-poetry.org/);
- Integração Contínua com [github actions](https://github.com/features/actions).

## Roadmap

- [x] CI funcionando;
- [x] 100% de cobertura de código pelos testes;
- [x] API restful simples;
- [x] Documentação com OpenAPI/Swagger/Redoc;
- [x] Uso de variáveis de ambiente e arquivos .env;
- [x] Paginação;
- [x] Migrações/seeding;
- [ ] Mensagens de erro customizadas;
- [ ] Algum método de autorização;
- [ ] Exemplo de deploy para um serviço PaaS.


## Primeiros passos

Depois de clonar esse respositório para seu projeto, crie um ambiente com o `poetry`:

```shell
~ $ poetry init
```

Há um arquivo `docker-compose.yml` com um serviço MongoDB pré-configurado que pode ser usado
para **teste e desenvolvimento**. Para rodar os testes, você vai precisar iniciá-lo: 

```shell
~ $ docker-compose up
```

Você também vai precisar de um arquivo `.env` para desenvolvimento local e testes.
Você pode copiar o arquivo the exemplo `dotenv.test` para esse propósito.

```shell
~ $ cp dotenv.test .env
```

### CLI

O CLI desse projeto foi feito com um arquivo Makefile.

#### Rodar no modo de desenvolvimento

```shell
~ $ make run-dev
```

(Não esqueça do serviço MongoDB e o arquivo .env 😉)

#### Checar o lint e os testes

Esse comando vai fazer a checagem de lint (`isort`, `flake8` e `black`), análise de tipagem
estática (`mypy`), análise de segurança (`bandit`) e relatórios de cobertura de código pelos
testes (`pytest --cov`). 

```shell
~ $ make check-all
```

Você também pode rodar esses passos separadamente com os targets `check-lint`, `check-typing`, `check-security` 
e `coverage`. 

Para consertar o lint, você pode rodar:

```shell
~ $ make fix-lint
```

#### Criar uma migration

```shell
~ $ make generate-migrations
```

A migration gerada vai estar localizada na pasta `migrations` no diretório raiz. 
Ela é gerada com o [pymongo-migrate](https://github.com/stxnext/pymongo-migrate).


### Conteúdo

O projeto tem duas pastas na raíz: `app` e `test`. Como você deve ter adivinhado, a pasta `app`
contém os arquivos do aplicativo enquanto a pasta `test` tem todos os testes e *fixtures*.
A estrutura da pasta `test` é espelhada da pasta `app`, assim fica mais fácil achar os testes
da aplicação.

Dentro da pasta `app`, há três outras pastas: 

- `api` que contém as coisas de api, como esquemas, visões e queries.
- `common` com os arquivos comum a todo projecto como um arquivo de configurações (`settings`).
- `model` com os modelos das coleções do MongoDB.

Explore essas pastas para entender o que está acontecendo o que você tem que modificar.

No diretório raíz, há outros arquivos importantes também:

Um arquivo `Procfile` com os targets web e release (que aplica a migration).

O arquivo `run.py`, o ponto de entrada do serviço.

O arquivo `Makefile` com os comandos CLI.

O arquivo `setup.cfg` com a configuração do lint.


## Perguntas Frequentes

### Posso usar esse projeto em um ambiente de produção?

Eu não sei. Eu posso?

### Por que você não cria um template para o cookiecutter?

Embora eu gosto do cookiecutter, eu acho que esse template é tão simples e fácil de entender que não há necessidade de se criar um template do cookiecutter pra ele.

### Posso contribuir para esse projeto?

Claro! Você pode contribuir sugerindo melhorias e fazendo Pull Requests. 😉