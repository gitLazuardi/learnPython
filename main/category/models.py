from main import db,fields,ma
#ONE TO MANY
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    movies = db.relationship('Movie', backref='category')

    def __repr__(self):
        return f"<Category : {self.name}>"

class CategorySchema(ma.Schema):
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)