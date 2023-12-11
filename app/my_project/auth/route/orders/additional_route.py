from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders import additional_controller
from my_project.auth.domain.orders.addition import AdditionalTable

additional_bp = Blueprint('additional', __name__, url_prefix='/additional')
additional = additional_controller.AdditionalController()


@additional_bp.get('')
def get_all_additional() -> Response:
    return make_response(jsonify(additional.find_all()), HTTPStatus.OK)


@additional_bp.post('')
def create_additional() -> Response:
    content = request.get_json()
    return make_response(jsonify(additional.create(AdditionalTable.create_from_dto(content))), HTTPStatus.CREATED)


@additional_bp.get('/<int:additional_id>')
def get_additional(additional_id: int) -> Response:
    return make_response(jsonify(additional.find_by_id(additional_id)), HTTPStatus.OK)


@additional_bp.put('/<int:additional_id>')
def update_additional(additional_id: int) -> Response:
    content = request.get_json()
    additional.update(additional_id, AdditionalTable.create_from_dto(content))
    return make_response("AdditionalTable updated", HTTPStatus.OK)


@additional_bp.patch('/<int:additional_id>')
def patch_additional(additional_id: int) -> Response:
    content = request.get_json()
    additional.patch(additional_id, content)
    return make_response("AdditionalTable updated", HTTPStatus.OK)


@additional_bp.delete('/<int:additional_id>')
def delete_additional(additional_id: int) -> Response:
    additional.delete(additional_id)
    return make_response("AdditionalTable deleted", HTTPStatus.OK)
