from flask import Flask
from controllers.consumption import consumption_blueprint
from controllers.home import home_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(consumption_blueprint)
    app.register_blueprint(home_blueprint)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)