from main import db, app, jsonify, abort, IntegrityError, request
from main.note.models import Note

@app.route('/notes', methods=['GET'])
def index():
    notes = Note.query.all()
    res = {}
    for item in notes:
        res[item.id] = {
            'title': item.title,
            'author': item.author,
            'detail': item.detail,
        }
    return jsonify(res)

@app.route('/notes/<id>', methods = ['GET'])
def get_note_by_id(id):
    note = Note.query.filter_by(id=id).first()
    if not note:
        abort(404)
    res = {
        'title': note.title,
        'author': note.author,
        'detail': note.detail,
    }
    return jsonify(res)

@app.route('/notes', methods=['POST'])
def add_notes():
    title = request.json['title']
    detail = request.json['detail']
    author = request.json['author']
    try:
        new_notes = Note(title, detail, author)
        db.session.add(new_notes)
        db.session.commit()
    except IntegrityError:
        return jsonify({'msg':'Title already exist..!'}),400

    return jsonify({new_notes.id: {
        'title': new_notes.title,
        'detail': new_notes.detail,
        'author': new_notes.author,
    }})

@app.route('/notes/<id>', methods=['PUT'])
def update_notes(id):
    note = Note.query.get(id)
    if not note:
        abort(404)
    title = request.json['title']
    detail = request.json['detail']
    author = request.json['author']
    note.title = title
    note.detail = detail
    note.author = author
    db.session.commit()
    return jsonify({note.id: {
        'title': note.title,
        'detail': note.detail,
        'author': note.author,
    }})

@app.route('/notes/<id>', methods = ['DELETE'])
def delete_note_by_id(id):
    get_note = Note.query.get(id)
    if not get_note:
        abort(404)
    db.session.delete(get_note)
    db.session.commit()
    return ("",204)