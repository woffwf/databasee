from __future__ import annotations
from typing import Dict, Any

from my_project import db


class Tickets(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    purchase_time = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    available_flights_id = db.Column(db.Integer, db.ForeignKey("available_flights.id"), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", backref=db.backref("tickets", lazy=True))
    available_flights = db.relationship("AvailableFlight", backref=db.backref("tickets", lazy=True))

    def __repr__(self) -> str:
        return f"Tickets({self.id}, {self.purchase_time}, {self.user_id}, {self.available_flights_id}, {self.cost}, {self.seat_number})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "purchase_time": self.purchase_time.isoformat() if self.purchase_time else None,  # Convert datetime to ISO format
            "user_id": self.user_id,
            "available_flights_id": self.available_flights_id,
            "cost": self.cost,
            "seat_number": self.seat_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Tickets:
        obj = Tickets(
            purchase_time=dto_dict.get("purchase_time"),
            user_id=dto_dict.get("user_id"),
            available_flights_id=dto_dict.get("available_flights_id"),
            cost=dto_dict.get("cost"),
            seat_number=dto_dict.get("seat_number"),
        )
        return obj
