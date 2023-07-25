from flask import request
from app.api import bp
from app.auth import token_auth
from app.controller import user_controller


@bp.route('/createNewUser', methods=['POST'])
def create_user():
    return user_controller.create_new_user_controller(request)


@bp.route('/getAllUser', methods=['GET'])
def get_all_user():
    return user_controller.get_all_users_controller(request)


@bp.route('/getUserById', methods=['GET'])
def get_user_by_id():
    return user_controller.get_user_by_id_controller(request)


@bp.route('/UpdatePhoneNumber', methods=['PUT'])
@token_auth.login_required
def update_phone_number():
    return user_controller.update_phone_number_controller(token_auth.current_user().id, request)


@bp.route('/addNTestUsers', methods=['POST'])
def add_n_test_users():
    return user_controller.add_n_test_users_controller(request)


@bp.route('/DeleteUserByPhoneNumber', methods=['DELETE'])
def delete_user_by_phone_number():
    return user_controller.delete_user_by_phone_number_controller(request)


@bp.route('/Login', methods=['GET', 'POST'])
def login():
    return user_controller.login_controller(request)


@bp.route('/Logout', methods=['GET'])
@token_auth.login_required
def logout():
    return user_controller.logout_controller(token_auth.current_user().id)


# TODO:
# addNewRest
@bp.route('/createNewRestaurant', methods=['POST'])
def create_restaurant():
    return user_controller.create_new_restaurant_controller(request)


# editRest
@bp.route('/editRestaurant', methods=['POST'])
def edit_restaurant():
    return user_controller.edit_restaurant_controller(request)


# addProductsOfRest
@bp.route('/addProduct', methods=['POST'])
def add_product():
    return user_controller.add_product_controller(request)


# editProductsOfRest
@bp.route('/editProduct', methods=['POST'])
def edit_product():
    return user_controller.edit_product_controller(request)


# getAllRest
@bp.route('/getAllRestaurant', methods=['GET'])
def get_all_restaurant():
    return user_controller.get_all_restaurant_controller(request)


# getProductsOfRest

# createOrder
@bp.route('/createOrder', methods=['POST'])
def create_Order():
    return user_controller.create_order(request)
