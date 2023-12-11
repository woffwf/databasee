from my_project.auth.dao.orders import available_flight_dao
from my_project.auth.service.general_service import GeneralService


class AvailableFlightSevice(GeneralService):
    _dao = available_flight_dao.AvailableFlightDAO()

    def get_all_available_flights(self, available_flight_id):
        self._dao.get_all_available_flights(available_flight_id)

    def get_statistic(self):
        return self._dao.get_statistic()

    def available_flights(self, available_flight_id):
        self._dao.available_flights(available_flight_id)

