from flask_restful import Resource, request
from models.item import ItemModel
from schemas.item import ItemSchema
from schemas.relation import RelationSchema

from pprint import pprint
import logging

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)
relation_schema = RelationSchema()


class Item(Resource):
    def get(self, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            return item_schema.dump(item), 200
        return {'message': 'Item not found.'}, 404

    def post(self, name: str):
        data = request.get_json()
        item = item_schema.load(data)
        _id = 0

        try:
            _id = item.save_to_db()
        except:
            return {'message': 'An error occurre inserting the item.'}, 500

        parent_id = data['parent_id']
        if _id and parent_id:
            if parent_id:
                data['child_id'] = _id
            else:
                data['parent_id'] = _id

            # entity_id = EntityModel.find_id_by_name(entity_name)
            data['child'] = ItemModel.find_by_id(data['child_id'])
            data['parent'] = ItemModel.find_by_id(data['parent_id'])

            logging.warning('\nresources\nparent_id: {}\nchild_id: {}'.format(data['parent_id'], data['child_id']))
            pprint(data)
            relation = relation_schema.load(data)

            pprint(relation_schema.dump(relation))
            relation.save_to_db()
            return relation_schema.dump(relation), 201
        else:
            return item_schema.dump(item), 201

        # return item_schema.dump(item), 201


class ItemList(Resource):
    def get(self):
        return {'items': item_list_schema.dump(ItemModel.find_all())}

    def post(self):
        data = request.get_json()

        for item_data in data:
            item = item_schema.load(item_data)
            try:
                item.save_to_db()
                return {'message': 'Data posted.'}, 201
            except:
                return {'message': 'An error occurre inserting the item.'}, 500
