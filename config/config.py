import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'), override=True)


class Config(object):
    POSTGRESQL_USER = os.environ.get("POSTGRESQL_USER")
    POSTGRESQL_PASSWORD = os.environ.get("POSTGRESQL_PASSWORD")
    POSTGRESQL_DB_NAME = os.environ.get("POSTGRESQL_DB_NAME")

    uri = os.environ.get("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = uri
