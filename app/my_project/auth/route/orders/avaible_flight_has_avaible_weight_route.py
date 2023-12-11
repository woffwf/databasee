from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.available_flights_has_avaible_weight_controller import \
    AvailableFlightsHasAvaibleWeightController
from my_project.auth.domain.orders.avaible_flight import AvailableFlight
from my_project.auth.domain.orders.avaible_flight_has_avaible_weight import AvailableFlightsHasAvaibleWeight
from my_project.auth.domain.orders.available_flight_and_available_weight import AvailableFlightAndAvailableWeight

avaible_flight_has_avaible_weight_bp = Blueprint('avaible_flight_has_avaible_weight', __name__,
                                                 url_prefix='/avaible_flight_has_avaible_weight')
avaible_flight_has_avaible_weight = AvailableFlightsHasAvaibleWeightController()


@avaible_flight_has_avaible_weight_bp.get('')
def get_all_avaible_flight_has_avaible_weight() -> Response:
    return make_response(jsonify(avaible_flight_has_avaible_weight.find_all()), HTTPStatus.OK)


@avaible_flight_has_avaible_weight_bp.post('')
def create_avaible_flight_has_avaible_weight() -> Response:
    content = request.get_json()
    avaible_flight_has_avaible_weight.insert_data_procedure(content.get("way"), content.get("price"),
                                                            content.get("weight"),
                                                            content.get("dimensions"), content.get("date_time"),
                                                            content.get("airline_id"),
                                                            content.get("type_of_fly"), content.get("avaible_seats"))
    return make_response("AvailableFlightsHasAvaibleWeight created", HTTPStatus.CREATED)


@avaible_flight_has_avaible_weight_bp.get('/<int:avaible_flight_has_avaible_weight_id>')
def get_avaible_flight_has_avaible_weight(avaible_flight_has_avaible_weight_id: int) -> Response:
    return make_response(jsonify(avaible_flight_has_avaible_weight.find_by_id(avaible_flight_has_avaible_weight_id)),
                         HTTPStatus.OK)


@avaible_flight_has_avaible_weight_bp.put('/<int:avaible_flight_has_avaible_weight_id>')
def update_avaible_flight_has_avaible_weight(avaible_flight_has_avaible_weight_id: int) -> Response:
    avaible_flight_has_avaible_weight.update(avaible_flight_has_avaible_weight_id,
                                             AvailableFlightsHasAvaibleWeight.create_from_dto(request.get_json()))
    return make_response("AvailableFlightsHasAvaibleWeight updated", HTTPStatus.OK)


@avaible_flight_has_avaible_weight_bp.patch('/<int:avaible_flight_has_avaible_weight_id>')
def patch_avaible_flight_has_avaible_weight(avaible_flight_has_avaible_weight_id: int) -> Response:
    avaible_flight_has_avaible_weight.patch(avaible_flight_has_avaible_weight_id, request.get_json())
    return make_response("AvailableFlightsHasAvaibleWeight updated", HTTPStatus.OK)


@avaible_flight_has_avaible_weight_bp.delete('/<int:avaible_flight_has_avaible_weight_id>')
def delete_avaible_flight_has_avaible_weight(avaible_flight_has_avaible_weight_id: int) -> Response:
    avaible_flight_has_avaible_weight.delete(avaible_flight_has_avaible_weight_id)
    return make_response("AvailableFlightsHasAvaibleWeight deleted", HTTPStatus.OK)


@avaible_flight_has_avaible_weight_bp.get('/all_data')
def get_all_data():
    availables = AvailableFlight.query.all()
    massive = []
    for available in availables:
        for weight in available.avaible_weights:
            massive.append(AvailableFlightAndAvailableWeight(available.way, available.price, weight.weight,
                                                             weight.dimensions).put_into_dto())

    return make_response(jsonify(massive), HTTPStatus.OK)
