from flask import Blueprint, jsonify

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome on the electricity consumption API"}), 200