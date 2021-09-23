import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route("/tours", methods=['GET'])
def get_tours():
    data = [
        {"id": 1, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 2, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 3, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 4, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
    ]
    return json.dumps(data)


@app.route("/tours/<int:sid>", methods=['GET'])
def get_tour_by_id(sid: int):
    data = [
        {"id": 1, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 2, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 3, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 4, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
    ]
    for d in data:
        if d["id"] == sid:
            return json.dumps(d), 200
    return "", 404


@app.route("/tours", methods=['POST'])
def create_tour():
    # add logic
    return "", 201


@app.route("/tours/<int:sid>", methods=['PUT'])
def update_tour(sid: int):
    data = json.loads(request.data)
    f1 = data["f1"]
    print(f1)
    if sid is None or f1 is None:
        return "", 400
    # update logic
    return "", 204


@app.route("/tours/<int:sid>", methods=['DELETE'])
def delete_tour(sid: int):
    # delete logic
    return "", 204
