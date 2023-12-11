from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.tickets import Tickets
from my_project.auth.domain.orders.user_purchase_history import UserPurchaseHistory


class TicketsDAO(GeneralDAO):
    _domain_type = Tickets

    def find_all(self):
        return Tickets.query.all()

    def get_purchase_history(self, tickets_id):
        return (self._session.query(UserPurchaseHistory).filter(UserPurchaseHistory.tickets_id == tickets_id)
                .order_by(UserPurchaseHistory.tickets_id).all())
