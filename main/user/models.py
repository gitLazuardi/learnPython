from main import db, ma, fields
from main.hobby.models import Hobby, HobbySchema

user_hobby = db.Table('user_hobby',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('hobby_id', db.Integer, db.ForeignKey('hobby.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    user_hobbies = db.relationship('Hobby', secondary=user_hobby, backref='liked_by')

    def __repr__(self):
        return f'<User : {self.name}>'

class UserSchema(ma.Schema):
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    user_hobbies = fields.Nested(HobbySchema, many=True)