from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.controllers import product_controller, transaction_controller
    app.register_blueprint(product_controller.bp)
    app.register_blueprint(transaction_controller.bp)

    return app
