from main import db, fields, ma

class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return f"<Hobby : {self.name}>"

#Hobby Schema
class HobbySchema(ma.Schema):
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)

