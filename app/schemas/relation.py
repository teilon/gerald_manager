from ma import ma
from marshmallow import EXCLUDE
from models.relation import RelationModel


class RelationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RelationModel
        dump_only = ("id",)
        load_instance = True
        include_fk = True
        unknown = EXCLUDE
