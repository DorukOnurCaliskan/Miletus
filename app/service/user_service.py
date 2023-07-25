import datetime

from app.db import user_db
from app.models.restaurant_models import Product, Restaurant
from app.models.user_models import User


def get_user_by_phone_service(phone):
    return user_db.get_user_by_phone(phone)


def create_user_service(data):
    user = User()
    user.from_dict_alternative(data, True)
    return user_db.insert_user_to_db(user)


def get_all_users_service():
    users = user_db.get_all_users_from_db()
    user_list = [user.to_dict() for user in users]
    return user_list


def get_user_by_id_service(user_id):
    return user_db.get_user_by_id_from_db(user_id)


def update_phone_number_service(user, new_phone):
    user.phone = new_phone
    return user_db.update_phone_number_db(user)


def update_phone_number_service_v2(user, data):
    user.from_dict_alternative(data)
    return user_db.update_phone_number_db(user)


def delete_user_by_phone_number_service(phone):
    user = user_db.get_user_by_phone(phone)
    if user is None:
        return False
    if user.phone == phone:
        return user_db.delete_user_by_phone_number_db(user)
    else:
        return


def auth_user_service(email, password):
    user = user_db.get_user_by_email(email)
    if not user:
        return False
    if user.verify_password(password):
        return user.get_token()
    return False


def logout_service(user):
    user.token_expiration = datetime.datetime.now() - datetime.timedelta(seconds=1)
    return user_db.logout_db()


def get_user_by_email_service(email):
    return user_db.get_user_by_email(email)


def create_new_restaurant_service(data):
    restaurant = Restaurant()
    restaurant.from_dict_alternative(data)
    return user_db.insert_restaurant_to_db(restaurant)


def get_restaurant_by_id_service(restaurant_id):
    return user_db.get_restaurant_by_id_from_db(restaurant_id)


def edit_restaurant_service(restaurant, data):
    restaurant.from_dict_alternative(data)
    return user_db.edit_restaurant_db(restaurant)


def get_all_restaurant_service():
    restaurants = user_db.get_all_restaurants_from_db()
    restaurants_list = [restaurant.to_dict() for restaurant in restaurants]
    return restaurants_list


def add_product_service(data):
    product = Product()
    product.from_dict_alternative(data)
    return user_db.insert_restaurant_to_db(product)


def get_product_by_id_service(product_id):
    return user_db.get_product_by_id_from_db(product_id)


def edit_product_service(product, data):
    product.from_dict_alternative(data)
    return user_db.edit_product_db(product)
