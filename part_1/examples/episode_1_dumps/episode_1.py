import datetime
import decimal
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

##### Шаг 1  #####

# a = "hello world"
# b = {
#     "field": "value"
# }
# c = [1, 2, 3]
# print(json.dumps(a))
# print(json.dumps(b))
# print(json.dumps(c))

##### Шаг 2  #####

# a = datetime.datetime.now()
# b = decimal.Decimal(3)
# # json.dumps(a)
# json.dumps(b)

##### Шаг 3  #####
#
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     age = db.Column(db.Integer)
#
#
# u = User(name="Jonh", age=30)
# json.dumps(u)
#
# a = "hello world"
# b = '{"field": "value"}'
# c = "[1, 2, 3]"
#print(json.loads(a))
# print(json.loads(b)["field"])
# print(json.loads(c)[0])

###### Шаг 4 #######


# a = "hello world"
# print(json.loads(a))


# b = '{"field": "value"}'
# # Получаем словарь
# print(json.loads(b)["field"])


# c = "[1, 2, 3]"
# # Получаем список
# print(json.loads(c)[0])




if __name__ == '__main__':
    app.run(debug=True)
