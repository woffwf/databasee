from my_project.auth.service.orders import user_service
from my_project.auth.controller.general_controller import GeneralController


class UserController(GeneralController):
    _service = user_service.UserService()

    def get_all_tickets(self, user_id):
        return self._service.get_all_tickets(user_id)

    def get_purchase_history(self, user_id):
        return self._service.get_purchase_history(user_id)
