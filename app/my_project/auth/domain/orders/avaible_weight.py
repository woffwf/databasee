from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class AvaibleWeight(db.Model, IDto):
    __tablename__ = "avaible_weight"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weight = db.Column(db.Integer, nullable=False)
    dimensions = db.Column(db.Integer, nullable=False)
    available_flights = db.relationship('AvailableFlight', secondary='available_flights_has_avaible_weight',
                                        back_populates='avaible_weights')

    def __repr__(self) -> str:
        return f"AvaibleWeight({self.id}, {self.weight}, {self.dimensions})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "weight": self.weight,
            "dimensions": self.dimensions,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AvaibleWeight:
        obj = AvaibleWeight(
            weight=dto_dict.get("weight"),
            dimensions=dto_dict.get("dimensions"),
        )
        return obj
