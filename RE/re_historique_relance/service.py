import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import REHistoriqueRelance
from .schema import REHistoriqueRelanceSchema


class REHistoriqueRelanceService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        re_historique_relance_schema = REHistoriqueRelanceSchema(many=True)
        page = request.args.get('page', '')
        re_historique_relances = session.query(REHistoriqueRelance)\
                .filter(REHistoriqueRelance.deleted_at == None)\
                .order_by(REHistoriqueRelance.created_at.desc())

        if (page != ''):
            re_historique_relances = paginate(re_historique_relances, page=page)
            result = re_historique_relances
            result['data'] = re_historique_relance_schema.dump(re_historique_relances['data'])
        else:
            result = re_historique_relance_schema.dump(re_historique_relances.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        re_historique_relance_schema = REHistoriqueRelanceSchema(many=True)
        page = request.args.get('page', '')
        re_historique_relances = session.query(REHistoriqueRelance)\
                .filter(REHistoriqueRelance.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(REHistoriqueRelance.created_at.desc())

        if (page != ''):
            re_historique_relances = paginate(re_historique_relances, page=page)
            result = re_historique_relances
            result['data'] = re_historique_relance_schema.dump(re_historique_relances['data'])
        else:
            result = re_historique_relance_schema.dump(re_historique_relances.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        re_historique_relance:REHistoriqueRelance = session.query(REHistoriqueRelance)\
            .filter(REHistoriqueRelance.deleted_at == None,
                    REHistoriqueRelance.id == id).first()
        
        if re_historique_relance is None: raise NotFound('re_historique_relance not found')

        result = REHistoriqueRelanceSchema().dump(re_historique_relance)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        re_historique_relance:REHistoriqueRelance = session.query(REHistoriqueRelance)\
            .filter(User.id == current_user.id,
                    REHistoriqueRelance.deleted_at == None,
                    REHistoriqueRelance.id == id).first()
        
        if re_historique_relance is None: raise NotFound('re_historique_relance not found')

        result = REHistoriqueRelanceSchema().dump(re_historique_relance)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            re_historique_relance = REHistoriqueRelance(
                re_relance_id = validated_data.re_relance_id,
                user_id = validated_data.user_id,
                date = validated_data.date,
                heure = validated_data.heure,
                mode = validated_data.mode,
                contenu = validated_data.contenu,
                
            )

            session.add(re_historique_relance)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REHistoriqueRelanceSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            re_historique_relance = REHistoriqueRelance(
                re_relance_id = validated_data.re_relance_id,
                date = validated_data.date,
                heure = validated_data.heure,
                mode = validated_data.mode,
                contenu = validated_data.contenu,
                
                user_id = current_user.id,
            )

            session.add(re_historique_relance)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REHistoriqueRelanceSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            re_historique_relance: REHistoriqueRelance = session.query(REHistoriqueRelance).filter(
                REHistoriqueRelance.id == id, REHistoriqueRelance.deleted_at == None).first()

            if re_historique_relance is None: raise NotFound('re_historique_relance not found')

            re_historique_relance.re_relance_id = validated_data.re_relance_id
            re_historique_relance.user_id = validated_data.user_id
            re_historique_relance.date = validated_data.date
            re_historique_relance.heure = validated_data.heure
            re_historique_relance.mode = validated_data.mode
            re_historique_relance.contenu = validated_data.contenu
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REHistoriqueRelanceSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            re_historique_relance: REHistoriqueRelance = session.query(REHistoriqueRelance).filter(
                User.id == current_user.id,
                REHistoriqueRelance.id == id, 
                REHistoriqueRelance.deleted_at == None).first()

            if re_historique_relance is None: raise NotFound('re_historique_relance not found')

            re_historique_relance.re_relance_id = validated_data.re_relance_id
            re_historique_relance.user_id = validated_data.user_id
            re_historique_relance.date = validated_data.date
            re_historique_relance.heure = validated_data.heure
            re_historique_relance.mode = validated_data.mode
            re_historique_relance.contenu = validated_data.contenu
            
            re_historique_relance.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REHistoriqueRelanceSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            re_historique_relance:REHistoriqueRelance = session.query(REHistoriqueRelance)\
                .filter(REHistoriqueRelance.deleted_at == None,
                        REHistoriqueRelance.id == id).first()
            if re_historique_relance is None: raise NotFound('re_historique_relance not found')

            re_historique_relance.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            re_historique_relance:REHistoriqueRelance = session.query(REHistoriqueRelance)\
                .filter(User.deleted_at == current_user.id,
                        REHistoriqueRelance.deleted_at == None,
                        REHistoriqueRelance.id == id).first()

            if re_historique_relance is None: raise NotFound('re_historique_relance not found')

            re_historique_relance.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK