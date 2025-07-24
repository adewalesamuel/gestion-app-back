import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import EDSchemaDonnees
from .schema import EDSchemaDonneesSchema


class EDSchemaDonneesService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        ed_schema_donnees_schema = EDSchemaDonneesSchema(many=True)
        page = request.args.get('page', '')
        ed_schema_donneess = session.query(EDSchemaDonnees)\
                .filter(EDSchemaDonnees.deleted_at == None)\
                .order_by(EDSchemaDonnees.created_at.desc())

        if (page != ''):
            ed_schema_donneess = paginate(ed_schema_donneess, page=page)
            result = ed_schema_donneess
            result['data'] = ed_schema_donnees_schema.dump(ed_schema_donneess['data'])
        else:
            result = ed_schema_donnees_schema.dump(ed_schema_donneess.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        ed_schema_donnees_schema = EDSchemaDonneesSchema(many=True)
        page = request.args.get('page', '')
        ed_schema_donneess = session.query(EDSchemaDonnees)\
                .filter(EDSchemaDonnees.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(EDSchemaDonnees.created_at.desc())

        if (page != ''):
            ed_schema_donneess = paginate(ed_schema_donneess, page=page)
            result = ed_schema_donneess
            result['data'] = ed_schema_donnees_schema.dump(ed_schema_donneess['data'])
        else:
            result = ed_schema_donnees_schema.dump(ed_schema_donneess.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        ed_schema_donnees:EDSchemaDonnees = session.query(EDSchemaDonnees)\
            .filter(EDSchemaDonnees.deleted_at == None,
                    EDSchemaDonnees.id == id).first()
        
        if ed_schema_donnees is None: raise NotFound('ed_schema_donnees not found')

        result = EDSchemaDonneesSchema().dump(ed_schema_donnees)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        ed_schema_donnees:EDSchemaDonnees = session.query(EDSchemaDonnees)\
            .filter(User.id == current_user.id,
                    EDSchemaDonnees.deleted_at == None,
                    EDSchemaDonnees.id == id).first()
        
        if ed_schema_donnees is None: raise NotFound('ed_schema_donnees not found')

        result = EDSchemaDonneesSchema().dump(ed_schema_donnees)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            ed_schema_donnees = EDSchemaDonnees(
                nom = validated_data.nom,
                version = validated_data.version,
                schema_json = validated_data.schema_json,
                statut = validated_data.statut,
                
            )

            session.add(ed_schema_donnees)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDSchemaDonneesSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            ed_schema_donnees = EDSchemaDonnees(
                nom = validated_data.nom,
                version = validated_data.version,
                schema_json = validated_data.schema_json,
                statut = validated_data.statut,
                
                user_id = current_user.id,
            )

            session.add(ed_schema_donnees)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDSchemaDonneesSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            ed_schema_donnees: EDSchemaDonnees = session.query(EDSchemaDonnees).filter(
                EDSchemaDonnees.id == id, EDSchemaDonnees.deleted_at == None).first()

            if ed_schema_donnees is None: raise NotFound('ed_schema_donnees not found')

            ed_schema_donnees.nom = validated_data.nom
            ed_schema_donnees.version = validated_data.version
            ed_schema_donnees.schema_json = validated_data.schema_json
            ed_schema_donnees.statut = validated_data.statut
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDSchemaDonneesSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            ed_schema_donnees: EDSchemaDonnees = session.query(EDSchemaDonnees).filter(
                User.id == current_user.id,
                EDSchemaDonnees.id == id, 
                EDSchemaDonnees.deleted_at == None).first()

            if ed_schema_donnees is None: raise NotFound('ed_schema_donnees not found')

            ed_schema_donnees.nom = validated_data.nom
            ed_schema_donnees.version = validated_data.version
            ed_schema_donnees.schema_json = validated_data.schema_json
            ed_schema_donnees.statut = validated_data.statut
            
            ed_schema_donnees.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDSchemaDonneesSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            ed_schema_donnees:EDSchemaDonnees = session.query(EDSchemaDonnees)\
                .filter(EDSchemaDonnees.deleted_at == None,
                        EDSchemaDonnees.id == id).first()
            if ed_schema_donnees is None: raise NotFound('ed_schema_donnees not found')

            ed_schema_donnees.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            ed_schema_donnees:EDSchemaDonnees = session.query(EDSchemaDonnees)\
                .filter(User.deleted_at == current_user.id,
                        EDSchemaDonnees.deleted_at == None,
                        EDSchemaDonnees.id == id).first()

            if ed_schema_donnees is None: raise NotFound('ed_schema_donnees not found')

            ed_schema_donnees.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK