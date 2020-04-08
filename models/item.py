from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    where_id = db.Column(db.Integer, db.ForeignKey('where.id'))
    store = db.relationship('WhereModel')

    def __init__(self, name, ilosc, where_id):
        self.name = name
        self.ilosc = ilosc
        self.where_id = where_id

    def json(self):
        return {'name': self.name, 'ilosc': self.ilosc}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
