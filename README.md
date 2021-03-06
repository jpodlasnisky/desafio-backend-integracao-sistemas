<h1 align="center"> Desafio Backend de Integração de Sistemas </h1>

<p align="center">	
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jpodlasnisky/desafio-backend-integracao-sistemas">
	
  <a href="https://www.linkedin.com/in/podlasnisky/">
    <img alt="Made by João Pedro Podlasnisky" src="https://img.shields.io/badge/made%20by-jpodlasnisky-%2304D361">
  </a>
  
  <a href="https://github.com/jpodlasnisky/desafio-backend-integracao-sistemas/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/jpodlasnisky/desafio-backend-integracao-sistemas">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
   <a href="https://github.com/jpodlasnisky/desafio-backend-integracao-sistemas/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/jpodlasnisky/desafio-backend-integracao-sistemas?style=social">
  </a>
</p> 
  
| Descriçao | Tecnologias |
|:---------:|:-----------:|
|Linguagem e framework|![python](https://img.shields.io/badge/python-3.8-blue?color=blue&label=python&logo=python) ![flask](https://img.shields.io/badge/flask-v1.1.2-blue?label=flask&logo=flask) ![wheel](https://img.shields.io/badge/wheel-yes-brightgreen)|
|Bancos de Dados|![mysql](https://img.shields.io/badge/mysql-8.0-blue?label=MySQL&logo=mysql) ![postgres](https://img.shields.io/badge/postgresql-10.0-blue?label=PostgreSQL&logo=postgresql)|
|IDE|![pycharm](https://img.shields.io/badge/pycharm-2020.2-blue?label=PyCharm&logo=pycharm)|
            
## Objetivo
<p>O objetivo deste teste é avaliar seu desempenho em desenvolver uma solução de integração entre sistemas.</p>

<p>O problema consiste em receber 1 ou mais contatos de celulares através de uma API Rest e adicioná-los ao banco de dados do cliente Macapá ou do cliente Varejão.</p>


#### Fluxo de Ações
- A API receberá um JSON via POST contendo o nome e celular :heavy_check_mark:
- O cliente deverá estar autenticado para inserir o contato na base :heavy_check_mark:
- O contato deverá ser inserido no banco de dados do cliente seguindo as regras de cada cliente :heavy_check_mark:

#### Especificações da API:
- A autenticação será através de um token JWT no Authorization Header :heavy_check_mark:
- Cada cliente tem 1 uma chave única :heavy_check_mark:
- A lista de contatos que será inserido em cada cliente está no arquivo contato.json :heavy_check_mark:

#### Especificações do Cliente Macapá:
- Banco de dados Mysql :heavy_check_mark:
- Formato do Nome é somente maiúsculas :heavy_check_mark:
- O formato de telefone segue o padrão +55 (41) 93030-6905 :heavy_check_mark:
- Em anexo está o sql de criação da tabela :heavy_check_mark:

#### Especificações do Cliente VareJão:
- Banco de dados Postgresql :heavy_check_mark:
- Formato do Nome é livre :heavy_check_mark:
- O formato de telefone segue o padrão 554130306905 :heavy_check_mark:
- Em anexo está o sql de criação da tabela :heavy_check_mark:

##### Observações
> A criação de um ambiente de testes usando Docker para simular o banco de dados do cliente é altamente recomendada. A solução poderá ser desenvolvida em Golang, Node.js ou Python. Fique livre para desenhar a solução da maneira que achar mais conveniente e supor qualquer cenário que não foi abordado nas especificações acima. 

*Não foi utilizado Docker na realização deste desafio. Considerando a incompatibilidade de se utilizar o Docker for Windows e o VMWare Workstation simultâneamente (pelo motivo de o Docker exigir a instalação do Hyper-V e o VMWare exigir a remoção do Hyper-V), optei por utilizar instâncias locais dos bancos de dados MySQL e PostgreSQL.*

## Melhorias futuras
* Reorganizar os endpoints atuais
* Habilitar os seguintes endpoints
	* POST /users/cadastra -> permite o cadastro de novos usuários
	* GET /users/<id> -> permite consulta de usuários pelo ID
	* DELETE /users/<id> -> permite a remoção de um usuário pelo ID
	* PUT /users/<id> -> permite a alteração de dados de um usuário, com base no ID
	* GET /contatos/clientes/<id> -> permite a listagem de contatos cadastrados relativos a um cliente
* Desenvolver front-end para permitir um acesso via web

## Requirements

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as dependências.

```bash
pip install -r requirements.txt
```
Atente ao fato de que há alguns problemas na compilação do mysqlclient no Windows 10. Houve a necessidade de baixar o arquivo compilado para instalação e instalar com o arquivo local, que está anexo ao repositório.

## Scripts
###### Tabela contacts no MySQL
```sql
CREATE table contacts (
	id serial PRIMARY KEY,
	nome VARCHAR ( 200 ) NOT NULL,
	celular VARCHAR ( 20 ) NOT NULL
);  
```
###### Tabela contacts no PostgreSQL
```sql
CREATE table contacts (
	id serial PRIMARY KEY,
	nome VARCHAR ( 100 ) NOT NULL,
	celular VARCHAR ( 13 ) NOT NULL
);
```
###### Models para gerenciamento de autenticação de usuários para geração do JWT
```python
class Users(db.Model):
    """ Definição da classe/tabela dos usuários e seus campos"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name
```

## Decisões ao longo do desenvolvimento
Como o desafio possuia um prazo de desenvolvimento ajustado, busquei solucioná-lo utilizando a linguagem que oferecia o menor tempo de desenvolvimento e que atendesse a necessidade. A API foi criada em Flask, framework de desenvolvimento Python. Para a gestão de usuários, à fim de permitir autenticação para criação do token JWT, criei um banco de dados auxiliar, armazenando os usuários. 
Considerei também, que o JSON que carrega os dados à serem incluídos nos bancos de dados era passado no body da requisição, ao invés de fazer upload do arquivo.

## Uso da API
### Response Codes 
#### Response Codes
```
200: Success
401: Unauthorized
404: Cannot be found
50X: Server Error
```
### Autenticação
**Você encaminha:**  username e senha no header como Basic auth.
**Você recebe:** Um `JWT-Token` que permitirá realizar outras ações.

**URL**
`/auth`

**Método**
`POST`

**Request:**
```http
POST /auth HTTP/1.1
Host: 127.0.0.1:5000
Authorization: Basic dmFyZWphbzpzZW5oYXZhcmVqYW8=
```
**Successful Response:**
```json
HTTP/1.1 200 OK
Server: Werkzeug/1.0.1 Python/3.8.3
Content-Type: application/json
Content-Length: 234
{
    "exp": "Sat, 12 Sep 2020 00:14:11 GMT",
    "message": "Validated successfully",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InZhcmVqYW8iLCJleHAiOjE1OTk4Njk2NTF9.xZ7CpqwA26xSEB4Tiw7MDNpX9V-1OoqDao06h4rxRXk"
}
```

### LoadJSON
**Você encaminha:**  O token no Header e um JSON no body da requisição.
**Você recebe:** Um `JWT-Token` que permitirá realizar outras ações.

**URL**
`/loadjson`

**Método**
`POST`

**Request:**
```http
POST /loadjson HTTP/1.1
Host: 127.0.0.1:5000
token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InZhcmVqYW8iLCJleHAiOjE1OTk4NzQ5OTJ9.XM8AxX7QrZWU8Hn84vu5oxoZpB3gWx8A6ULjFpkaaSk
Content-Type: application/json

{
    "contacts": [
        {
            "name": "Marina Rodrigues",
            "cellphone": "5541996941919"
        },
        {
            "name": "Nicolas Rodrigues",
            "cellphone": "5541954122723"
        },
        {
            "name": "Davi Lucca Rocha",
            "cellphone": "5541979210400"
        }
    ]
}
```
**Successful Response:**
```json
HTTP/1.1 201 CREATED
Server: Werkzeug/1.0.1 Python/3.8.3
Content-Type: application/json
Content-Length: 4668
{
    "data": {
        "contacts": [
            {
                "cellphone": "5541996941919",
                "name": "Marina Rodrigues"
            },
            {
                "cellphone": "5541954122723",
                "name": "Nicolas Rodrigues"
            },
            {
                "cellphone": "5541979210400",
                "name": "Davi Lucca Rocha"
            }
        ]
    },
    "message": "json successfully handled"
}
```
**BAD REQUEST**
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>400 Bad Request</title>
<h1>Bad Request</h1>
<p>Failed to decode JSON object: Expecting value: line 1 column 1 (char 0)</p>
```

### Get Users
**Você encaminha:**  Uma requisição vazia na raiz
**Você recebe:** Um JSON listando os usuários cadastrados.

**URL**
`/`

**Método**
`POST`

**Request:**
```http
GET / HTTP/1.1
Host: 127.0.0.1:5000
```
**Successful Response:**
```json
HTTP/1.1 200 OK
Server: Werkzeug/1.0.1 Python/3.8.3
Content-Type: application/json
Content-Length: 4668
{
    "data": [
        {
            "created_on": "2020-09-10T21:27:03+00:00",
            "id": 1,
            "name": "Macapá",
            "password": "pbkdf2:sha256:150000$dq4apChk$8679e392e39f71da4fb09b0a5f5a6aab07ecdb4a295f0aef8ccb6d0035413e78",
            "username": "macapa"
        },
        {
            "created_on": "2020-09-10T21:29:51+00:00",
            "id": 2,
            "name": "Varejão",
            "password": "pbkdf2:sha256:150000$2MGLv8gU$8f8387ef4b7908640741492b3185b90b7eaca341add9e4b6b5775aaf66298aea",
            "username": "varejao"
        }
    ],
    "message": "successfully fetched"
}```


