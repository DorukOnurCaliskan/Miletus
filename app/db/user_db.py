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


def get_all_users_from_db():
    return db.session.query(User).all()


def get_user_by_id_from_db():
    return db.session.query(User).filter(User.query.get(User.id) == User['id']).first()


def update_phone_number_db(user):
    try:
        db.session.commit()
        return True
    except:
        db.rollback()
        return False
