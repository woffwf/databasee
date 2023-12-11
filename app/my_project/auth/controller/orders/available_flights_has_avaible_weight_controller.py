from my_project.auth.service.orders import available_flights_has_avaible_weight_service
from my_project.auth.controller.general_controller import GeneralController


class AvailableFlightsHasAvaibleWeightController(GeneralController):
    _service = available_flights_has_avaible_weight_service.AvailableFlightsHasAvaibleWeightService()

    def insert_data_procedure(self, param, param1, param2, param3, param4, param5, param6, param7):
        return self._service.insert_data_procedure(param, param1, param2, param3,param4, param5, param6,param7)
