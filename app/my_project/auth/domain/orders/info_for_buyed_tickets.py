from __future__ import annotations
from typing import Dict, Any

from my_project import db


class InfoForBuyedTickets(db.Model):
    __tablename__ = "info_for_buyed_tickets"

    purchase_time = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(45), nullable=False)
    id = db.Column(db.String(45), primary_key=True)
    tickets_id = db.Column(db.Integer, db.ForeignKey("tickets.id"), primary_key=True)

    user = db.relationship("User", backref=db.backref("info_for_buyed_tickets", lazy=True))
    tickets = db.relationship("Tickets", backref=db.backref("info_for_buyed_tickets", lazy=True))

    def __repr__(self) -> str:
        return f"InfoForBuyedTickets({self.purchase_time}, {self.user_id}, {self.seat_number}, '{self.status}', '{self.id}', {self.tickets_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "purchase_time": self.purchase_time.isoformat(),  # Convert date to ISO format
            "user_id": self.user_id,
            "seat_number": self.seat_number,
            "status": self.status,
            "id": self.id,
            "tickets_id": self.tickets_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> InfoForBuyedTickets:
        obj = InfoForBuyedTickets(
            purchase_time=dto_dict.get("purchase_time"),
            user_id=dto_dict.get("user_id"),
            seat_number=dto_dict.get("seat_number"),
            status=dto_dict.get("status"),
            id=dto_dict.get("id"),
            tickets_id=dto_dict.get("tickets_id"),
        )
        return obj
