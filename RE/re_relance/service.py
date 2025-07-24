import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import RERelance
from .schema import RERelanceSchema


class RERelanceService:
    @staticmethod
    def index(current_user: User | None):
        result = []
        re_relance_schema = RERelanceSchema(many=True)
        page = request.args.get('page', '')
        re_relances = session.query(RERelance)\
                .filter(RERelance.deleted_at == None)\
                .order_by(RERelance.created_at.desc())

        if (page != ''):
            re_relances = paginate(re_relances, page=page)
            result = re_relances
            result['data'] = re_relance_schema.dump(re_relances['data'])
        else:
            result = re_relance_schema.dump(re_relances.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user: User | None):
        result = []
        re_relance_schema = RERelanceSchema(many=True)
        page = request.args.get('page', '')
        re_relances = session.query(RERelance)\
                .filter(RERelance.deleted_at == None,
                        RERelance.user_id == current_user.id)\
                .order_by(RERelance.created_at.desc())

        if (page != ''):
            re_relances = paginate(re_relances, page=page)
            result = re_relances
            result['data'] = re_relance_schema.dump(re_relances['data'])
        else:
            result = re_relance_schema.dump(re_relances.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user: User | None, id: int):
        re_relance:RERelance = session.query(RERelance)\
            .filter(RERelance.deleted_at == None,
                    RERelance.id == id).first()
        
        if re_relance is None: raise NotFound('re_relance not found')

        result = RERelanceSchema().dump(re_relance)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user: User | None, id: int):
        re_relance:RERelance = session.query(RERelance)\
            .filter(RERelance.user_id == current_user.id,
                    RERelance.deleted_at == None,
                    RERelance.id == id).first()
        
        if re_relance is None: raise NotFound('re_relance not found')

        result = RERelanceSchema().dump(re_relance)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user: User | None, validated_data):
        try:
            re_relance = RERelance(
                re_ordre_recette_id = validated_data.re_ordre_recette_id,
                user_id = validated_data.user_id,
                date = validated_data.date,
                heure = validated_data.heure,
                mode = validated_data.mode,
                statut = validated_data.statut,
                
            )

            session.add(re_relance)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RERelanceSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user: User | None, validated_data):
        try:
            re_relance = RERelance(
                re_ordre_recette_id = validated_data.re_ordre_recette_id,
                date = validated_data.date,
                heure = validated_data.heure,
                mode = validated_data.mode,
                statut = validated_data.statut,
                
                user_id = current_user.id,
            )

            session.add(re_relance)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RERelanceSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user: User | None, id: int, validated_data):
        try:
            re_relance: RERelance = session.query(RERelance).filter(
                RERelance.id == id, RERelance.deleted_at == None).first()

            if re_relance is None: raise NotFound('re_relance not found')

            re_relance.re_ordre_recette_id = validated_data.re_ordre_recette_id
            re_relance.user_id = validated_data.user_id
            re_relance.date = validated_data.date
            re_relance.heure = validated_data.heure
            re_relance.mode = validated_data.mode
            re_relance.statut = validated_data.statut
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RERelanceSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user: User | None, id: int, validated_data):
        try:
            re_relance: RERelance = session.query(RERelance).filter(
                RERelance.user_id == current_user.id,
                RERelance.id == id, 
                RERelance.deleted_at == None).first()

            if re_relance is None: raise NotFound('re_relance not found')

            re_relance.re_ordre_recette_id = validated_data.re_ordre_recette_id
            re_relance.user_id = validated_data.user_id
            re_relance.date = validated_data.date
            re_relance.heure = validated_data.heure
            re_relance.mode = validated_data.mode
            re_relance.statut = validated_data.statut
            
            re_relance.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RERelanceSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user: User | None, id: int):    
        try:
            re_relance:RERelance = session.query(RERelance)\
                .filter(RERelance.deleted_at == None,
                        RERelance.id == id).first()
            if re_relance is None: raise NotFound('re_relance not found')

            re_relance.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user: User | None, id: int):    
        try:
            re_relance:RERelance = session.query(RERelance)\
                .filter(User.deleted_at == current_user.id,
                        RERelance.deleted_at == None,
                        RERelance.id == id).first()

            if re_relance is None: raise NotFound('re_relance not found')

            re_relance.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK