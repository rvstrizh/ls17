# app.py

from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class UserDB(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)


api = Api(app)
user_ns = api.namespace('tests')

jonh = UserDB(id=1, email='a@a.a', name='jane', age=20)
kate = UserDB(id=2, email='b@a.a', name='kate', age=28)
max = UserDB(id=3, email='c@a.a', name='max', age=32)
maxim = UserDB(id=4, email='d@a.a', name='maxim', age=38)
mary = UserDB(id=5, email='e@a.a', name='mary', age=36)

db.drop_all()
db.create_all()

with db.session.begin():
    db.session.add_all([jonh, kate, max, mary])




@app.route('/tests/', methods= ["GET]]
def index():
    return render_template("index.html", data=data)

@app.route('/tests/<int:id>', methods= ["POST]]
def index(id):
    return render_template("index.html", data=data)

@app.route('/tests/', methods= ["POST]]
def index():
    return render_template("index.html", data=data)





@user_ns.route('/')
class Users(Resource):
    def get(self):
        users_response = []
        all_users = UserDB.query.all()
        for u in all_users:
            user_dict = {
                "id": u.id,
                "name": u.title,
                "email": u.email,
                "age": u.age
            }
            users_response.append(user_dict)
        return users_response, 200

    def post(self):
        req_json = request.json
        new_user = UserDB(**req_json)
        with db.session.begin():
            db.session.add(new_user)
        return "", 201


@user_ns.route('/<int:uid>')
class User(Resource):
    def get(self, uid: int):
        try:
            user = UserDB.query.get(uid)
            user_dict = {
                "id": user.id,
                "name": user.title,
                "email": user.email,
                "age": user.age
            }
            return user_dict, 200
        except Exception as e:
            return "", 404

    def put(self, uid: int):
        user = UserDB.query.get(uid)
        req_json = request.json
        user.title = req_json.get("name")
        user.email = req_json.get("email")
        user.age = req_json.get("age")
        db.session.add(user)
        db.session.commit()
        return "", 204

    def patch(self, uid: int):
        user = UserDB.query.get(uid)
        req_json = request.json
        if "name" in req_json:
            user.title = req_json.get("name")
        if "email" in req_json:
            user.email = req_json.get("email")
        if "age" in req_json:
            user.age = req_json.get("age")
        db.session.add(user)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        user = UserDB.query.get(uid)
        db.session.delete(user)
        db.session.commit()
        return "", 204


if __name__ == '__main__':
    app.run(debug=False)
