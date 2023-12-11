from .orders.available_flight_dao import AvailableFlightDAO
from .orders.airline_dao import AirlineDAO
from .orders.avaible_weight_dao import AvaibleWeightDao
from .orders.airport_dao import AirportDAO
from .orders.user_dao import UserDAO
from .orders.info_for_buyed_tickets_dao import InfoForBuyedTicketsDAO
from .orders.tickets_dao import TicketsDAO
from .orders.user_purchase_history_dao import UserPurchaseHistoryDAO
from .orders.available_flights_has_avaible_weight_dao import AvailableFlightsHasAvaibleWeightDAO
from .orders.connected_flight_dao import ConnectedFlightDAO

available_flight_dao = AvailableFlightDAO()
airline_dao = AirlineDAO()
avaible_weight_dao = AvaibleWeightDao()
airport_dao = AirportDAO()
user_dao = UserDAO()
info_for_buyed_tickets_dao = InfoForBuyedTicketsDAO()
tickets_dao = TicketsDAO()
user_purchase_history_dao = UserPurchaseHistoryDAO()
available_flights_has_avaible_weight_dao = AvailableFlightsHasAvaibleWeightDAO()
connected_flight_dao = ConnectedFlightDAO()
