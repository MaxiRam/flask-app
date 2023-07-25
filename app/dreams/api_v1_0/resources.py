from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import DreamSchema
from ..models import Dream

dreams_v1_0_bp = Blueprint('dreams_v1_0_bp', __name__)

dream_schema = DreamSchema()

api = Api(dreams_v1_0_bp)

class DreamListResource(Resource):
    def get(self):
        dreams = Dream.get_all()
        result = dream_schema.dump(dreams, many=True)
        return result
    
    def post(self):
        data = request.get_json()
        dream_dict = dream_schema.load(data)
        dream = Dream(topic=dream_dict['topic'])
        dream.save()
        resp = dream_schema.dump(dream)
        return resp, 201

class DreamResource(Resource):
    def get(self, dream_id):
        Dream = Dream.get_by_id(dream_id)
        if dream is None:
            raise ObjectNotFound('El numero no esta registrado')
        resp = dream_schema.dump(dream)
        return resp

api.add_resource(DreamListResource, '/api/v1.0/dreams/', endpoint='dream_list_resource')
api.add_resource(DreamResource, '/api/v1.0/dreams/<int:dream_id>', endpoint='dream_resource')