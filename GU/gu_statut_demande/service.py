import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import GUStatutDemande
from .schema import GUStatutDemandeSchema


class GUStatutDemandeService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        gu_statut_demande_schema = GUStatutDemandeSchema(many=True)
        page = request.args.get('page', '')
        gu_statut_demandes = session.query(GUStatutDemande)\
                .filter(GUStatutDemande.deleted_at == None)\
                .order_by(GUStatutDemande.created_at.desc())

        if (page != ''):
            gu_statut_demandes = paginate(gu_statut_demandes, page=page)
            result = gu_statut_demandes
            result['data'] = gu_statut_demande_schema.dump(gu_statut_demandes['data'])
        else:
            result = gu_statut_demande_schema.dump(gu_statut_demandes.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        gu_statut_demande_schema = GUStatutDemandeSchema(many=True)
        page = request.args.get('page', '')
        gu_statut_demandes = session.query(GUStatutDemande)\
                .filter(GUStatutDemande.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(GUStatutDemande.created_at.desc())

        if (page != ''):
            gu_statut_demandes = paginate(gu_statut_demandes, page=page)
            result = gu_statut_demandes
            result['data'] = gu_statut_demande_schema.dump(gu_statut_demandes['data'])
        else:
            result = gu_statut_demande_schema.dump(gu_statut_demandes.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        gu_statut_demande:GUStatutDemande = session.query(GUStatutDemande)\
            .filter(GUStatutDemande.deleted_at == None,
                    GUStatutDemande.id == id).first()
        
        if gu_statut_demande is None: raise NotFound('gu_statut_demande not found')

        result = GUStatutDemandeSchema().dump(gu_statut_demande)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        gu_statut_demande:GUStatutDemande = session.query(GUStatutDemande)\
            .filter(User.id == current_user.id,
                    GUStatutDemande.deleted_at == None,
                    GUStatutDemande.id == id).first()
        
        if gu_statut_demande is None: raise NotFound('gu_statut_demande not found')

        result = GUStatutDemandeSchema().dump(gu_statut_demande)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            gu_statut_demande = GUStatutDemande(
                code = validated_data.code,
                libelle = validated_data.libelle,
                couleur_hex = validated_data.couleur_hex,
                ordre = validated_data.ordre,
                notifiable = validated_data.notifiable,
                
            )

            session.add(gu_statut_demande)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUStatutDemandeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            gu_statut_demande = GUStatutDemande(
                code = validated_data.code,
                libelle = validated_data.libelle,
                couleur_hex = validated_data.couleur_hex,
                ordre = validated_data.ordre,
                notifiable = validated_data.notifiable,
                
                user_id = current_user.id,
            )

            session.add(gu_statut_demande)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUStatutDemandeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            gu_statut_demande: GUStatutDemande = session.query(GUStatutDemande).filter(
                GUStatutDemande.id == id, GUStatutDemande.deleted_at == None).first()

            if gu_statut_demande is None: raise NotFound('gu_statut_demande not found')

            gu_statut_demande.code = validated_data.code
            gu_statut_demande.libelle = validated_data.libelle
            gu_statut_demande.couleur_hex = validated_data.couleur_hex
            gu_statut_demande.ordre = validated_data.ordre
            gu_statut_demande.notifiable = validated_data.notifiable
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUStatutDemandeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            gu_statut_demande: GUStatutDemande = session.query(GUStatutDemande).filter(
                User.id == current_user.id,
                GUStatutDemande.id == id, 
                GUStatutDemande.deleted_at == None).first()

            if gu_statut_demande is None: raise NotFound('gu_statut_demande not found')

            gu_statut_demande.code = validated_data.code
            gu_statut_demande.libelle = validated_data.libelle
            gu_statut_demande.couleur_hex = validated_data.couleur_hex
            gu_statut_demande.ordre = validated_data.ordre
            gu_statut_demande.notifiable = validated_data.notifiable
            
            gu_statut_demande.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUStatutDemandeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            gu_statut_demande:GUStatutDemande = session.query(GUStatutDemande)\
                .filter(GUStatutDemande.deleted_at == None,
                        GUStatutDemande.id == id).first()
            if gu_statut_demande is None: raise NotFound('gu_statut_demande not found')

            gu_statut_demande.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            gu_statut_demande:GUStatutDemande = session.query(GUStatutDemande)\
                .filter(User.deleted_at == current_user.id,
                        GUStatutDemande.deleted_at == None,
                        GUStatutDemande.id == id).first()

            if gu_statut_demande is None: raise NotFound('gu_statut_demande not found')

            gu_statut_demande.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK