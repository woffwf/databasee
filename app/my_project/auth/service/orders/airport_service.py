from my_project.auth.dao.orders import airport_dao
from my_project.auth.service.general_service import GeneralService


class AirportService(GeneralService):
    _dao = airport_dao.AirportDAO()

    def get_connected_flight(self, airport_id):
        return self._dao.get_connected_flight(airport_id)
