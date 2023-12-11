from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.user_controller import UserController
from my_project.auth.domain.orders.user import User

user_bp = Blueprint('user', __name__, url_prefix='/user')
user = UserController()


@user_bp.get('')
def get_all_user() -> Response:
    return make_response(jsonify(user.find_all()), HTTPStatus.OK)


@user_bp.post('')
def create_user() -> Response:
    content = request.get_json()
    return make_response(jsonify(user.create(User.create_from_dto(content))),
                         HTTPStatus.CREATED)


@user_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    return make_response(jsonify(user.find_by_id(user)), HTTPStatus.OK)


@user_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    user.update(user_id, User.create_from_dto(request.get_json()))
    return make_response("User updated", HTTPStatus.OK)


@user_bp.patch('/<int:user_id>')
def patch_user(user_id: int) -> Response:
    user.patch(user_id, request.get_json())
    return make_response("User updated", HTTPStatus.OK)


@user_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    user.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)


@user_bp.get('/<int:user_id>/tickets')
def get_all_tickets(user_id: int):
    result = user.get_all_tickets(user_id)
    result = [row.put_into_dto() for row in result]

    return make_response(jsonify(result), HTTPStatus.OK)


@user_bp.get('/<int:user_id>/purchase_history')
def get_purchase_history(user_id: int):
    result = user.get_purchase_history(user_id)
    result = [row.put_into_dto() for row in result]

    return make_response(jsonify(result), HTTPStatus.OK)
