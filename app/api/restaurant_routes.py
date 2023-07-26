from flask import request
from app.api import bp
from app.auth import token_auth
from app.controller import restaurant_controller


@bp.route('/createNewRestaurant', methods=['POST'])
def create_restaurant():
    return restaurant_controller.create_new_restaurant_controller(request)


# editRest
@bp.route('/editRestaurant', methods=['PUT'])
@token_auth.login_required
def edit_restaurant():
    return restaurant_controller.edit_restaurant_controller(request)


# addProductsOfRest
@bp.route('/addProduct', methods=['POST'])
def add_product():
    return restaurant_controller.add_product_controller(request)


# editProductsOfRest
@bp.route('/editProduct', methods=['PUT'])
@token_auth.login_required
def edit_product():
    return restaurant_controller.edit_product_controller(request)


# getAllRest
@bp.route('/getAllRestaurant', methods=['GET'])
def get_all_restaurant():
    return restaurant_controller.get_all_restaurant_controller(request)


@bp.route('/loginRestaurant', methods=['GET', 'POST'])
def login_restaurant():
    return restaurant_controller.login_restaurant_controller(request)

# get product of rest
# create order
