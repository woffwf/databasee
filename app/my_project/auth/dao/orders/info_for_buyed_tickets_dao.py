from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.info_for_buyed_tickets import InfoForBuyedTickets


class InfoForBuyedTicketsDAO(GeneralDAO):
    """
    Realisation of FilmHasRating data access layer.
    """
    _domain_type = InfoForBuyedTickets

    def find_all(self):
        return InfoForBuyedTickets.query.all()
