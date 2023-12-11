from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.airport import Airport
from my_project.auth.domain.orders.connected_flight import ConnectedFlight


class AirportDAO(GeneralDAO):
    _domain_type = Airport

    def find_all(self):
        return Airport.query.all()

    def get_connected_flight(self, airport_id):
        return (self._session.query(ConnectedFlight).filter(ConnectedFlight.airoport_id == airport_id)
                .order_by(ConnectedFlight.airoport_id).all())
