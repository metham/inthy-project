from flask import Flask
from consumption_app.controllers.consumption import consumption_blueprint
from consumption_app.controllers.home import home_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(consumption_blueprint)
    app.register_blueprint(home_blueprint)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)