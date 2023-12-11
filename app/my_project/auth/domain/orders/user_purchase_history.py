from __future__ import annotations
from typing import Dict, Any

from my_project import db


class UserPurchaseHistory(db.Model):
    __tablename__ = "user_purchase_history"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    purchase_time = db.Column(db.DateTime, nullable=True)
    price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    tickets_id = db.Column(db.Integer, db.ForeignKey("tickets.id"), nullable=False)

    user = db.relationship("User", backref=db.backref("purchase_history", lazy=True))
    tickets = db.relationship("Tickets", backref=db.backref("purchase_history", lazy=True))

    def __repr__(self) -> str:
        return f"UserPurchaseHistory({self.id}, {self.purchase_time}, {self.price}, {self.user_id}, {self.tickets_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "purchase_time": self.purchase_time.isoformat() if self.purchase_time else None,  # Convert datetime to ISO format
            "price": self.price,
            "user_id": self.user_id,
            "tickets_id": self.tickets_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UserPurchaseHistory:
        obj = UserPurchaseHistory(
            purchase_time=dto_dict.get("purchase_time"),
            price=dto_dict.get("price"),
            user_id=dto_dict.get("user_id"),
            tickets_id=dto_dict.get("tickets_id"),
        )
        return obj
