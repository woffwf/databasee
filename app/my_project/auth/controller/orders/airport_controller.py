from my_project.auth.service.orders import airport_service
from my_project.auth.controller.general_controller import GeneralController


class AirportController(GeneralController):
    _service = airport_service.AirportService()

    def get_connected_flight(self, airport_id):
        return self._service.get_connected_flight(airport_id)
