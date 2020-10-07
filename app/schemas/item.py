from ma import ma
from marshmallow import EXCLUDE
from models.item import ItemModel


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        dump_only = ("id",)
        load_instance = True
        unknown = EXCLUDE
