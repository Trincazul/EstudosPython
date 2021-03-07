from flask import Flask, url_for
from flask import request
from flask import json

app = Flask(__name__)

#exemplo de criação de rotas

@app.route('/')
def api_root():
    return 'Bem Vindo'

@app.route('/ola')
def api_hello():
    if 'name' in request.args:
        return 'Ola ' + request.args['name']
    else:
        return 'ola John Doe'

@app.route('/artigos')
def api_articles():
    return 'Lista de ' + url_for('api_articles')

@app.route('/artigos/<articleid>')
def api_article(articleid):
    return 'Você está lendo ' + articleid

#rotas passando request e metodos
@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"


if __name__ == '__main__':
    app.run()

