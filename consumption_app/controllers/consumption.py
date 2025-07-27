from flask import Blueprint, jsonify, request
from datetime import datetime
from consumption_app.usecases.get_consumption_between import GetConsumptionBetween
from consumption_app.infrastructure.repositories.sql_alch_energy_repository import SqlAlchemyEnergyRepository


consumption_blueprint = Blueprint("consumption", __name__, url_prefix='/consumption')

@consumption_blueprint.route("/", methods=["GET"])
def consumption():
    start = request.args.get('start')
    end = request.args.get('end')
    if not start or not end:
        return jsonify({"message": "start and end paramters are required"}), 400

    try:
        start = datetime.fromisoformat(start)
    except ValueError as e:
        return jsonify({"message": "start needs to be in the ISO format"}), 400

    try:
        end = datetime.fromisoformat(end)
    except ValueError as e:
        return jsonify({"message": "end needs to be in the ISO format"}), 400

    repo = SqlAlchemyEnergyRepository()
    get_between = GetConsumptionBetween(repository=repo)

    try: 
        result = get_between.execute(start, end)
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400   
    except Exception as e: 
        return jsonify({"error": str(e)}), 500