from main import db, fields,ma
from main.category.models import CategorySchema

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return str({
            'id': self.id,
            'name': self.name,
        })

class MovieSchema(ma.Schema):
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    category = fields.Nested(CategorySchema)
