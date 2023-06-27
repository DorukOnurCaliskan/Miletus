from flask import request
from app.api import bp
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
def update_phone_number():
    return user_controller.update_phone_number_controller(request)


@bp.route('/addNTestUsers', methods=['POST'])
def add_n_test_users():
    return user_controller.add_n_test_users_controller(request)
