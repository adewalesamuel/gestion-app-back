import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import EDAbonnement
from .schema import EDAbonnementSchema


class EDAbonnementService:
    @staticmethod
    def index(current_user: User | None):
        result = []
        ed_abonnement_schema = EDAbonnementSchema(many=True)
        page = request.args.get('page', '')
        ed_abonnements = session.query(EDAbonnement)\
                .filter(EDAbonnement.deleted_at == None)\
                .order_by(EDAbonnement.created_at.desc())

        if (page != ''):
            ed_abonnements = paginate(ed_abonnements, page=page)
            result = ed_abonnements
            result['data'] = ed_abonnement_schema.dump(ed_abonnements['data'])
        else:
            result = ed_abonnement_schema.dump(ed_abonnements.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user: User | None, id: int):
        ed_abonnement:EDAbonnement = session.query(EDAbonnement)\
            .filter(EDAbonnement.deleted_at == None,
                    EDAbonnement.id == id).first()
        
        if ed_abonnement is None: raise NotFound('ed_abonnement not found')

        result = EDAbonnementSchema().dump(ed_abonnement)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user: User | None, validated_data):
        try:
            ed_abonnement = EDAbonnement(
                ed_api_id = validated_data.ed_api_id,
                rc_acteur_id = validated_data.rc_acteur_id,
                nom_client = validated_data.nom_client,
                token = validated_data.token,
                date_expiration = validated_data.date_expiration,
                limite_requetes_jour = validated_data.limite_requetes_jour,
                
            )

            session.add(ed_abonnement)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDAbonnementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user: User | None, id: int, validated_data):
        try:
            ed_abonnement: EDAbonnement = session.query(EDAbonnement).filter(
                EDAbonnement.id == id, EDAbonnement.deleted_at == None).first()

            if ed_abonnement is None: raise NotFound('ed_abonnement not found')

            ed_abonnement.ed_api_id = validated_data.ed_api_id
            ed_abonnement.rc_acteur_id = validated_data.rc_acteur_id
            ed_abonnement.nom_client = validated_data.nom_client
            ed_abonnement.token = validated_data.token
            ed_abonnement.date_expiration = validated_data.date_expiration
            ed_abonnement.limite_requetes_jour = validated_data.limite_requetes_jour
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDAbonnementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def delete(current_user: User | None, id: int):    
        try:
            ed_abonnement:EDAbonnement = session.query(EDAbonnement)\
                .filter(EDAbonnement.deleted_at == None,
                        EDAbonnement.id == id).first()
            if ed_abonnement is None: raise NotFound('ed_abonnement not found')

            ed_abonnement.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK