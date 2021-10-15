# app.py

from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError, validates

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
    permission = db.Column(db.String)


def validate_email(email):
    if "mail.ru" in email:
        raise ValidationError("No mail.ru!")


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Email(validate=validate_email)
    name = fields.Str(required=True)
    age = fields.Int(validate=validate.Range(min=18, max=40))
    permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))

    @validates("name")
    def validate_name(self, value: str):
        if value.startswith("A"):
            raise ValidationError("Name should not starts with A")


user_schema = UserSchema()
users_schema = UserSchema(many=True)

api = Api(app)
user_ns = api.namespace('users', description='users operations')

jonh = UserDB(id=1, email='a@a.a', name='jane', age=20)
kate = UserDB(id=2, email='b@a.a', name='kate', age=28)
max = UserDB(id=3, email='c@a.a', name='max', age=32)
maxim = UserDB(id=4, email='d@a.a', name='maxim', age=38)
mary = UserDB(id=5, email='e@a.a', name='mary', age=36)

db.drop_all()
db.create_all()

with db.session.begin():
    db.session.add_all([jonh, kate, max, mary])


@user_ns.route('/')
class Users(Resource):
    def get(self):
        all_users = UserDB.query.all()
        return users_schema.dump(all_users), 200

    def post(self):
        req_json = request.json
        new_user = UserDB(id=req_json.get("id"),
                          name=req_json.get("name"),
                          email=req_json.get("email"),
                          age=req_json.get("age"))
        with db.session.begin():
            db.session.add(new_user)
        return "", 201


@user_ns.route('/<int:uid>')
class User(Resource):
    def get(self, uid: int):
        try:
            user = UserDB.query.get(uid)
            return user_schema.dump(user), 200
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
    app.run(debug=True)
