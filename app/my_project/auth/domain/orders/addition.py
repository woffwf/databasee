from typing import Dict, Any

from my_project import db


class AdditionalTable(db.Model):
    __tablename__ = "additional"

    additional_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    additional_data = db.Column(db.String(255), nullable=False)
    airline_id = db.Column(db.Integer, db.ForeignKey('airline.id'), nullable=False)
    airline = db.relationship('Airline', backref=db.backref('additional_data', lazy=True))

    def __repr__(self) -> str:
        return f"AdditionalTable({self.additional_id}, '{self.additional_data}', {self.airline_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.additional_id,
            "additional_data": self.additional_data,
            "airline_id": self.airline_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = AdditionalTable(
            additional_data=dto_dict.get("additional_data"),
            airline_id=dto_dict.get("airline_id")
        )
        return obj
