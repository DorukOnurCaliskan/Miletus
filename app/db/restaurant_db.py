from app import db
from app.models.restaurant_models import Restaurant, Product


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


def get_restaurant_by_type(restaurant_type):
    return db.session.query(Restaurant).filter(Restaurant.restaurant_type == restaurant_type).first()


def get_restaurant_by_name(restaurant_name):
    return db.session.query(Restaurant).filter(Restaurant.restaurant_name == restaurant_name).first()


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
