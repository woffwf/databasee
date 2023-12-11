from my_project.auth.service.orders import info_for_buyed_tickets_service
from my_project.auth.controller.general_controller import GeneralController


class InfoForBuyedTicketsController(GeneralController):
    _service = info_for_buyed_tickets_service.InfoForBuyedTicketsService()
