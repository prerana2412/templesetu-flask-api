from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Allow all origins

mongo_client = MongoClient("YOUR_MONGODB_ATLAS_STRING")
db = mongo_client["temple_app"]
collection = db["temples"]

@app.route("/temple/<temple_id>", methods=["GET"])
def get_temple_metadata(temple_id):
    doc = collection.find_one({"temple_id": temple_id})
    if not doc:
        return jsonify({"error": "Temple not found"}), 404

    doc["_id"] = str(doc["_id"])  # remove ObjectId
    return jsonify(doc)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

