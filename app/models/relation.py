from datetime import datetime
from db import db

import logging


class RelationModel(db.Model):
    __tablename__ = 'relations'

    id = db.Column(db.Integer, primary_key=True)

    # parent_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    # parent = db.relationship('ItemModel', foreign_keys=parent_id)
    # child_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    # child = db.relationship('ItemModel', foreign_keys=child_id)

    base_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    base = db.relationship('ItemModel', foreign_keys=base_id)
    second_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    second = db.relationship('ItemModel', foreign_keys=second_id)

    is_parent = db.Column(db.Boolean, default=False)
    is_wifehusband = db.Column(db.Boolean, default=False)

    @classmethod
    def find_relation(cls, base_id, second_id):
        result = cls.query.filter_by(base_id=base_id, second_id=second_id).first()
        if not result:
            result = cls.query.filter_by(base_id=second_id, second_id=base_id).first()
        return result

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
