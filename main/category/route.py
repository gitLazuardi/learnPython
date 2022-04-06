import json
from main import db, app, jsonify, abort, IntegrityError, request, Flask
from main.movie.models import Movie
from main.category.models import Category
from main.category.models import CategorySchema

one = CategorySchema()
many = CategorySchema(many=True)

@app.route('/category', methods=['GET'])
def index_category():
    cat = Category.query.all()
    result = many.dump(cat)
    return jsonify(result)

@app.route('/category/<id>', methods=['GET'])
def find_category(id):
    result = db.session.execute('select a.*, b.name as movname, b.id as movid from category a join movie b on a.id = b.category_id where a.id=:id',{'id':id})
    res = {}
    movies = {}
    for item in result:
        res[item.id] = {'name':item.name}
        movies[item.movid] = {'name':item.movname}
    res['movies'] = movies
    
    return jsonify(res)


@app.route('/category', methods=['POST'])
def add_category():
    name = request.json['name']
    movies = request.json['movies']
    new = Category(name=name)
    db.session.add(new)
    db.session.commit()
    idd = new.id
    for item in movies:
        movie = Movie(name=item['name'], category_id=idd)
        db.session.add(movie)
        db.session.commit()
    
    return find_category(idd)
    

        
    