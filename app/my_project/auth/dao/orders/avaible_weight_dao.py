from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.avaible_weight import AvaibleWeight


class AvaibleWeightDao(GeneralDAO):
    _domain_type = AvaibleWeight

    def find_all(self):
        return AvaibleWeight.query.all()
