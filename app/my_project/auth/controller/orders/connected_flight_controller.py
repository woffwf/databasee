from my_project.auth.service.orders import connected_flight_service
from my_project.auth.controller.general_controller import GeneralController


class ConnectedFlightController(GeneralController):
    _service = connected_flight_service.ConnectedFlightService()
