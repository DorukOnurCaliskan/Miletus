# -- coding: UTF-8 --
import os
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config.config import Config
import app.db
db = SQLAlchemy()
migrate = Migrate()

# csrf = CSRFProtect()
def create_app(config_class=Config):
    # rest of connection code using the connection string uri
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    MIGRATION_DIR = os.path.join('config', 'database_migrations_psql')
    migrate.init_app(app, db, directory=MIGRATION_DIR, compare_type=True)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    with app.app_context():
        from app import models
        db.create_all()
    return app


#     from app.api import bp as api_bp
#     app.register_blueprint(api_bp, url_prefix='/api')

