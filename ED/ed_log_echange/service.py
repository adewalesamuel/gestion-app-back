import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import EDLogEchange
from .schema import EDLogEchangeSchema


class EDLogEchangeService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        ed_log_echange_schema = EDLogEchangeSchema(many=True)
        page = request.args.get('page', '')
        ed_log_echanges = session.query(EDLogEchange)\
                .filter(EDLogEchange.deleted_at == None)\
                .order_by(EDLogEchange.created_at.desc())

        if (page != ''):
            ed_log_echanges = paginate(ed_log_echanges, page=page)
            result = ed_log_echanges
            result['data'] = ed_log_echange_schema.dump(ed_log_echanges['data'])
        else:
            result = ed_log_echange_schema.dump(ed_log_echanges.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        ed_log_echange_schema = EDLogEchangeSchema(many=True)
        page = request.args.get('page', '')
        ed_log_echanges = session.query(EDLogEchange)\
                .filter(EDLogEchange.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(EDLogEchange.created_at.desc())

        if (page != ''):
            ed_log_echanges = paginate(ed_log_echanges, page=page)
            result = ed_log_echanges
            result['data'] = ed_log_echange_schema.dump(ed_log_echanges['data'])
        else:
            result = ed_log_echange_schema.dump(ed_log_echanges.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        ed_log_echange:EDLogEchange = session.query(EDLogEchange)\
            .filter(EDLogEchange.deleted_at == None,
                    EDLogEchange.id == id).first()
        
        if ed_log_echange is None: raise NotFound('ed_log_echange not found')

        result = EDLogEchangeSchema().dump(ed_log_echange)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        ed_log_echange:EDLogEchange = session.query(EDLogEchange)\
            .filter(User.id == current_user.id,
                    EDLogEchange.deleted_at == None,
                    EDLogEchange.id == id).first()
        
        if ed_log_echange is None: raise NotFound('ed_log_echange not found')

        result = EDLogEchangeSchema().dump(ed_log_echange)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            ed_log_echange = EDLogEchange(
                ed_api_id = validated_data.ed_api_id,
                user_id = validated_data.user_id,
                date_heure = validated_data.date_heure,
                heure = validated_data.heure,
                type_requete = validated_data.type_requete,
                endpoint = validated_data.endpoint,
                statut_reponse = validated_data.statut_reponse,
                temps_reponse_ms = validated_data.temps_reponse_ms,
                
            )

            session.add(ed_log_echange)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDLogEchangeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            ed_log_echange = EDLogEchange(
                ed_api_id = validated_data.ed_api_id,
                date_heure = validated_data.date_heure,
                heure = validated_data.heure,
                type_requete = validated_data.type_requete,
                endpoint = validated_data.endpoint,
                statut_reponse = validated_data.statut_reponse,
                temps_reponse_ms = validated_data.temps_reponse_ms,
                
                user_id = current_user.id,
            )

            session.add(ed_log_echange)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDLogEchangeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            ed_log_echange: EDLogEchange = session.query(EDLogEchange).filter(
                EDLogEchange.id == id, EDLogEchange.deleted_at == None).first()

            if ed_log_echange is None: raise NotFound('ed_log_echange not found')

            ed_log_echange.ed_api_id = validated_data.ed_api_id
            ed_log_echange.user_id = validated_data.user_id
            ed_log_echange.date_heure = validated_data.date_heure
            ed_log_echange.heure = validated_data.heure
            ed_log_echange.type_requete = validated_data.type_requete
            ed_log_echange.endpoint = validated_data.endpoint
            ed_log_echange.statut_reponse = validated_data.statut_reponse
            ed_log_echange.temps_reponse_ms = validated_data.temps_reponse_ms
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDLogEchangeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            ed_log_echange: EDLogEchange = session.query(EDLogEchange).filter(
                User.id == current_user.id,
                EDLogEchange.id == id, 
                EDLogEchange.deleted_at == None).first()

            if ed_log_echange is None: raise NotFound('ed_log_echange not found')

            ed_log_echange.ed_api_id = validated_data.ed_api_id
            ed_log_echange.user_id = validated_data.user_id
            ed_log_echange.date_heure = validated_data.date_heure
            ed_log_echange.heure = validated_data.heure
            ed_log_echange.type_requete = validated_data.type_requete
            ed_log_echange.endpoint = validated_data.endpoint
            ed_log_echange.statut_reponse = validated_data.statut_reponse
            ed_log_echange.temps_reponse_ms = validated_data.temps_reponse_ms
            
            ed_log_echange.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDLogEchangeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            ed_log_echange:EDLogEchange = session.query(EDLogEchange)\
                .filter(EDLogEchange.deleted_at == None,
                        EDLogEchange.id == id).first()
            if ed_log_echange is None: raise NotFound('ed_log_echange not found')

            ed_log_echange.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            ed_log_echange:EDLogEchange = session.query(EDLogEchange)\
                .filter(User.deleted_at == current_user.id,
                        EDLogEchange.deleted_at == None,
                        EDLogEchange.id == id).first()

            if ed_log_echange is None: raise NotFound('ed_log_echange not found')

            ed_log_echange.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK