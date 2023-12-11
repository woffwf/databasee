from my_project.auth.service.orders import user_purchase_history_service
from my_project.auth.controller.general_controller import GeneralController


class UserPurchaseHistoryController(GeneralController):
    _service = user_purchase_history_service.UserPurchaseHistoryService()
