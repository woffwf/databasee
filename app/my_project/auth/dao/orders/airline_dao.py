from typing import List

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.airline import Airline
from my_project.auth.domain.orders.airport import Airport
from my_project.auth.domain.orders.avaible_flight import AvailableFlight
from my_project.auth.domain.orders.connected_flight import ConnectedFlight


class AirlineDAO(GeneralDAO):
    _domain_type = Airline

    def find_all(self):
        return Airline.query.all()

    def get_all_airport(self, airline_id) -> List[Airport]:
        return self._session.query(Airport).filter(Airport.airline_id == airline_id).order_by(Airport.airline_id).all()

    def get_all_available_flights(self, airline_id) -> List[AvailableFlight]:
        return (self._session.query(AvailableFlight).filter(AvailableFlight.airline_id == airline_id)
                .order_by(AvailableFlight.airline_id).all())

    def get_all_connected_flight(self, airline_id) -> List[ConnectedFlight]:
        return (self._session.query(ConnectedFlight).filter(ConnectedFlight.airline_id == airline_id)
                .order_by(ConnectedFlight.airline_id).all())

    def insert_airline(self, p_name):
        params = {"p_name": p_name}

        self._session.begin()
        result = self._session.execute(sqlalchemy.text(f"CALL insert_airline(:p_name)"),
                                       params).mappings().all()
        self._session.commit()
        return result

    def insert_no_name(self):
        self._session.begin()
        result = self._session.execute(sqlalchemy.text(f"CALL insert_noname_airline()")).mappings().all()
        self._session.commit()
        return result
