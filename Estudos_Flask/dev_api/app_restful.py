from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app) 

desenvolvedores = [
    {'id':0,'name':'Endriw','habilidades':['Python', 'Flask']},
    {'id':1,'name':'Villa','habilidades':['Python', 'Django']}
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 'mensagem':'desenvolvedor de id não existe'}           
        except Exception:
            response = {'status':'erro', 'mensagem':'Procure o dev da api'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'Mensagem':'Registro excluido com sucesso','status':'excluido'}

api.add_resource(Desenvolvedor, '/dev/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)