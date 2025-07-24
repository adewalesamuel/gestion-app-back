import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import EDFormatDonnees
from .schema import EDFormatDonneesSchema


class EDFormatDonneesService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        ed_format_donnees_schema = EDFormatDonneesSchema(many=True)
        page = request.args.get('page', '')
        ed_format_donneess = session.query(EDFormatDonnees)\
                .filter(EDFormatDonnees.deleted_at == None)\
                .order_by(EDFormatDonnees.created_at.desc())

        if (page != ''):
            ed_format_donneess = paginate(ed_format_donneess, page=page)
            result = ed_format_donneess
            result['data'] = ed_format_donnees_schema.dump(ed_format_donneess['data'])
        else:
            result = ed_format_donnees_schema.dump(ed_format_donneess.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        ed_format_donnees_schema = EDFormatDonneesSchema(many=True)
        page = request.args.get('page', '')
        ed_format_donneess = session.query(EDFormatDonnees)\
                .filter(EDFormatDonnees.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(EDFormatDonnees.created_at.desc())

        if (page != ''):
            ed_format_donneess = paginate(ed_format_donneess, page=page)
            result = ed_format_donneess
            result['data'] = ed_format_donnees_schema.dump(ed_format_donneess['data'])
        else:
            result = ed_format_donnees_schema.dump(ed_format_donneess.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        ed_format_donnees:EDFormatDonnees = session.query(EDFormatDonnees)\
            .filter(EDFormatDonnees.deleted_at == None,
                    EDFormatDonnees.id == id).first()
        
        if ed_format_donnees is None: raise NotFound('ed_format_donnees not found')

        result = EDFormatDonneesSchema().dump(ed_format_donnees)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        ed_format_donnees:EDFormatDonnees = session.query(EDFormatDonnees)\
            .filter(User.id == current_user.id,
                    EDFormatDonnees.deleted_at == None,
                    EDFormatDonnees.id == id).first()
        
        if ed_format_donnees is None: raise NotFound('ed_format_donnees not found')

        result = EDFormatDonneesSchema().dump(ed_format_donnees)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            ed_format_donnees = EDFormatDonnees(
                nom = validated_data.nom,
                mime_type = validated_data.mime_type,
                schema_xsd_url = validated_data.schema_xsd_url,
                exemple_url = validated_data.exemple_url,
                
            )

            session.add(ed_format_donnees)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDFormatDonneesSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            ed_format_donnees = EDFormatDonnees(
                nom = validated_data.nom,
                mime_type = validated_data.mime_type,
                schema_xsd_url = validated_data.schema_xsd_url,
                exemple_url = validated_data.exemple_url,
                
                user_id = current_user.id,
            )

            session.add(ed_format_donnees)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDFormatDonneesSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            ed_format_donnees: EDFormatDonnees = session.query(EDFormatDonnees).filter(
                EDFormatDonnees.id == id, EDFormatDonnees.deleted_at == None).first()

            if ed_format_donnees is None: raise NotFound('ed_format_donnees not found')

            ed_format_donnees.nom = validated_data.nom
            ed_format_donnees.mime_type = validated_data.mime_type
            ed_format_donnees.schema_xsd_url = validated_data.schema_xsd_url
            ed_format_donnees.exemple_url = validated_data.exemple_url
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDFormatDonneesSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            ed_format_donnees: EDFormatDonnees = session.query(EDFormatDonnees).filter(
                User.id == current_user.id,
                EDFormatDonnees.id == id, 
                EDFormatDonnees.deleted_at == None).first()

            if ed_format_donnees is None: raise NotFound('ed_format_donnees not found')

            ed_format_donnees.nom = validated_data.nom
            ed_format_donnees.mime_type = validated_data.mime_type
            ed_format_donnees.schema_xsd_url = validated_data.schema_xsd_url
            ed_format_donnees.exemple_url = validated_data.exemple_url
            
            ed_format_donnees.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDFormatDonneesSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            ed_format_donnees:EDFormatDonnees = session.query(EDFormatDonnees)\
                .filter(EDFormatDonnees.deleted_at == None,
                        EDFormatDonnees.id == id).first()
            if ed_format_donnees is None: raise NotFound('ed_format_donnees not found')

            ed_format_donnees.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            ed_format_donnees:EDFormatDonnees = session.query(EDFormatDonnees)\
                .filter(User.deleted_at == current_user.id,
                        EDFormatDonnees.deleted_at == None,
                        EDFormatDonnees.id == id).first()

            if ed_format_donnees is None: raise NotFound('ed_format_donnees not found')

            ed_format_donnees.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK