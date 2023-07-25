from app import db
from app.models.restaurant_models import Restaurant, Product
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


def get_user_by_id_from_db(user_id):
    return db.session.query(User).get(user_id)


def update_phone_number_db(user):
    try:
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def delete_user_by_phone_number_db(user):
    try:
        db.session.delete(user)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def get_user_by_email(email):
    return db.session.query(User).filter(User.email == email).first()


def logout_db():
    try:
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def insert_restaurant_to_db(restaurant):
    try:
        db.session.add(restaurant)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def get_restaurant_by_id_from_db(restaurant_id):
    return db.session.query(Restaurant).get(restaurant_id)


def edit_restaurant_db(restaurant):
    try:
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def get_all_restaurants_from_db():
    return db.session.query(Restaurant).all()


def add_product_to_db(product):
    try:
        db.session.add(product)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def get_product_by_id_from_db(product_id):
    return db.session.query(Product).get(product_id)


def edit_product_db(product):
    try:
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False
