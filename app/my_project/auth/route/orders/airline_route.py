from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders import airline_controller
from my_project.auth.domain.orders.airline import Airline

airline_bp = Blueprint('airline', __name__, url_prefix='/airline')
airline = airline_controller.AirlineController()


@airline_bp.get('')
def get_all_airline() -> Response:
    return make_response(jsonify(airline.find_all()), HTTPStatus.OK)


@airline_bp.post('')
def create_airline() -> Response:
    content = request.get_json()
    return make_response(jsonify(airline.create(Airline.create_from_dto(content))), HTTPStatus.CREATED)


@airline_bp.get('/<int:airline_id>')
def get_airline(airline_id: int) -> Response:
    return make_response(jsonify(airline.find_by_id(airline_id)), HTTPStatus.OK)


@airline_bp.put('/<int:airline_id>')
def update_airline(airline_id: int) -> Response:
    content = request.get_json()
    airline.update(airline_id, Airline.create_from_dto(content))
    return make_response("Airline updated", HTTPStatus.OK)


@airline_bp.patch('/<int:airline_id>')
def patch_airline(airline_id: int) -> Response:
    content = request.get_json()
    airline.patch(airline_id, content)
    return make_response("Airline updated", HTTPStatus.OK)


@airline_bp.delete('/<int:airline_id>')
def delete_airline(airline_id: int) -> Response:
    airline.delete(airline_id)
    return make_response("Airline deleted", HTTPStatus.OK)


@airline_bp.get('/<int:airline_id>/airport')
def get_all_airport(airline_id: int) -> Response:
    result = airline.get_all_airport(airline_id)
    result = [row.put_into_dto() for row in result]

    return make_response(jsonify(result), HTTPStatus.OK)


@airline_bp.get('/<int:airline_id>/available_flights')
def get_all_available_flights(airline_id: int) -> Response:
    result = airline.get_all_available_flights(airline_id)
    result = [row.put_into_dto() for row in result]

    return make_response(jsonify(result), HTTPStatus.OK)


@airline_bp.get('/<int:airline_id>/connected_flight')
def get_all_connected_flight(airline_id: int) -> Response:
    result = airline.get_all_connected_flight(airline_id)
    result = [row.put_into_dto() for row in result]

    return make_response(jsonify(result), HTTPStatus.OK)


@airline_bp.post('/insert')
def insert_airline():
    data = request.get_json()
    p_name = data.get('name')

    result = airline.insert_airline(p_name)
    formatted_result = [{"id": row["id"], "name": row["name"]} for row in result]
    return make_response(jsonify(formatted_result), HTTPStatus.OK)


@airline_bp.post('/no_name')
def insert_no_name():
    result = airline.insert_no_name()
    result = [row.put_into_dto() for row in result]

    return make_response(jsonify(result), HTTPStatus.OK)
