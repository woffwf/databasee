from my_project.auth.dao.orders import user_dao
from my_project.auth.service.general_service import GeneralService


class UserService(GeneralService):
    _dao = user_dao.UserDAO()

    def get_all_tickets(self, user_id):
        return self._dao.get_all_tickets(user_id)

    def get_purchase_history(self, user_id):
        return self._dao.get_purchase_history(user_id)
