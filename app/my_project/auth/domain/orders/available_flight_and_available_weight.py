from typing import Dict, Any


class AvailableFlightAndAvailableWeight:
    def __init__(self, way, price, weight, dimensions):
        self.way = way
        self.price = price
        self.weight = weight
        self.dimensions = dimensions

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "way": self.way,
            "price": self.price,
            "weight": self.weight,
            "dimensions": self.dimensions
        }
