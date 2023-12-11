from my_project.auth.dao.orders import airline_dao, additional_dao
from my_project.auth.service.general_service import GeneralService


class AdditionalService(GeneralService):
    _dao = additional_dao.AdditionalDAO()
