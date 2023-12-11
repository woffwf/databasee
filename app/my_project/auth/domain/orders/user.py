from __future__ import annotations
from typing import Dict, Any

from my_project import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    age = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"User({self.id}, '{self.name}', '{self.surname}', '{self.age}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        obj = User(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            age=dto_dict.get("age"),
        )
        return obj
