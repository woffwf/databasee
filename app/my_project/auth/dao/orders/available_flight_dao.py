import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.avaible_flight import AvailableFlight
from my_project.auth.domain.orders.connected_flight import ConnectedFlight
from my_project.auth.domain.orders.tickets import Tickets


class AvailableFlightDAO(GeneralDAO):
    _domain_type = AvailableFlight

    def find_all(self):
        return AvailableFlight.query.all()

    def get_all_available_flights(self, available_flight_id):
        return (self._session.query(ConnectedFlight).filter(ConnectedFlight.available_flights == available_flight_id)
                .order_by(ConnectedFlight.airline_id).all())

    def get_statistic(self):
        return self._session.execute(sqlalchemy.text(f"CALL get_available_flights_statistics()")).mappings().all()

    def available_flights(self, available_flight_id):
        return (self._session.query(Tickets).filter(Tickets.available_flights_id == available_flight_id)
                .order_by(Tickets.available_flights_id).all())
