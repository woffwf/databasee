from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Airport(db.Model, IDto):
    __tablename__ = "airoport"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    airline_id = db.Column(db.Integer, db.ForeignKey("airline.id"), nullable=False)
    country = db.Column(db.String(45), nullable=False)
    avaible = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String(45), nullable=False)

    airline = db.relationship("Airline", backref="airoport", lazy=True)

    def __repr__(self) -> str:
        return f"Airport({self.id}, {self.airline_id}, '{self.country}', {self.avaible}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "airline_id": self.airline_id,
            "country": self.country,
            "available": self.avaible,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> "Airport":
        obj = Airport(
            airline_id=dto_dict.get("airline_id"),
            country=dto_dict.get("country"),
            available=dto_dict.get("avaible"),
            name=dto_dict.get("name")
        )
        return obj