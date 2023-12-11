from my_project.auth.dao.orders import user_purchase_history_dao
from my_project.auth.service.general_service import GeneralService


class UserPurchaseHistoryService(GeneralService):
    _dao = user_purchase_history_dao.UserPurchaseHistoryDAO()
