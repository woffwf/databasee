from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller.orders.info_for_buyed_tickets_controller import InfoForBuyedTicketsController
from my_project.auth.domain.orders.info_for_buyed_tickets import InfoForBuyedTickets

info_for_buyed_tickets_bp = Blueprint('info_for_buyed_tickets', __name__, url_prefix='/info_for_buyed_tickets')
info_for_buyed_tickets = InfoForBuyedTicketsController()


@info_for_buyed_tickets_bp.get('')
def get_all_info_for_buyed_tickets() -> Response:
    return make_response(jsonify(info_for_buyed_tickets.find_all()), HTTPStatus.OK)


@info_for_buyed_tickets_bp.post('')
def create_info_for_buyed_tickets() -> Response:
    content = request.get_json()
    return make_response(jsonify(info_for_buyed_tickets.create(InfoForBuyedTickets.create_from_dto(content))), HTTPStatus.CREATED)


@info_for_buyed_tickets_bp.get('/<int:info_for_buyed_tickets_id>')
def get_info_for_buyed_tickets(info_for_buyed_tickets_id: int) -> Response:
    return make_response(jsonify(info_for_buyed_tickets.find_by_id(info_for_buyed_tickets_id)), HTTPStatus.OK)


@info_for_buyed_tickets_bp.put('/<int:info_for_buyed_tickets_id>')
def update_info_for_buyed_tickets(info_for_buyed_tickets_id: int) -> Response:
    info_for_buyed_tickets.update(info_for_buyed_tickets_id, InfoForBuyedTickets.create_from_dto(request.get_json()))
    return make_response("Review updated", HTTPStatus.OK)


@info_for_buyed_tickets_bp.patch('/<int:info_for_buyed_tickets_id>')
def patch_info_for_buyed_tickets(info_for_buyed_tickets_id: int) -> Response:
    info_for_buyed_tickets.patch(info_for_buyed_tickets_id, request.get_json())
    return make_response("InfoForBuyedTickets updated", HTTPStatus.OK)


@info_for_buyed_tickets_bp.delete('/<int:info_for_buyed_tickets_id>')
def delete_info_for_buyed_tickets(info_for_buyed_tickets_id: int) -> Response:
    info_for_buyed_tickets.delete(info_for_buyed_tickets_id)
    return make_response("InfoForBuyedTickets deleted", HTTPStatus.OK)
