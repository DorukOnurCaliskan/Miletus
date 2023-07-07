# -- coding: UTF-8 --
import logging
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
    if os.environ.get('APP_MODE') == 'prod':
        print('Production Mode sOn')

        if app.config['LOG_TO_STDOUT'] == 1:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/teklifimgelsinapp.log',
                                               maxBytes=10240, backupCount=10)

            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('App Started')

    return app


#     from app.api import bp as api_bp
#     app.register_blueprint(api_bp, url_prefix='/api')
