from datetime import datetime
from db import db

import logging


class RelationModel(db.Model):
    __tablename__ = 'relations'

    id = db.Column(db.Integer, primary_key=True)

    parent_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    parent = db.relationship('ItemModel', foreign_keys=parent_id)
    child_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    child = db.relationship('ItemModel', foreign_keys=child_id)

    @classmethod
    def find_parents(cls, person_id):
        parents = db.session.filter(cls.child_id == person_id).all()
        # return parents
        return [item.parent for item in parents]

    @classmethod
    def find_children(cls, person_id):
        children = db.session.filter(cls.parent_id == person_id).all()
        # return children
        return [item.child for item in children]

    def save_to_db(self):
        # check = (self.parent_id != self.child_id)
        logging.warning('\nmodels\nparent_id: {}\nchild_id: {}'.format(self.parent_id, self.child_id))
        logging.warning('\nmodels\nparent: {}\nchild: {}'.format(self.parent, self.child))

        if True:
            db.session.add(self)
            db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
