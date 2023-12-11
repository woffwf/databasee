from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.tickets import Tickets
from my_project.auth.domain.orders.user import User
from my_project.auth.domain.orders.user_purchase_history import UserPurchaseHistory


class UserDAO(GeneralDAO):
    _domain_type = User

    def find_all(self):
        return User.query.all()

    def get_all_tickets(self, user_id):
        return (self._session.query(Tickets).filter(Tickets.user_id == user_id)
                .order_by(Tickets.user_id).all())

    def get_purchase_history(self, user_id):
        return (self._session.query(UserPurchaseHistory).filter(UserPurchaseHistory.user_id == user_id)
                .order_by(UserPurchaseHistory.user_id).all())
