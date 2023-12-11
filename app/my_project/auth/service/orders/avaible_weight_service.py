from my_project.auth.dao.orders import avaible_weight_dao
from my_project.auth.service.general_service import GeneralService


class AvaibleWeightService(GeneralService):
    _dao = avaible_weight_dao.AvaibleWeightDao()
