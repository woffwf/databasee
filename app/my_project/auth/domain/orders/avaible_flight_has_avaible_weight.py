from __future__ import annotations
from typing import Dict, Any

from my_project import db


class AvailableFlightsHasAvaibleWeight(db.Model):
    __tablename__ = "available_flights_has_avaible_weight"

    available_flights_id = db.Column(db.Integer, db.ForeignKey("available_flights.id"), primary_key=True)
    avaible_weight_id = db.Column(db.Integer, db.ForeignKey("avaible_weight.id"), primary_key=True)

    def __repr__(self) -> str:
        return f"AvailableFlightsHasAvaibleWeight({self.available_flights_id}, {self.avaible_weight_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "available_flights_id": self.available_flights_id,
            "avaible_weight_id": self.avaible_weight_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AvailableFlightsHasAvaibleWeight:
        obj = AvailableFlightsHasAvaibleWeight(
            available_flights_id=dto_dict.get("available_flights_id"),
            avaible_weight_id=dto_dict.get("avaible_weight_id"),
        )
        return obj