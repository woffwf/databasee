from datetime import date
from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.connected_flight import ConnectedFlight


class ConnectedFlightDAO(GeneralDAO):
    _domain_type = ConnectedFlight

    def find_all(self):
        return ConnectedFlight.query.all()
