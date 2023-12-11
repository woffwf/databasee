from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Airline(db.Model, IDto):
    __tablename__ = "airline"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), index=True)

    def __repr__(self) -> str:
        return f"Actor({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Airline:
        obj = Airline(
            name=dto_dict.get("name")
        )
        return obj
