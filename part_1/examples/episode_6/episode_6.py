from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    age = fields.Int()


# user = User(id=1, name="jane", age=19)
# user_schema = UserSchema()
# print(user_schema.dump(user)["name"])
# print(user_schema.dumps(user))


# u = User(id=1, name="Jonh", age=30)
user_schema = UserSchema()
# print(user_schema.dumps(u))

u1 = User(id=2, name="Jonh", age=30)
u2 = User(id=3, name="Kate", age=30)
u3 = User(id=4, name="Mary", age=30)
u4 = User(id=5, name="Max", age=30)
users_schema = UserSchema(many=True)
print(users_schema.dump([u1, u2, u3, u4]))

# user_json_str = '{"name": "Jonh", "age": 30}'
# user_dict = user_schema.loads(user_json_str)
# user = User(**user_dict)
# print(user.age)


if __name__ == '__main__':
    app.run(debug=True)
