from sqlalchemy import text

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.avaible_flight_has_avaible_weight import AvailableFlightsHasAvaibleWeight


class AvailableFlightsHasAvaibleWeightDAO(GeneralDAO):
    _domain_type = AvailableFlightsHasAvaibleWeight

    def find_all(self):
        return AvailableFlightsHasAvaibleWeight.query.all()

    def insert_data_procedure(self, param, param1, param2, param3, param4, param5, param6, param7):
        query = text(
            "CALL insert_data_procedure(:way, :price, :weight,:dimensions, :date_time, :airline_id, :type_of_fly, :avaible_seats)")

        self._session.begin()
        self._session.execute(query, {"way": param, "price": param1, "weight": param2, "dimensions": param3,
                                      "date_time": param4, "airline_id": param5, "type_of_fly": param6,
                                      "avaible_seats": param7})
        self._session.commit()
