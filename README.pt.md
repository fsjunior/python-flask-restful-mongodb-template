# Python+Flask RESTful template com MongoDB
![python 3.9](https://img.shields.io/badge/python-3.9-blue)
[![build](https://img.shields.io/github/workflow/status/fsjunior/python-flask-restful-mongodb-template/build)](https://github.com/fsjunior/python-flask-restful-mongodb-template/actions?query=workflow%3Abuild)
[![Codecov](https://img.shields.io/codecov/c/gh/fsjunior/python-flask-restful-mongodb-template)](https://codecov.io/gh/fsjunior/python-flask-restful-mongodb-template)
[![maintainability](https://img.shields.io/codeclimate/maintainability/fsjunior/python-flask-restful-mongodb-template)](https://codeclimate.com/github/fsjunior/python-flask-restful-mongodb-template)
[![quality gate](https://img.shields.io/sonar/quality_gate/fsjunior_python-flask-restful-mongodb-template?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=fsjunior_python-flask-restful-mongodb-template)
![GitHub last commit](https://img.shields.io/github/last-commit/fsjunior/python-flask-restful-mongodb-template)

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
- Linting com [flake8](https://gitlab.com/pycqa/flake8), 
[black](https://github.com/psf/black) e [isort](https://pypi.org/project/isort/);
- Análise de segurança com [bandit](https://github.com/PyCQA/bandit);
- Gerencimento de ambientes e dependencias com [poetry](https://python-poetry.org/);
- Integração Contínua com [github actions](https://github.com/features/actions).

## Roadmap

- [x] CI funcionando;
- [x] 100% de cobertura de código pelos testes;
- [x] API restful simples;
- [x] Documentação com OpenAPI/Swagger/ReDoc;
- [x] Uso de variáveis de ambiente e arquivos .env;
- [x] Paginação;
- [x] Migrações/seeding;
- [x] Suporte a cache;
- [x] Mensagens de erro customizadas;
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

Agora você pode rodar os testes:

```shell
~ $ make coverage
```

Ou rodar o template no modo de desenvolvimento:

```shell
~ $ make run-dev
```

No seu navegador você pode acessar a documentação Swagger ou ReDoc:

```
http://127.0.0.1:8080/doc/swagger
http://127.0.0.1:8080/doc/redoc
```

### O template

#### Filosofia

Eu evitei criar minhas próprias soluções (aka reinventar a roda) nesse template para 
deixá-lo o mais simples possível. Praticamente todas as *features* aqui são fornecidas 
pelas bibliotecas usadas (por exemplo: a páginação já é fornecida pelas bibliotecas 
flask-smorest e flask-mongoengine).

O padrão de projeto que eu tentei usar aqui é sempre criar arquivos e módulos específicos 
para recursos específicos e criar um arquivo/módulo `common` para códigos que serão usados
por diferentes recursos.

#### Estrutura

Explore essas pastas para entender o que está acontecendo o que você tem que modificar para
adaptar o template para seu projeto. Aqui uma breve explicação para ajudar:

O projeto tem duas pastas na raíz: `app` e `test`. Como você deve ter adivinhado, a pasta `app`
contém os arquivos do aplicativo enquanto a pasta `test` tem todos os testes e *fixtures*.
A estrutura da pasta `test` é espelhada da pasta `app`, assim fica mais fácil achar os testes
da aplicação.

Dentro da pasta `app`, há três outras pastas: 

- `api` que contém as outras sub-pastas de API `schema`(para esquemas), `rest` (para visões 
RESTful) e `query` (para queries no banco).
- `common` com os arquivos comum a todo projecto como um arquivo de configurações (`settings`).
- `model` com os modelos das coleções do MongoDB.

No diretório raíz, há outros arquivos importantes também:

Um arquivo `Procfile` com os targets web e release (que aplica a migration).

O arquivo `run.py`, o ponto de entrada do serviço.

O arquivo `Makefile` com os comandos CLI.

O arquivo `setup.cfg` com a configuração do lint.

## CLI

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
A string de conexão usada para se conectar ao MongoDB será a do arquivo `.env`.

## Outras configurações

Esse template está configurado para usar o codecov para fazer análises de cobertura de 
código. Se você quer ativar isso também em seu projeto, vai precisar criar uma conta
 em [codecov](https://codecov.io/) e associar ao seu projeto.

## Perguntas Frequentes

### Posso usar esse projeto em um ambiente de produção?

Provavelmente, mas com precauções. Você sempre deve fazer uma análise de qualidade de código
com ferramentas como o sonarcloud antes de fazer um deploy em um ambiente de produção. 
Você deve ter em mente também que nem tudo que é fornecido nesse template é adequado para
um ambiente de produção. Por exemplo, o arquivo `docker-compose.yml` fornecido não 
deveria ser usado nesse ambiente.

### Por que você não cria um template para o cookiecutter?

Embora eu gosto do cookiecutter, eu acho que esse template é tão simples e fácil de entender que não há necessidade de se criar um template do cookiecutter pra ele.

### Posso contribuir para esse projeto?

Claro! Se você gostaria de ver uma nova feature, abra uma nova issue.

## Licença

Criado e mantido por Francisco de Souza Júnior (2020).

Licenciado sob a [Licença MIT](https://github.com/fsjunior/python-flask-restful-mongodb-template/blob/main/LICENSE).