from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#Lista de dados
desenvolvedores = [
    {'name':'Endriw','habilidades':['Python', 'Flask']},
    {'name':'Villa','habilidades':['Python', 'Django']}
    
]

# devolve um desenvolvedor pelo ID, tambem altera e deleta um decsenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 'mensagem':'desenvolvedor de id não existe'}           
        except Exception:
            response = {'status':'erro', 'mensagem':'Procure o dev da api'}
        return jsonify(response)
 
# método de alteração de resultado
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

#método de deletar, selecionando pela id pop() 
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Mensagem':'Registro excluido com sucesso','status':'excluido'})

# Lista todos os desenvolvedores e inclui um novo
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso','mensagem':'Registro inserido com sucesso'})

#faz uma listagem de todos os dados registrados
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
