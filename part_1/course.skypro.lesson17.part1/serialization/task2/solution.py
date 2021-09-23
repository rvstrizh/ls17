import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
db = SQLAlchemy(app)


class Guide(db.Model):
    __tablename__ = 'guide'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String)
    full_name = db.Column(db.String)
    tours_count = db.Column(db.Integer)
    bio = db.Column(db.String)
    is_pro = db.Column(db.Boolean)
    company = db.Column(db.Integer)


class GuideSchema(Schema):
    id = fields.Int(dump_only=True)
    surname = fields.Str()
    full_name = fields.Str()
    tours_count = fields.Int()
    bio = fields.Str()
    is_pro = fields.Bool()
    company = fields.Int()


def get_json():
    guide1 = Guide(id=2, surname='Васечкин', full_name='Андрей Васечкин', tours_count=5,
                   bio='Я обожаю Москву, и изучаю город с необычных ракурсов.', is_pro=True, company=1)
    guide2 = Guide(id=3, surname='Новикова', full_name='Людмила Новикова', tours_count=2,
                   bio='Я петербурженка в 7-м поколении. Люблю делиться историями', is_pro=True, company=2)
    guide3 = Guide(id=4, surname='Беридзе', full_name='Георги Беридзе', tours_count=5,
                   bio='Филолог-журналист по образованию.', is_pro=True, company=None)
    guides_schema = GuideSchema(many=True)

    return guides_schema.dumps([guide1, guide2, guide3])
