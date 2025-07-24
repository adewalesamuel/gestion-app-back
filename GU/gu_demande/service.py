import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import GUDemande
from .schema import GUDemandeSchema


class GUDemandeService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        gu_demande_schema = GUDemandeSchema(many=True)
        page = request.args.get('page', '')
        gu_demandes = session.query(GUDemande)\
                .filter(GUDemande.deleted_at == None)\
                .order_by(GUDemande.created_at.desc())

        if (page != ''):
            gu_demandes = paginate(gu_demandes, page=page)
            result = gu_demandes
            result['data'] = gu_demande_schema.dump(gu_demandes['data'])
        else:
            result = gu_demande_schema.dump(gu_demandes.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        gu_demande:GUDemande = session.query(GUDemande)\
            .filter(GUDemande.deleted_at == None,
                    GUDemande.id == id).first()
        
        if gu_demande is None: raise NotFound('gu_demande not found')

        result = GUDemandeSchema().dump(gu_demande)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            gu_demande = GUDemande(
                gu_type_demande_id = validated_data.gu_type_demande_id,
                gu_statut_demande_id = validated_data.gu_statut_demande_id,
                rc_acteur_id = validated_data.rc_acteur_id,
                rc_engin_flottant_id = validated_data.rc_engin_flottant_id,
                reference = validated_data.reference,
                date_depot = validated_data.date_depot,
                heure = validated_data.heure,
                date_traitement = validated_data.date_traitement,
                date_expiration = validated_data.date_expiration,
                fichiers_joints = validated_data.fichiers_joints,
                
            )

            session.add(gu_demande)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUDemandeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            gu_demande: GUDemande = session.query(GUDemande).filter(
                GUDemande.id == id, GUDemande.deleted_at == None).first()

            if gu_demande is None: raise NotFound('gu_demande not found')

            gu_demande.gu_type_demande_id = validated_data.gu_type_demande_id
            gu_demande.gu_statut_demande_id = validated_data.gu_statut_demande_id
            gu_demande.rc_acteur_id = validated_data.rc_acteur_id
            gu_demande.rc_engin_flottant_id = validated_data.rc_engin_flottant_id
            gu_demande.reference = validated_data.reference
            gu_demande.date_depot = validated_data.date_depot
            gu_demande.heure = validated_data.heure
            gu_demande.date_traitement = validated_data.date_traitement
            gu_demande.date_expiration = validated_data.date_expiration
            gu_demande.fichiers_joints = validated_data.fichiers_joints
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUDemandeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            gu_demande:GUDemande = session.query(GUDemande)\
                .filter(GUDemande.deleted_at == None,
                        GUDemande.id == id).first()
            if gu_demande is None: raise NotFound('gu_demande not found')

            gu_demande.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK