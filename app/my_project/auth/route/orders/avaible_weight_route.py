from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders import avaible_weight_controller
from my_project.auth.domain.orders.avaible_weight import AvaibleWeight

avaible_weight_bp = Blueprint('avaible_weight', __name__, url_prefix='/avaible_weight')
avaible_weight = avaible_weight_controller.AvaibleWeightController()


@avaible_weight_bp.get('')
def get_all_avaible_weight() -> Response:
    return make_response(jsonify(avaible_weight.find_all()), HTTPStatus.OK)


@avaible_weight_bp.post('')
def create_avaible_weight() -> Response:
    content = request.get_json()
    return make_response(jsonify(avaible_weight.create(AvaibleWeight.create_from_dto(content))), HTTPStatus.CREATED)


@avaible_weight_bp.get('/<int:avaible_weight_id>')
def get_avaible_weight(avaible_weight_id: int) -> Response:
    return make_response(jsonify(avaible_weight.find_by_id(avaible_weight_id)), HTTPStatus.OK)


@avaible_weight_bp.put('/<int:avaible_weight_id>')
def update_avaible_weight(avaible_weight_id: int) -> Response:
    content = request.get_json()
    avaible_weight.update(avaible_weight_id, AvaibleWeight.create_from_dto(content))
    return make_response("AvaibleWeight updated", HTTPStatus.OK)


@avaible_weight_bp.patch('/<int:avaible_weight_id>')
def patch_avaible_weight(avaible_weight_id: int) -> Response:
    avaible_weight.patch(avaible_weight_id, request.get_json())
    return make_response("AvaibleWeight updated", HTTPStatus.OK)


@avaible_weight_bp.delete('/<int:avaible_weight_id>')
def delete_avaible_weight(avaible_weight_id: int) -> Response:
    avaible_weight.delete(avaible_weight_id)
    return make_response("AvaibleWeight deleted", HTTPStatus.OK)
