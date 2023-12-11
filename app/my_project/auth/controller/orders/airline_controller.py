from my_project.auth.service.orders import airline_service
from my_project.auth.controller.general_controller import GeneralController


class AirlineController(GeneralController):
    _service = airline_service.AirlineService()

    def get_all_airport(self, airline_id):
        return self._service.get_all_airport(airline_id)

    def get_all_available_flights(self, airline_id):
        return self._service.get_all_available_flights(airline_id)

    def get_all_connected_flight(self, airline_id):
        return self._service.get_all_connected_flight(airline_id)

    def insert_airline(self, p_name):
        return self._service.insert_airline(p_name)

    def insert_no_name(self):
        return self._service.insert_no_name()
