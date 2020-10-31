from flask_restful import Resource, request
from models.item import ItemModel
from models.relation import RelationModel
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
            # pprint(data)
            relation = relation_schema.load(data)

            # pprint(relation_schema.dump(relation))
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

        ids = []

        for x in data:

            pprint(x)
            
            item = ItemModel.find_by_uri(x['uri'])
            if not item:
                item_dump = {'name': x['name'], 'uri': x['uri']}
                item = item_schema.load(item_dump)
                try:
                    item.save_to_db()                
                except:
                    return {'message': 'An error occurre inserting the item.'}, 500            
            
            ids.append({'id_db': item.id, 'id_dump': x['id']})

            if x['relation_id'] == -1:
                continue
            
            base_id = item.id
            second_id = next(filter(lambda a: a['id_dump'] == x['relation_id'], ids))['id_db']
            relation = RelationModel.find_relation(base_id, second_id)
            if relation:
                continue

            is_parent = False
            is_wifehusband = False
            if x['category'] == 'Отец':
                is_parent = True
            elif x['category'] == 'Мать':
                is_parent = True
            elif x['category'] == 'Супруг':
                is_wifehusband = True
            elif x['category'] == 'Супруга':
                is_wifehusband = True
            elif x['category'] == 'Дети':
                base_id, second_id = second_id, base_id
                is_parent = True

            relation_dump = {
                'base_id': base_id,
                'second_id': second_id,
                'is_parent': is_parent,
                'is_wifehusband': is_wifehusband}
            relation = relation_schema.load(relation_dump)            

            try:
                relation.save_to_db()
            except:
                return {'message': 'An error occurre inserting the relation.'}, 500
