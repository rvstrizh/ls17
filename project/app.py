# app.py

from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

api = Api(app)
movie_ns = api.namespace('movies')
director_ns = api.namespace('directors')
genre_ns = api.namespace('genres')

db.drop_all()
db.create_all()

# -------------------------------------------------------
data = {
    "movies": [],
    "directors": [],
    "genres": [],
}
# -------------------------------------------------------

for movie in data["movies"]:
    m = Movie(
        id=movie["id"],
        title=movie["title"],
        description=movie["description"],
        trailer=movie["trailer"],
        year=movie["year"],
        rating=movie["rating"],
        genre_id=movie["genre_id"],
        director_id=movie["director_id"],
    )
    with db.session.begin():
        db.session.add(m)

for director in data["directors"]:
    d = Director(
        id=director["id"],
        name=director["name"],
    )
    with db.session.begin():
        db.session.add(d)

for genre in data["genres"]:
    d = Genre(
        id=genre["id"],
        name=genre["name"],
    )
    with db.session.begin():
        db.session.add(d)

# ----------------------------------- MOVIES ---------------------------------------------------------------

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = Movie.query.all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        try:
            movie = Movie.query.get(uid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return "", 404

    def put(self, uid: int):
        movie = Movie.query.get(uid)
        req_json = request.json
        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def patch(self, uid: int):
        movie = Movie.query.get(uid)
        req_json = request.json
        if "title" in req_json:
            movie.title = req_json.get("title")
        if "description" in req_json:
            movie.description = req_json.get("description")
        if "trailer" in req_json:
            movie.trailer = req_json.get("trailer")
        if "year" in req_json:
            movie.year = req_json.get("year")
        if "rating" in req_json:
            movie.rating = req_json.get("rating")
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        user = Movie.query.get(uid)
        db.session.delete(user)
        db.session.commit()
        return "", 204


# ----------------------------------- DIRECTORS ---------------------------------------------------------------

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = Director.query.all()
        return movies_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        with db.session.begin():
            db.session.add(new_director)
        return "", 201


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid: int):
        try:
            movie = Director.query.get(uid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return "", 404

    def put(self, uid: int):
        director = Director.query.get(uid)
        req_json = request.json
        director.title = req_json.get("name")
        db.session.add(director)
        db.session.commit()
        return "", 204

    def patch(self, uid: int):
        director = Director.query.get(uid)
        req_json = request.json
        if "name" in req_json:
            director.title = req_json.get("name")
        db.session.add(director)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        director = Director.query.get(uid)
        db.session.delete(director)
        db.session.commit()
        return "", 204


# ----------------------------------- GENRES ---------------------------------------------------------------

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_users = Genre.query.all()
        return movies_schema.dump(all_users), 200

    def post(self):
        req_json = request.json
        new_movie = Genre(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid: int):
        try:
            genre = Genre.query.get(uid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return "", 404

    def put(self, uid: int):
        movie = Genre.query.get(uid)
        req_json = request.json
        movie.title = req_json.get("name")
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def patch(self, uid: int):
        genre = Genre.query.get(uid)
        req_json = request.json
        if "name" in req_json:
            genre.title = req_json.get("name")
        db.session.add(genre)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        user = Genre.query.get(uid)
        db.session.delete(user)
        db.session.commit()
        return "", 204


if __name__ == '__main__':
    app.run(debug=True)
