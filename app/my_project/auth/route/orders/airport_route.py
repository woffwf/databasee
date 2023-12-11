from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders import airport_controller
from my_project.auth.domain.orders.airport import Airport

airport_bp = Blueprint('airport', __name__, url_prefix='/airport')
airport = airport_controller.AirportController()


@airport_bp.get('')
def get_all_airport() -> Response:
    return make_response(jsonify(airport.find_all()), HTTPStatus.OK)


@airport_bp.post('')
def create_airport() -> Response:
    content = request.get_json()
    return make_response(jsonify(airport.create(Airport.create_from_dto(content))), HTTPStatus.CREATED)


@airport_bp.get('/<int:airport_id>')
def get_airport(airport_id: int) -> Response:
    return make_response(jsonify(airport.find_by_id(airport_id)), HTTPStatus.OK)


@airport_bp.put('/<int:airport_id>')
def update_airport(airport_id: int) -> Response:
    content = request.get_json()
    airport.update(airport_id, Airport.create_from_dto(content))
    return make_response("Airport updated", HTTPStatus.OK)


@airport_bp.patch('/<int:airport_id>')
def patch_airport(airport_id: int) -> Response:
    airport.patch(airport_id, request.get_json())
    return make_response("Airport updated", HTTPStatus.OK)


@airport_bp.delete('/<int:airport_id>')
def delete_airport(airport_id: int) -> Response:
    airport.delete(airport_id)
    return make_response("Airport deleted", HTTPStatus.OK)


@airport_bp.get('/<int:airport_id>/connected_flight')
def get_connected_flight(airport_id: int):
    result = airport.get_connected_flight(airport_id)
    result = [row.put_into_dto() for row in result]

    return make_response(jsonify(result), HTTPStatus.OK)
