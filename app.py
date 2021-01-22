import os
import configparser

from flask import Flask, jsonify, request
from database import Database

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
    houses = db.get_houses_all()
    return jsonify({"itemCount": len(houses), "items": houses})


# House by ID GET and House by ID PUT
@app.route("/api/houses/<house_id>", methods=["PUT", "GET"])
def houses_by_id(house_id):
    if request.method == "GET":
        return jsonify(db.get_houses_by_id(house_id))
    elif request.method == "PUT":
        data = request.json
        # since the location isn't useful and should not be updated i will just manually set it to the requested
        # endpoints just to be extra safe.
        data["location"] = "http://{}:{}/api/houses/{}".format(HOST, PORT, house_id)
        return jsonify(db.put_houses_by_id(house_id, data))


if __name__ == "__main__":
    # load the file into memory
    app.run(host=HOST, port=PORT)
