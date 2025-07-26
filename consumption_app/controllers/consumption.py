from flask import Blueprint, jsonify, request
from datetime import datetime
from usecases.get_consumption import get_consumption_between

consumption_blueprint = Blueprint("consumption", __name__, url_prefix='/consumption')

@consumption_blueprint.route("/", methods=["GET"])
def consumption():
    start = request.args.get('start')
    end = request.args.get('end')
    if not start or not end:
        return jsonify({"message": "start and end paramters are required"}), 400

    try:
        start = datetime.strptime(f"{start}", "%Y-%m-%dT%H:%M")
    except ValueError as e:
        return jsonify({"message": "start needs to be formated that way YYYY-MM-DDTHH:MM"}), 400

    try:
        end = datetime.strptime(f"{end}", "%Y-%m-%dT%H:%M")
    except ValueError as e:
        return jsonify({"message": "end needs to be formated that way YYYY-MM-DDTHH:MM"}), 400

    if start > end:
        return jsonify({"message": "start needs to be a more recent date than end"}), 400

    try: 
        result = get_consumption_between(start, end)
        return jsonify(result), 200
    except Exception as e: 
        return jsonify({"error": str(e)}), 500