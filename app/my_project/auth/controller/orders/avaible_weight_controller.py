from my_project.auth.service.orders import avaible_weight_service
from my_project.auth.controller.general_controller import GeneralController


class AvaibleWeightController(GeneralController):
    _service = avaible_weight_service.AvaibleWeightService()
