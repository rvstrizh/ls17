books = {
    1: {
        "name": "Harry Potter",
        "year": 2000,
        "author": "Joan Routing"
    },
    2: {
        "name": "Le Comte de Monte-Cristo",
        "year": 1844,
        "author": "Alexandre Dumas"
    }
}


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        return jsonify(books), 200

    def post(self):
        req_json = request.json
        books[len(books) + 1] = req_json
        return "", 201


@book_ns.route('/<int:bid>')
class BookView(Resource):
    def get(self, bid):
        return books[bid], 200

    def delete(self, bid):
        del books[bid]
        return "", 204
