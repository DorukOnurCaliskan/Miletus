from app.db import user_db
from app.models.user_models import User


def get_user_by_phone_service(phone):
    return user_db.get_user_by_phone(phone)


def create_user_service(data):
    user = User()
    user.from_dict(data)
    return user_db.insert_user_to_db(user)


def get_all_users_service():
    users = user_db.get_all_users_from_db()
    user_list = [user.to_dict() for user in users]
    return user_list


def get_user_by_id_service(user_id):
    return user_db.get_user_by_id_from_db(user_id)


def update_phone_number_service(old_phone, new_phone):
    user = user_db.get_user_by_phone(old_phone)
    if user is None:
        return False
    user.phone = new_phone
    return user_db.update_phone_number_db(user)


def delete_user_by_phone_number_service(phone):
    user = user_db.get_user_by_phone(phone)
    if user is None:
        return False
    if user.phone == phone:
        return user_db.delete_user_by_phone_number_db(user)
    else :
        return


def auth_user_service(email, password):

    user = user_db.get_user_by_email(email)
    if not user:
        return False
    if user.verify_password(password):
        return user.get_token(2629743)
    return False