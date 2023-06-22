from flask import jsonify, request
from app import app, db
from app.api import bp
from app.controller import user_controller
from app.models.user_models import User


@bp.route('/createNewUser', methods=['POST'])
def create_user():
    return user_controller.create_new_user_controller(request)

