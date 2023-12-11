from my_project.auth.service.orders import tickets_service
from my_project.auth.controller.general_controller import GeneralController


class TicketsController(GeneralController):
    _service = tickets_service.TicketsService()

    def get_purchase_history(self, tickets_id):
        return self._service.get_purchase_history(tickets_id)
