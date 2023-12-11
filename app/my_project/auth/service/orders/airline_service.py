from my_project.auth.dao.orders import airline_dao
from my_project.auth.service.general_service import GeneralService


class AirlineService(GeneralService):
    _dao = airline_dao.AirlineDAO()

    def get_all_airport(self, airline_id):
        return self._dao.get_all_airport(airline_id)

    def get_all_available_flights(self, airline_id):
        return self._dao.get_all_available_flights(airline_id)

    def get_all_connected_flight(self, airline_id):
        return self._dao.get_all_connected_flight(airline_id)

    def insert_airline(self, p_name):
        return self._dao.insert_airline(p_name)

    def insert_no_name(self):
        return self._dao.insert_no_name()
