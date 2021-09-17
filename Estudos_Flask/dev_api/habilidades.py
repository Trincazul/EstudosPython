from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'PHP', 'Flask', 'Django']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades