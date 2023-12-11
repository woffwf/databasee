from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.available_flight_controller import AvailableFlightController
from my_project.auth.domain.orders.avaible_flight import AvailableFlight

available_flight_bp = Blueprint('available_flight', __name__, url_prefix='/available_flight')
available_flight = AvailableFlightController()


@available_flight_bp.get('')
def get_all_available_flight() -> Response:
    return make_response(jsonify(available_flight.find_all()), HTTPStatus.OK)


@available_flight_bp.post('')
def create_available_flight() -> Response:
    content = request.get_json()
    return make_response(jsonify(available_flight.create(AvailableFlight.create_from_dto(content))), HTTPStatus.CREATED)


@available_flight_bp.get('/<int:available_flight_id>')
def get_available_flight(available_flight_id: int) -> Response:
    return make_response(jsonify(available_flight.find_by_id(available_flight_id)), HTTPStatus.OK)


@available_flight_bp.put('/<int:available_flight_id>')
def update_available_flight(available_flight_id: int) -> Response:
    available_flight.update(available_flight_id, AvailableFlight.create_from_dto(request.get_json()))
    return make_response("AvailableFlight updated", HTTPStatus.OK)


@available_flight_bp.patch('/<int:available_flight_id>')
def patch_available_flight(available_flight_id: int) -> Response:
    available_flight.patch(available_flight_id, request.get_json())
    return make_response("AvailableFlight updated", HTTPStatus.OK)


@available_flight_bp.delete('/<int:available_flight_id>')
def delete_available_flight(available_flight_id: int) -> Response:
    available_flight.delete(available_flight_id)
    return make_response("AvailableFlight deleted", HTTPStatus.OK)


@available_flight_bp.get('/<int:available_flight_id>/connected_flight')
def get_all_connected_flight(available_flight_id: int) -> Response:
    result = available_flight.get_all_available_flights(available_flight_id)
    result = [row.put_into_dto() for row in result]

    return make_response(jsonify(result), HTTPStatus.OK)


@available_flight_bp.get('/<int:available_flight_id>/available_flights')
def available_flights(available_flight_id: int) -> Response:
    result = available_flight.available_flights(available_flight_id)
    result = [row.put_into_dto() for row in result]

    return make_response(jsonify(result), HTTPStatus.OK)
