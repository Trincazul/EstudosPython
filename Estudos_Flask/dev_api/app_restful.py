from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app) 

desenvolvedores = [
    {'id':0,'name':'Endriw','habilidades':['Python', 'Flask']},
    {'id':1,'name':'Villa','habilidades':['Python', 'Django']}
]

# devolve um desenvolvedor pelo ID, tambem altera e deleta um desenvolvedor, com classe restful
class Desenvolvedor(Resource):

    # método de chamada de api
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 'mensagem':'desenvolvedor de id não existe'}           
        except Exception:
            response = {'status':'erro', 'mensagem':'Procure o dev da api'}
        return response

    # método de alteração de resultado
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    # método de deletar usuario
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'Mensagem':'Registro excluido com sucesso','status':'excluido'}

# Foi criada uma nova classe para uma nova rota adicionada em baixo
class ListaDesenvolvedores(Resource):

    #retorna todos os cadastros no /dev/
    def get(self):
        return desenvolvedores

    #adiciona um novo usuario na rota /dev/
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
# Rota em Habilidades.py
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)