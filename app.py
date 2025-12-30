from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection (service name = mongo)
MONGO_URI = os.environ.get(
    "MONGO_URI", "mongodb://mongo:27017/flaskdb"
)

client = MongoClient(MONGO_URI)
db = client.flaskdb
collection = db.users


@app.route("/")
def home():
    return "Flask + MongoDB + Docker Volume is working"


@app.route("/add", methods=["POST"])
def add_user():
    data = request.json
    collection.insert_one(data)
    return {"message": "User added successfully"}, 201


@app.route("/users", methods=["GET"])
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return jsonify(users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
