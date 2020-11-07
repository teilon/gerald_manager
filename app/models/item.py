from typing import List
from datetime import datetime
from db import db

import logging

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    born = db.Column(db.String(8), nullable=True)
    died = db.Column(db.String(8), nullable=True)
    sex = db.Column(db.String(8), nullable=True)

    uri = db.Column(db.String(250), unique=True, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def find_by_name(cls, name: str) -> "ItemModel":
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_uri(cls, uri: str) -> "ItemModel":
        if not uri:
            return cls.query.filter_by(uri=uri).first()
        return None

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
