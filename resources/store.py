from flask_restful import Resource
from models.store import WhereModel


class Where(Resource):
    def get(self, name):
        store = WhereModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if WhereModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        store = WhereModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return store.json(), 201

    def delete(self, name):
        store = WhereModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class WhereList(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(), WhereModel.query.all()))}
