from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.user_purchase_history import UserPurchaseHistory


class UserPurchaseHistoryDAO(GeneralDAO):
    _domain_type = UserPurchaseHistory

    def find_all(self):
        return UserPurchaseHistory.query.all()
