from flask import Blueprint, jsonify
from consumption_app.usecases.get_consumption import get_consumption_between

consumption_blueprint = Blueprint("consumption", __name__, url_prefix='/consumption')

@home_blueprint.route("/", methods=["GET"])
def consumption():
    start = request.args.get('start')
    end = request.args.get('end')
    if not start or not end:
        return jsonify({"message": "start and end paramters are required"}), 400
    
    try: 
        result = get_consumption_between(start, end)
        return jsonify(result), 200
    except Exception as e: 
        return jsonify({"error": str(e)}), 500