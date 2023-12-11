from my_project.auth.dao.orders import info_for_buyed_tickets_dao
from my_project.auth.service.general_service import GeneralService


class InfoForBuyedTicketsService(GeneralService):
    _dao = info_for_buyed_tickets_dao.InfoForBuyedTicketsDAO()
