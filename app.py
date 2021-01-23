import os
import configparser

from flask import Flask, jsonify, request, abort
from marshmallow import ValidationError
from database import Database
from houses_validation import BaseSchema

app = Flask(__name__)
os.environ["FLASK_ENV"] = "development"

config = configparser.ConfigParser()
config.read("settings.ini")
HOST = config["DEFAULT"]["host"]
PORT = config["DEFAULT"]["port"]

db = Database(HOST, PORT)


@app.route("/")
def hello_world():
    """Very important method that returns the text string "Hello World!" you're welcome B)"""
    return "Hello World!"


# Houses GET
@app.route("/api/houses/", methods=["GET"])
def houses_all():
    """
    GET endpoint that returns the number of houses, as well as all of the available Houses in the database as a json
    object
    """
    houses = db.get_houses_all()
    return jsonify({"itemCount": len(houses), "items": houses})


# House by ID GET and House by ID PUT
@app.route("/api/houses/<house_id>", methods=["GET"])
def houses_by_id_get(house_id):
    """
    Endpoint that handles both GET and PUT requests targeting a single House object by id.

    The GET variant searches the database for the requested house.
    -    On success it returns the JSON representation of the object.
    -    On failure it returns a 404 error code indicating that the requested House does not exist.


    """
    if request.method == "GET":
        db_res = db.get_houses_by_id(house_id)
        if db_res is not None:
            return jsonify(db_res)
        else:
            abort(404)


@app.route("/api/houses/<house_id>", methods=["PUT"])
def houses_by_id_put(house_id):
    """
    Endpoint that handles both GET and PUT requests targeting a single House object by id.

    The PUT variant searches the database for the target house, if it finds it it will replace the saved data with the
    data from the request body. If it finds no matching House ID it will create a new resource for that data.
    -    On success it returns the JSON representation of the updated or newly created House
    -    On failure it returns 400 rejecting the request due to malformed data
    """
    data = request.json

    # schema validation
    schema = BaseSchema()
    try:
        schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # since the location isn't useful and should not be updated i will just manually set it to the requested
    # endpoints just to be extra safe.
    data["location"] = "http://{}:{}/api/houses/{}".format(HOST, PORT, house_id)
    return jsonify(db.put_houses_by_id(house_id, data))


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
