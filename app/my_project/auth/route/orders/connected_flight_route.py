from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.connected_flight_controller import ConnectedFlightController
from my_project.auth.domain.orders.connected_flight import ConnectedFlight

connected_flight_bp = Blueprint('connected_flight', __name__, url_prefix='/connected_flight')
connected_flight = ConnectedFlightController()


@connected_flight_bp.get('')
def get_all_descriptions() -> Response:
    return make_response(jsonify(connected_flight.find_all()), HTTPStatus.OK)


@connected_flight_bp.post('')
def create_description() -> Response:
    content = request.get_json()
    return make_response(jsonify(connected_flight.create(ConnectedFlight.create_from_dto(content))), HTTPStatus.CREATED)


@connected_flight_bp.get('/<int:connected_flight_id>')
def get_description(connected_flight_id: int) -> Response:
    return make_response(jsonify(connected_flight.find_by_id(connected_flight_id)), HTTPStatus.OK)


@connected_flight_bp.put('/<int:connected_flight_id>')
def update_description(connected_flight_id: int) -> Response:
    connected_flight.update(connected_flight_id, ConnectedFlight.create_from_dto(request.get_json()))
    return make_response("ConnectedFlight updated", HTTPStatus.OK)


@connected_flight_bp.patch('/<int:connected_flight_id>')
def patch_description(connected_flight_id: int) -> Response:
    connected_flight.patch(connected_flight_id, request.get_json())
    return make_response("ConnectedFlight updated", HTTPStatus.OK)


@connected_flight_bp.delete('/<int:connected_flight_id>')
def delete_description(connected_flight_id: int) -> Response:
    connected_flight.delete(connected_flight_id)
    return make_response("ConnectedFlight deleted", HTTPStatus.OK)
