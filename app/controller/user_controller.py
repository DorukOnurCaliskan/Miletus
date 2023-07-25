from flask import jsonify

from app.service import user_service
from errors import bad_request
from utils.decorators import verify_registration_data, verify_restaurant_data, verify_product_data


@verify_registration_data
def create_new_user_controller(data):
    if user_service.get_user_by_phone_service(data['phone']):
        return bad_request("Üyelik var")

    if user_service.get_user_by_email_service(data['email']):
        return bad_request("Üyelik var")

    if user_service.create_user_service(data):
        return jsonify(message="Üyelik Başarılı")
    else:
        return bad_request("SYSTEM ERROR")


def get_all_users_controller(request):
    user_list = user_service.get_all_users_service()

    # todo: below line better in service
    if not user_list:
        return jsonify(message="Sisteme kayıtlı kullanıcı bulunamadı")

    return jsonify(user_list)


def get_user_by_id_controller(request):
    # todo:you MUST always check your inputs while data read etc

    client_id = request.args.get('id')
    if client_id:
        if not isinstance(client_id, int):
            return bad_request("Kullanıcı Bullunamadı")

    user = user_service.get_user_by_id_service(client_id)
    if user:
        user_dict = user.to_dict()
        return jsonify(user_dict)
    else:
        return bad_request("Kullanıcı Bullunamadı")


def update_phone_number_controller(user_id, request):
    user = user_service.get_user_by_id_service(user_id)

    data = request.get_json()
    # Alternative for more generic usage
    result_data = {}

    if user_service.update_phone_number_service_v2(user, data):
        for field in data:
            if field == "phone":
                result_data['phone_number'] = "updated"
            if field == "name":
                result_data['name'] = "updated"
            if field == "email":
                result_data['email'] = "updated"
            if field == "surname":
                result_data['surname'] = "updated"
        return jsonify(result_data)
    else:
        return bad_request("Failed to update phone number")

    # if user_service.update_phone_number_service(user, data['new_phone']):
    #     return jsonify(message='Phone number updated successfully')
    # else:
    #     return bad_request("Failed to update phone number")


def add_n_test_users_controller(request):
    data = request.get_json()
    for user_data in data['users']:

        if user_service.get_user_by_phone_service(user_data['phone']):
            print("Üyelik var")
        else:
            if user_service.create_user_service(user_data):
                print("Üyelik başarılı")
            else:
                print("System error")

    return jsonify(message="Olmayan Üyelikler eklendi")


def delete_user_by_phone_number_controller(request):
    data = request.get_json()
    if 'phone' not in data:
        return bad_request("Telefon numarası yok")

    if user_service.delete_user_by_phone_number_service(data['phone']):
        return jsonify(message='User deleted successfully')
    else:
        return bad_request("Failed to delete user")


def login_controller(request):
    data = request.get_json() or {}

    # TODO: check all fields and required format

    if 'email' not in data and 'password' not in data:
        return bad_request("Mıssing Fields")

    email = data['email']
    password = data['password']
    # TODO: need format control

    # IF everything fine lets go

    token = user_service.auth_user_service(email, password)
    if not token:
        return bad_request("Kullanıcı Bulunamadı")
    return jsonify(access_token=token)


def logout_controller(user_id):
    user = user_service.get_user_by_id_service(user_id)
    user_service.logout_service(user)
    return jsonify('Logout')


@verify_restaurant_data
def create_new_restaurant_controller(data):
    if user_service.create_new_restaurant_service(data):
        return jsonify(message="restoran Üyelik Başarılı")
    else:
        return bad_request("SYSTEM ERROR")


def edit_restaurant_controller(request):
    data = request.get_json()
    # Alternative for more generic usage
    result_data = {}
    restaurant = user_service.get_restaurant_by_id_service(data['restaurant_id'])
    if user_service.edit_restaurant_service(restaurant, data):
        for field in data:
            if field == "restaurant_name":
                result_data['restaurant_name'] = "updated"
            if field == "restaurant_address":
                result_data['restaurant_address'] = "updated"
            if field == "restaurant_type":
                result_data['restaurant_type'] = "updated"
            if field == "restaurant_opening_hour":
                result_data['restaurant_opening_hour'] = "updated"
            if field == "restaurant_closing_hour":
                result_data['restaurant_closing_hour'] = "updated"
            if field == "restaurant_status":
                result_data['restaurant_status'] = "updated"
        return jsonify(result_data)
    else:
        return bad_request("Failed to update phone number")


@verify_product_data
def add_product_controller(data):
    if user_service.add_product_service(data):
        return jsonify(message="Ürün girme Başarılı")
    else:
        return bad_request("SYSTEM ERROR")


def edit_product_controller(request):
    data = request.get_json()
    # Alternative for more generic usage
    result_data = {}
    product = user_service.get_product_by_id_service(data['product_id'])
    if user_service.edit_product_service(product, data):
        for field in data:
            if field == "product_name":
                result_data['product_name'] = "updated"
            if field == "product_price":
                result_data['product_price'] = "updated"
            if field == "discount_amount":
                result_data['discount_amount'] = "updated"
            if field == "product_status":
                result_data['product_status'] = "updated"
            if field == "product_stock":
                result_data['product_stock'] = "updated"
        return jsonify(result_data)
    else:
        return bad_request("Failed to update data")


def get_all_restaurant_controller(request):
    restaurant_list = user_service.get_all_restaurant_service()

    # todo: below line better in service
    if not restaurant_list:
        return jsonify(message="Sisteme kayıtlı restoran bulunamadı")

    return jsonify(restaurant_list)