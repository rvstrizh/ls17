# app.py

from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)

api = Api(app)

book_ns = api.namespace('books')
note_ns = api.namespace('notes')
user_ns = api.namespace('users')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        ...


@book_ns.route('/<int:uid>')
class BookView(Resource):
    def get(self, uid):
        ...


@note_ns.route('/')
class NotesView(Resource):
    def get(self):
        ...


@user_ns.route('/<int:uid>')
class NoteView(Resource):
    def get(self, uid):
        ...


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        ...


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        ...


if __name__ == '__main__':
    app.run(debug=False)
