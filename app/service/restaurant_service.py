from app.db import restaurant_db
from app.models.restaurant_models import Restaurant, Product


def create_new_restaurant_service(data):
    restaurant = Restaurant()
    restaurant.from_dict_alternative(data)
    return restaurant_db.insert_restaurant_to_db(restaurant)


def get_restaurant_by_id_service(restaurant_id):
    return restaurant_db.get_restaurant_by_id_from_db(restaurant_id)


def edit_restaurant_service(restaurant, data):
    restaurant.from_dict_alternative(data)
    return restaurant_db.edit_restaurant_db(restaurant)


def get_all_restaurant_service():
    restaurants = restaurant_db.get_all_restaurants_from_db()
    restaurants_list = [restaurant.to_dict() for restaurant in restaurants]
    return restaurants_list


def get_restaurant_by_type_service(restaurant_type):
    return restaurant_db.get_restaurant_by_type(restaurant_type)


def get_restaurant_by_name_service(restaurant_name):
    return restaurant_db.get_restaurant_by_name(restaurant_name)


def add_product_service(data):
    product = Product()
    product.from_dict_alternative(data)
    return restaurant_db.insert_restaurant_to_db(product)


def get_product_by_id_service(product_id):
    return restaurant_db.get_product_by_id_from_db(product_id)


def edit_product_service(product, data):
    product.from_dict_alternative(data)
    return restaurant_db.edit_product_db(product)


def auth_restaurant_service(restaurant_name, restaurant_password):
    restaurant = restaurant_db.get_restaurant_by_name(restaurant_name)
    if not restaurant:
        return False
    if restaurant.verify_password(restaurant_password):
        return restaurant.get_token()
    return False