from my_project.auth.dao.orders import available_flights_has_avaible_weight_dao
from my_project.auth.service.general_service import GeneralService


class AvailableFlightsHasAvaibleWeightService(GeneralService):
    _dao = available_flights_has_avaible_weight_dao.AvailableFlightsHasAvaibleWeightDAO()

    def insert_data_procedure(self, param, param1, param2, param3, param4, param5, param6, param7):
        return self._dao.insert_data_procedure(param, param1, param2, param3, param4, param5, param6, param7)
