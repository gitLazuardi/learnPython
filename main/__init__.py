from flask import Flask, jsonify, abort, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_marshmallow import Marshmallow
from marshmallow import fields
from flask_swagger_ui import get_swaggerui_blueprint
import os
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://uname:password@localhost:3306/flaskrest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Try swagger'
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.route("/static/swagger.json")
def specs():
    return send_from_directory("../static/", "swagger.json")

db = SQLAlchemy(app)
ma = Marshmallow(app)
 
from main.note.route import *
from main.user.route import *
from main.hobby.route import *
from main.movie.route import *
from main.category.route import *
from main.movieraw.route import *