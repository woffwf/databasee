from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.user_purchase_history_controller import UserPurchaseHistoryController
from my_project.auth.domain.orders.user_purchase_history import UserPurchaseHistory

user_purchase_history_bp = Blueprint('user_purchase_history', __name__, url_prefix='/user_purchase_history')
user_purchase_history = UserPurchaseHistoryController()


@user_purchase_history_bp.get('')
def get_all_user_purchase_history() -> Response:
    return make_response(jsonify(user_purchase_history.find_all()), HTTPStatus.OK)


@user_purchase_history_bp.post('')
def create_user_purchase_history() -> Response:
    content = request.get_json()
    return make_response(jsonify(user_purchase_history.create(UserPurchaseHistory.create_from_dto(content))), HTTPStatus.CREATED)


@user_purchase_history_bp.get('/<int:user_purchase_history_id>')
def get_user_purchase_history(user_purchase_history_id: int) -> Response:
    return make_response(jsonify(user_purchase_history.find_by_id(user_purchase_history_id)), HTTPStatus.OK)


@user_purchase_history_bp.put('/<int:user_purchase_history_id>')
def update_user_purchase_history(user_purchase_history_id: int) -> Response:
    user_purchase_history.update(user_purchase_history_id, UserPurchaseHistory.create_from_dto(request.get_json()))
    return make_response("UserPurchaseHistory updated", HTTPStatus.OK)


@user_purchase_history_bp.patch('/<int:user_purchase_history_id>')
def patch_user_purchase_history(user_purchase_history_id: int) -> Response:
    user_purchase_history.patch(user_purchase_history_id, request.get_json())
    return make_response("UserPurchaseHistory updated", HTTPStatus.OK)


@user_purchase_history_bp.delete('/<int:user_purchase_history_id>')
def delete_user_purchase_history(user_purchase_history_id: int) -> Response:
    user_purchase_history.delete(user_purchase_history_id)
    return make_response("PerUserPurchaseHistory deleted", HTTPStatus.OK)
