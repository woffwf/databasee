from my_project.auth.service.orders import available_flight_service
from my_project.auth.controller.general_controller import GeneralController


class AvailableFlightController(GeneralController):
    _service = available_flight_service.AvailableFlightSevice()

    def get_all_available_flights(self, available_flight_id):
        self._service.get_all_available_flights(available_flight_id)

    def get_statistic(self):
        return self._service.get_statistic()

    def available_flights(self, available_flight_id):
        return self._service.available_flights(available_flight_id)
