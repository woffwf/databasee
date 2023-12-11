from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class AvailableFlight(db.Model, IDto):
    __tablename__ = "available_flights"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    way = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=True)
    airline_id = db.Column(db.Integer, nullable=False)
    type_of_fly = db.Column(db.String(45), nullable=False)
    avaible_seats = db.Column(db.Integer, nullable=False)
    avaible_weights = db.relationship('AvaibleWeight', secondary='available_flights_has_avaible_weight',
                                      back_populates='available_flights')

    def __repr__(self) -> str:
        return f"AvailableFlight({self.id}, '{self.way}', {self.price}, {self.time}, {self.airline_id}, '{self.type_of_fly}', {self.avaible_seats})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "way": self.way,
            "price": self.price,
            "time": self.time,
            "airline_id": self.airline_id,
            "type_of_fly": self.type_of_fly,
            "available_seats": self.avaible_seats,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AvailableFlight:
        obj = AvailableFlight(
            way=dto_dict.get("way"),
            price=dto_dict.get("price"),
            time=dto_dict.get("time"),
            airline_id=dto_dict.get("airline_id"),
            type_of_fly=dto_dict.get("type_of_fly"),
            available_seats=dto_dict.get("avaible_seats"),
        )
        return obj
