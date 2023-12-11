from my_project.auth.dao.orders import tickets_dao
from my_project.auth.service.general_service import GeneralService


class TicketsService(GeneralService):
    _dao = tickets_dao.TicketsDAO()

    def get_purchase_history(self, tickets_id):
        return self._dao.get_purchase_history(tickets_id)
