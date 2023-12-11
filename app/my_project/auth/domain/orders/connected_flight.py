from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class ConnectedFlight(db.Model, IDto):
    __tablename__ = "connected_flight"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    available_flights_id = db.Column(db.Integer, db.ForeignKey("available_flights.id"), nullable=False)
    airline_id = db.Column(db.Integer, db.ForeignKey("airline.id"), nullable=False)
    airoport_id = db.Column(db.Integer, db.ForeignKey("airoport.id"), nullable=False)
    duration = db.Column(db.Integer, nullable=True)
    arrival_time = db.Column(db.Integer, nullable=False)

    available_flights = db.relationship("AvailableFlight", backref=db.backref("connected_flight", lazy=True))
    airline = db.relationship("Airline", backref=db.backref("connected_flights", lazy=True))
    airport = db.relationship("Airport", backref=db.backref("connected_flights", lazy=True))

    def __repr__(self) -> str:
        return f"ConnectedFlight({self.id}, {self.available_flights_id}, {self.airline_id}, {self.airoport_id}, {self.duration}, {self.arrival_time})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "available_flights_id": self.available_flights_id,
            "airline_id": self.airline_id,
            "airoport_id": self.airoport_id,
            "duration": self.duration,
            "arrival_time": self.arrival_time,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ConnectedFlight:
        obj = ConnectedFlight(
            available_flights_id=dto_dict.get("available_flights_id"),
            airline_id=dto_dict.get("airline_id"),
            airoport_id=dto_dict.get("airoport_id"),
            duration=dto_dict.get("duration"),
            arrival_time=dto_dict.get("arrival_time"),
        )
        return obj
