from typing import List
from datetime import datetime
from db import db

import logging

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # surname = db.Column(db.String(50), nullable=False)
    # fathername = db.Column(db.String(50), nullable=False)

    # born = db.Column(db.Date)
    # died = db.Column(db.Date)
    # sex = db.Column(db.Boolean, default=True)   # True - Male & False - Female

    uri = db.Column(db.String(250), unique=True, nullable=False)

    # father_id = db.Column(db.Integer)
    # mother_id = db.Column(db.Integer)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    # parents = db.relationship('RelationModel', lazy='dynamic')
    # children = db.relationship('RelationModel', lazy='dynamic')

    @classmethod
    def find_by_name(cls, name: str) -> "ItemModel":
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_uri(cls, uri: str) -> "ItemModel":
        return cls.query.filter_by(uri=uri).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "ItemModel":
        logging.warning('input _id = {}'.format(_id))
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> int:
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            return 0

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
