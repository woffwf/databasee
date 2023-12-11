from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.orders import additional_service


class AdditionalController(GeneralController):
    _service = additional_service.AdditionalService()
