from datetime import datetime
from http import HTTPStatus
from flask import jsonify, request, current_app
from app.models.leads_model import LeadModel
from werkzeug.exceptions import BadRequest, NotFound
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

def create_lead():
    try:
        data = request.get_json()

        print(data)

        required_fields = ['name', 'email', 'phone']
        LeadModel.check_fields(required_fields, data)

        LeadModel.validate_phone(data['phone'])

        lead = LeadModel(**data)

        current_app.db.session.add(lead)
        current_app.db.session.commit()

        return jsonify(lead), HTTPStatus.CREATED
    
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            return {'error': 'Email e telefone devem ser únicos'}, HTTPStatus.CONFLICT
    
    except BadRequest as e:
        if e.__dict__['description'] == 'phone format':
            return {'error': 'Formatação incorreta de telefone. Esperado (XX)XXXXX-XXXX'}, HTTPStatus.BAD_REQUEST
        if e.__dict__['description'] == 'fields':
            return {'error': "Apenas utilizar campos 'name', 'email' e 'phone'"}, HTTPStatus.BAD_REQUEST
    
    except TypeError as e:
        print(e)
        return {'error': "Todos campos devem ser string"}, HTTPStatus.BAD_REQUEST
        
        
def get_leads():
    try:
        leads_data = LeadModel.query.all()
        
        if len(leads_data) == 0:
            raise NotFound
        
        return jsonify(leads_data), HTTPStatus.OK
    
    except NotFound:
        return {"error": "Nenhuma lead cadastrada"}, HTTPStatus.NOT_FOUND

def update_lead():
    try:
        data = request.get_json()

        required_fields = ['email']
        LeadModel.check_fields(required_fields, data)
        
        lead = LeadModel.query.filter_by(email=data['email']).first()

        if lead == None:
            raise NotFound


        setattr(lead, 'visits', (lead.__dict__['visits'] + 1))
        setattr(lead, 'last_visit', datetime.now())

        current_app.db.session.add(lead)
        current_app.db.session.commit()

        return '', HTTPStatus.NO_CONTENT
    
    except BadRequest as e:
        if e.__dict__['description'] == 'fields':
            return {'error': "Apenas utilizar campo 'email'"}, HTTPStatus.BAD_REQUEST
    
    except TypeError:
        return {'error': "Campo email deve ser string"}, HTTPStatus.BAD_REQUEST
    
    except NotFound:
        return {"error": "Lead não encontrada"}, HTTPStatus.NOT_FOUND

def delete_lead():
    try:
        data = request.get_json()

        required_fields = ['email']
        LeadModel.check_fields(required_fields, data)

        lead = LeadModel.query.filter_by(email=data['email']).first()

        if lead == None:
            raise NotFound

        current_app.db.session.delete(lead)
        current_app.db.session.commit()
        
        return "", 204

    except BadRequest as e:
        if e.__dict__['description'] == 'fields':
            return {'error': "Apenas utilizar campo 'email'"}, HTTPStatus.BAD_REQUEST
    
    except TypeError:
        return {'error': "Campo email deve ser string"}, HTTPStatus.BAD_REQUEST
    
    except NotFound:
        return {"error": "Lead não encontrada"}, HTTPStatus.NOT_FOUND
