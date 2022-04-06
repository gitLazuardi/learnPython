from main import db, app, jsonify, abort, IntegrityError, request
from main.hobby.models import Hobby

@app.route('/hobby', methods=['GET'])
def get_hobby_raw():
    hobby = db.session.execute('select * from category')
    res = {}
    for item in hobby:
        res[item.id] = {
            'id': item.id,
            'name': item.name
        }
    return jsonify(res)