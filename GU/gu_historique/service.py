import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import GUHistorique
from .schema import GUHistoriqueSchema


class GUHistoriqueService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        gu_historique_schema = GUHistoriqueSchema(many=True)
        page = request.args.get('page', '')
        gu_historiques = session.query(GUHistorique)\
                .filter(GUHistorique.deleted_at == None)\
                .order_by(GUHistorique.created_at.desc())

        if (page != ''):
            gu_historiques = paginate(gu_historiques, page=page)
            result = gu_historiques
            result['data'] = gu_historique_schema.dump(gu_historiques['data'])
        else:
            result = gu_historique_schema.dump(gu_historiques.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        gu_historique_schema = GUHistoriqueSchema(many=True)
        page = request.args.get('page', '')
        gu_historiques = session.query(GUHistorique)\
                .filter(GUHistorique.deleted_at == None,
                        GUHistorique.user_id == current_user.id)\
                .order_by(GUHistorique.created_at.desc())

        if (page != ''):
            gu_historiques = paginate(gu_historiques, page=page)
            result = gu_historiques
            result['data'] = gu_historique_schema.dump(gu_historiques['data'])
        else:
            result = gu_historique_schema.dump(gu_historiques.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        gu_historique:GUHistorique = session.query(GUHistorique)\
            .filter(GUHistorique.deleted_at == None,
                    GUHistorique.id == id).first()
        
        if gu_historique is None: raise NotFound('gu_historique not found')

        result = GUHistoriqueSchema().dump(gu_historique)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        gu_historique:GUHistorique = session.query(GUHistorique)\
            .filter(GUHistorique.user_id == current_user.id,
                    GUHistorique.deleted_at == None,
                    GUHistorique.id == id).first()
        
        if gu_historique is None: raise NotFound('gu_historique not found')

        result = GUHistoriqueSchema().dump(gu_historique)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            gu_historique = GUHistorique(
                user_id = validated_data.user_id,
                gu_demande_id = validated_data.gu_demande_id,
                action = validated_data.action,
                details = validated_data.details,
                date = validated_data.date,
                heure = validated_data.heure,
                
            )

            session.add(gu_historique)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUHistoriqueSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            gu_historique = GUHistorique(
                gu_demande_id = validated_data.gu_demande_id,
                action = validated_data.action,
                details = validated_data.details,
                date = validated_data.date,
                heure = validated_data.heure,
                
                user_id = current_user.id,
            )

            session.add(gu_historique)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUHistoriqueSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            gu_historique: GUHistorique = session.query(GUHistorique).filter(
                GUHistorique.id == id, GUHistorique.deleted_at == None).first()

            if gu_historique is None: raise NotFound('gu_historique not found')

            gu_historique.user_id = validated_data.user_id
            gu_historique.gu_demande_id = validated_data.gu_demande_id
            gu_historique.action = validated_data.action
            gu_historique.details = validated_data.details
            gu_historique.date = validated_data.date
            gu_historique.heure = validated_data.heure
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUHistoriqueSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            gu_historique: GUHistorique = session.query(GUHistorique).filter(
                GUHistorique.user_id == current_user.id,
                GUHistorique.id == id, 
                GUHistorique.deleted_at == None).first()

            if gu_historique is None: raise NotFound('gu_historique not found')

            gu_historique.user_id = validated_data.user_id
            gu_historique.gu_demande_id = validated_data.gu_demande_id
            gu_historique.action = validated_data.action
            gu_historique.details = validated_data.details
            gu_historique.date = validated_data.date
            gu_historique.heure = validated_data.heure
            
            gu_historique.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUHistoriqueSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            gu_historique:GUHistorique = session.query(GUHistorique)\
                .filter(GUHistorique.deleted_at == None,
                        GUHistorique.id == id).first()
            if gu_historique is None: raise NotFound('gu_historique not found')

            gu_historique.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            gu_historique:GUHistorique = session.query(GUHistorique)\
                .filter(User.deleted_at == current_user.id,
                        GUHistorique.deleted_at == None,
                        GUHistorique.id == id).first()

            if gu_historique is None: raise NotFound('gu_historique not found')

            gu_historique.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK