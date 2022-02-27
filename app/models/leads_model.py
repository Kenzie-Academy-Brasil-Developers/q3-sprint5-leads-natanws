from datetime import datetime
from re import fullmatch
from sqlalchemy import Column, Integer, String, DateTime
from app.configs.database import db
from werkzeug.exceptions import BadRequest

class LeadModel(db.Model):
    
    __tablename__ = 'leads'

    id: int
    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: str
    visits: int

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    creation_date = Column(DateTime, nullable=False, default=datetime.now())
    last_visit = Column(DateTime, nullable=False, default=datetime.now())
    visits = Column(Integer, nullable=False, default=1)

    @staticmethod
    def serialize(data):
        serialized_data = [{
            'id': lead.id,
            'name': lead.name,
            'email': lead.email,
            'phone': lead.phone,
            'creation_date': lead.creation_date,
            'last_visit': lead.last_visit,
            'visits': lead.visits
        } for lead in data]

        return serialized_data

    @staticmethod
    def validate_phone(phone):
        regex = '\([0-9]{2}\)[0-9]{5}\-[0-9]{4}'

        if not fullmatch(regex, phone):
            raise BadRequest('phone format')

    @staticmethod
    def check_fields(required_fields, data):
        for key in data.keys():
            if not key in required_fields:
                raise BadRequest('fields')
        for value in data.values():
            if value != str:
                raise TypeError