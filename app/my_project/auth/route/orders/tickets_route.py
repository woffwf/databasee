from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.tickets_controller import TicketsController
from my_project.auth.domain.orders.tickets import Tickets

tickets_bp = Blueprint('tickets', __name__, url_prefix='/tickets')
tickets = TicketsController()


@tickets_bp.get('')
def get_all_tickets() -> Response:
    return make_response(jsonify(tickets.find_all()), HTTPStatus.OK)


@tickets_bp.post('')
def create_tickets() -> Response:
    content = request.get_json()
    return make_response(jsonify(tickets.create(Tickets.create_from_dto(content))), HTTPStatus.CREATED)


@tickets_bp.get('/<int:tickets_id>')
def get_tickets(tickets_id: int) -> Response:
    return make_response(jsonify(tickets.find_by_id(tickets_id)), HTTPStatus.OK)


@tickets_bp.put('/<int:tickets_id>')
def update_tickets(genre_id: int) -> Response:
    tickets.update(genre_id, Tickets.create_from_dto(request.get_json()))
    return make_response("Tickets updated", HTTPStatus.OK)


@tickets_bp.patch('/<int:tickets_id>')
def patch_tickets(tickets_id: int) -> Response:
    tickets.patch(tickets_id, request.get_json())
    return make_response("Tickets updated", HTTPStatus.OK)


@tickets_bp.delete('/<int:tickets_id>')
def delete_tickets(tickets_id: int) -> Response:
    tickets.delete(tickets_id)
    return make_response("Tickets deleted", HTTPStatus.OK)


@tickets_bp.get('/<int:tickets_id>/purchase_history')
def get_purchase_history(tickets_id: int):
    result = tickets.get_purchase_history(tickets_id)
    result = [row.put_into_dto() for row in result]

    return make_response(jsonify(result), HTTPStatus.OK)
