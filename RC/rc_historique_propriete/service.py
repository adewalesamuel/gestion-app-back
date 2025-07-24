import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import RCHistoriquePropriete
from .schema import RCHistoriqueProprieteSchema


class RCHistoriqueProprieteService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        rc_historique_propriete_schema = RCHistoriqueProprieteSchema(many=True)
        page = request.args.get('page', '')
        rc_historique_proprietes = session.query(RCHistoriquePropriete)\
                .filter(RCHistoriquePropriete.deleted_at == None)\
                .order_by(RCHistoriquePropriete.created_at.desc())

        if (page != ''):
            rc_historique_proprietes = paginate(rc_historique_proprietes, page=page)
            result = rc_historique_proprietes
            result['data'] = rc_historique_propriete_schema.dump(rc_historique_proprietes['data'])
        else:
            result = rc_historique_propriete_schema.dump(rc_historique_proprietes.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        rc_historique_propriete_schema = RCHistoriqueProprieteSchema(many=True)
        page = request.args.get('page', '')
        rc_historique_proprietes = session.query(RCHistoriquePropriete)\
                .filter(RCHistoriquePropriete.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(RCHistoriquePropriete.created_at.desc())

        if (page != ''):
            rc_historique_proprietes = paginate(rc_historique_proprietes, page=page)
            result = rc_historique_proprietes
            result['data'] = rc_historique_propriete_schema.dump(rc_historique_proprietes['data'])
        else:
            result = rc_historique_propriete_schema.dump(rc_historique_proprietes.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        rc_historique_propriete:RCHistoriquePropriete = session.query(RCHistoriquePropriete)\
            .filter(RCHistoriquePropriete.deleted_at == None,
                    RCHistoriquePropriete.id == id).first()
        
        if rc_historique_propriete is None: raise NotFound('rc_historique_propriete not found')

        result = RCHistoriqueProprieteSchema().dump(rc_historique_propriete)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        rc_historique_propriete:RCHistoriquePropriete = session.query(RCHistoriquePropriete)\
            .filter(User.id == current_user.id,
                    RCHistoriquePropriete.deleted_at == None,
                    RCHistoriquePropriete.id == id).first()
        
        if rc_historique_propriete is None: raise NotFound('rc_historique_propriete not found')

        result = RCHistoriqueProprieteSchema().dump(rc_historique_propriete)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            rc_historique_propriete = RCHistoriquePropriete(
                rc_acteur_id = validated_data.rc_acteur_id,
                rc_engin_flottant_id = validated_data.rc_engin_flottant_id,
                date_debut = validated_data.date_debut,
                date_fin = validated_data.date_fin,
                type_transaction = validated_data.type_transaction,
                
            )

            session.add(rc_historique_propriete)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCHistoriqueProprieteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            rc_historique_propriete = RCHistoriquePropriete(
                rc_acteur_id = validated_data.rc_acteur_id,
                rc_engin_flottant_id = validated_data.rc_engin_flottant_id,
                date_debut = validated_data.date_debut,
                date_fin = validated_data.date_fin,
                type_transaction = validated_data.type_transaction,
                
                user_id = current_user.id,
            )

            session.add(rc_historique_propriete)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCHistoriqueProprieteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            rc_historique_propriete: RCHistoriquePropriete = session.query(RCHistoriquePropriete).filter(
                RCHistoriquePropriete.id == id, RCHistoriquePropriete.deleted_at == None).first()

            if rc_historique_propriete is None: raise NotFound('rc_historique_propriete not found')

            rc_historique_propriete.rc_acteur_id = validated_data.rc_acteur_id
            rc_historique_propriete.rc_engin_flottant_id = validated_data.rc_engin_flottant_id
            rc_historique_propriete.date_debut = validated_data.date_debut
            rc_historique_propriete.date_fin = validated_data.date_fin
            rc_historique_propriete.type_transaction = validated_data.type_transaction
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCHistoriqueProprieteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            rc_historique_propriete: RCHistoriquePropriete = session.query(RCHistoriquePropriete).filter(
                User.id == current_user.id,
                RCHistoriquePropriete.id == id, 
                RCHistoriquePropriete.deleted_at == None).first()

            if rc_historique_propriete is None: raise NotFound('rc_historique_propriete not found')

            rc_historique_propriete.rc_acteur_id = validated_data.rc_acteur_id
            rc_historique_propriete.rc_engin_flottant_id = validated_data.rc_engin_flottant_id
            rc_historique_propriete.date_debut = validated_data.date_debut
            rc_historique_propriete.date_fin = validated_data.date_fin
            rc_historique_propriete.type_transaction = validated_data.type_transaction
            
            rc_historique_propriete.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCHistoriqueProprieteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            rc_historique_propriete:RCHistoriquePropriete = session.query(RCHistoriquePropriete)\
                .filter(RCHistoriquePropriete.deleted_at == None,
                        RCHistoriquePropriete.id == id).first()
            if rc_historique_propriete is None: raise NotFound('rc_historique_propriete not found')

            rc_historique_propriete.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            rc_historique_propriete:RCHistoriquePropriete = session.query(RCHistoriquePropriete)\
                .filter(User.deleted_at == current_user.id,
                        RCHistoriquePropriete.deleted_at == None,
                        RCHistoriquePropriete.id == id).first()

            if rc_historique_propriete is None: raise NotFound('rc_historique_propriete not found')

            rc_historique_propriete.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK