from app import db
from app.models.user_models import User


def get_user_by_phone(phone):
    return db.session.query(User).filter(User.phone == phone).first()


def insert_user_to_db(user):
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False