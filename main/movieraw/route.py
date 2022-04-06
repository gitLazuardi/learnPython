from unittest import result
from main import db, app, jsonify, abort, IntegrityError, request
from main.movie.models import Movie
from main.category.models import Category
from main.movie.models import MovieSchema

singular = MovieSchema()
plural = MovieSchema(many=True)

@app.route('/moviesraw', methods=['GET'])
def get_movies_raw():
    movies = db.session.execute('select a.*,b.name as category, b.id as catid from movie a join category b on a.category_id = b.id')
    res = {}
    for item in movies:
        res[item.id] = {
            'id': item.id,
            'name': item.name,
            'category_id': item.category_id,
            'category': {
                'id': item.catid,
                'name':item.category,
            }
        }
    return jsonify(res)

@app.route('/moviesraw/<id>', methods = ['GET'])
def get_movie_by_id_raw(id):
    res = {}
    sql = "select a.*,b.name as category, b.id as catid from movie a join category b on a.category_id = b.id where a.id=:id"
    val = {'id':id}
    movie = db.session.execute(sql, val).fetchone()
    res = {
        'id' :movie.id,
        'name' :movie.name,
        'category_id' :movie.id,
        'category' : {
            'id':movie.catid,
            'name':movie.category
        }
    }
    return res

@app.route('/moviesraw', methods=['POST'])
def add_movies_raw():
    res = {}
    name = request.json['name']
    category_id = request.json['category_id']
    sql = "select id from category where id=:id"
    val = {'id':category_id}
    test = db.session.execute(sql, val).fetchone()
    if not test:
        return {'msg': 'Category not found..'},400
    else:
        val = {'name':name,'category_id':category_id}
        db.session.execute(f"INSERT INTO movie (name, category_id) VALUES (:name, :category_id)", val)
        db.mark_changed(db.session)
        
        # res = {
        #     'id' :movie.id,
        #     'name' :movie.name,
        #     'category_id' :movie.id,
        #     'category' : {
        #         'id':movie.catid,
        #         'name':movie.category
        #     }
        # }
    return {'add':'true'}