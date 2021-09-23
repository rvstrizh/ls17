import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    full_name = Column(String)
    city = Column(Integer)
    city_ru = Column(String)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    password = fields.Str()
    full_name = fields.Str()
    city = fields.Int()
    city_ru = fields.Str()


class Guide(db.Model):
    __tablename__ = 'guide'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    full_name = Column(String)
    tours_count = Column(Integer)
    bio = Column(String)
    is_pro = Column(Boolean)
    company = Column(Integer)


class GuideSchema(Schema):
    id = fields.Int(dump_only=True)
    surname = fields.Str()
    full_name = fields.Str()
    tours_count = fields.Int()
    bio = fields.Str()
    is_pro = fields.Bool()
    company = fields.Int()


class TourSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    guide = fields.Int()
    guide_ru = fields.Str()
    attractions = fields.Str()
    city = fields.Int()
    start_point = fields.Str()
    end_point = fields.Str()
    children_ok = fields.Str()
    group_size = fields.Int()
    language = fields.Str()
    duration_min = fields.Int()
    price_rur = fields.Int()


class Tour(db.Model):
    __tablename__ = 'tour'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    guide = db.Column(db.Integer)
    guide_ru = db.Column(db.String)
    attractions = db.Column(db.String)
    city = db.Column(db.Integer)
    start_point = db.Column(db.String)
    end_point = db.Column(db.String)
    children_ok = db.Column(db.String)
    group_size = db.Column(db.Integer)
    language = db.Column(db.String)
    duration_min = db.Column(db.Integer)
    price_rur = db.Column(db.Integer)
