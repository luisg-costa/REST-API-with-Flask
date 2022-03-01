from flask_restful import Resource
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):
    
    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404
    
    @jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "Store '{}' already exists".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500
        return store.json(), 201
    
    @jwt_required()
    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_from_db()
            except:
                return {'message': 'Cant delected {} store'.format(name)}
        return {'message': 'Store delected.'}

class StoreList(Resource):
    
    @jwt_required()
    def get(self):
        return {'stores': [store.json() for store in StoreModel.find_all()]}
    
