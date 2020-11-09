from flask_restful import Resource, request

class Home(Resource):
    def get(self):
        return 'I`am Gerald!'