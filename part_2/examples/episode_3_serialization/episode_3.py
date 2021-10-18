from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)


class BookSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    author = fields.Str()
    year = fields.Int()


book_schema = BookSchema()
books_schema = BookSchema(many=True)

api = Api(app)
book_ns = api.namespace('')

b1 = Book(id=1, name="Гарри Поттер", author="Джоан Роулинг", year=1992)
b2 = Book(id=2, name="Граф Монте Кристо", author="Александр Дюма", year=1854)

db.create_all()

with db.session.begin():
    db.session.add_all([b1, b2])


@book_ns.route('/books')
class BooksView(Resource):
    def get(self):
        all_books = Book.query.all()
        return books_schema.dump(all_books), 200

    def post(self):
        req_json = request.json
        new_user = Book(**req_json)
        with db.session.begin():
            db.session.add(new_user)
        return "", 201


@book_ns.route('/books/<int:uid>')
class BookView(Resource):

    def get(self, uid: int):    # Получение данных
        try:
            book = Book.query.get(uid)
            return book_schema.dump(book), 200
        except Exception as e:
            return "", 404

    def put(self, uid):  # Замена данных
        book = Book.query.get(uid)
        req_json = request.json
        book.name = req_json.get("name")
        book.email = req_json.get("email")
        book.age = req_json.get("age")
        db.session.add(book)
        db.session.commit()
        return "", 204

    def patch(self, uid): # Частичное обновление данных
        book = Book.query.get(uid)
        req_json = request.json
        if "name" in req_json:
            book.name = req_json.get("name")
        if "email" in req_json:
            book.email = req_json.get("email")
        if "age" in req_json:
            book.age = req_json.get("age")
        db.session.add(book)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        user = Book.query.get(uid)
        db.session.delete(user)
        db.session.commit()
        return "", 204


if __name__ == '__main__':
    app.run(debug=False)
