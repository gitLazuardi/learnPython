from main import db, app, jsonify, abort, IntegrityError, request
from main.user.models import User, UserSchema
from main.hobby.models import Hobby

singular = UserSchema()
plural = UserSchema(many=True)

@app.route('/users', methods=['GET'])
def all_user():
    all_user = User.query.all()
    result = plural.dump(all_user)
    return jsonify({'data' : result})

@app.route('/users/<id>', methods = ['GET'])
def get_user_by_id(id):
    get_user = User.query.get(id)
    user = singular.dump(get_user)
    return jsonify({"data": user})

@app.route('/users', methods=['POST'])
def add_user():
    name = request.json['name']
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()

    return singular.jsonify(new_user)

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    name = request.json['name']
    user.name = name
    db.session.commit()
    return singular.jsonify(user)

@app.route('/users/<id>', methods = ['DELETE'])
def delete_user_by_id(id):
    get_user = User.query.get(id)
    db.session.delete(get_user)
    db.session.commit()
    return ("",204)

@app.route('/addhobbybyname/<user>/<hobby>', methods=['GET'])
def addHobbyToUser(user, hobby):
    user1 = User.query.filter_by(name=user).first()
    hobby1 = Hobby.query.filter_by(name=hobby).first()
    user1.user_hobbies.append(hobby1)
    db.session.commit()
    result = singular.dump(user1)
    return jsonify(result)
