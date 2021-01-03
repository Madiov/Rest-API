from flask_jwt import jwt_required , JWT
from flask_restful import Resource, reqparse
from Model.item import ItemModel



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='this field cannot be left blank!')

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {'message': 'item not found'}, 404

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'message': 'item already exists'}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        item.save_to_db()
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_by_name()
        return {'message': 'item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']

        else:
            item = ItemModel(name, data['price'])

        item.save_to_db()
        return item.json(), 201


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
