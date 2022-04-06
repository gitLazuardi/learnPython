from unittest import result
from main import db, app, jsonify, abort, IntegrityError, request
from main.movie.models import Movie
from main.category.models import Category
from main.movie.models import MovieSchema

singular = MovieSchema()
plural = MovieSchema(many=True)

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    result = plural.dump(movies)
    return jsonify({"data": result})

@app.route('/movies/<id>', methods = ['GET'])
def get_movie_by_id(id):
    movie = Movie.query.filter_by(id=id).first()
    if not movie:
        abort(404)
    result = singular.dump(movie)
    return jsonify({"data": result})

@app.route('/movies', methods=['POST'])
def add_movies():
    name = request.json['name']
    category_id = request.json['category_id']
    test = Category.query.filter_by(id=category_id).first()
    if not test:
        return {'msg': 'Invalid input category_id, category not found'},400
    else:
        movie = Movie(name=name, category_id=category_id)
        db.session.add(movie)
        db.session.commit()

        result = singular.dump(movie)
        return jsonify({"data": result})