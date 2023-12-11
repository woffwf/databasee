from my_project.auth.dao.orders import connected_flight_dao
from my_project.auth.service.general_service import GeneralService


class ConnectedFlightService(GeneralService):
    _dao = connected_flight_dao.ConnectedFlightDAO()
