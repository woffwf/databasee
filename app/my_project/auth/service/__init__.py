from .orders.available_flight_service import AvailableFlightSevice
from .orders.airline_service import AirlineService
from .orders.user_service import UserService
from .orders.airport_service import AirportService
from .orders.tickets_service import TicketsService
from .orders.avaible_weight_service import AvaibleWeightService
from .orders.available_flights_has_avaible_weight_service import AvailableFlightsHasAvaibleWeightService
from .orders.connected_flight_service import ConnectedFlightService
from .orders.info_for_buyed_tickets_service import InfoForBuyedTicketsService
from .orders.user_purchase_history_service import UserPurchaseHistoryService

available_flight_service = AvailableFlightSevice()
airline_service = AirlineService()
user_service = UserService()
airport_service = AirportService()
tickets_service = TicketsService()
avaible_weight_service = AvaibleWeightService()
available_flights_has_avaible_weight_service = AvailableFlightsHasAvaibleWeightService()
connected_flight_service = ConnectedFlightService()
info_for_buyed_tickets_service = InfoForBuyedTicketsService()
user_purchase_history_service = UserPurchaseHistoryService()
