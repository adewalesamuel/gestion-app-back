import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import GUTypeDemande
from .schema import GUTypeDemandeSchema


class GUTypeDemandeService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        gu_type_demande_schema = GUTypeDemandeSchema(many=True)
        page = request.args.get('page', '')
        gu_type_demandes = session.query(GUTypeDemande)\
                .filter(GUTypeDemande.deleted_at == None)\
                .order_by(GUTypeDemande.created_at.desc())

        if (page != ''):
            gu_type_demandes = paginate(gu_type_demandes, page=page)
            result = gu_type_demandes
            result['data'] = gu_type_demande_schema.dump(gu_type_demandes['data'])
        else:
            result = gu_type_demande_schema.dump(gu_type_demandes.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        gu_type_demande_schema = GUTypeDemandeSchema(many=True)
        page = request.args.get('page', '')
        gu_type_demandes = session.query(GUTypeDemande)\
                .filter(GUTypeDemande.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(GUTypeDemande.created_at.desc())

        if (page != ''):
            gu_type_demandes = paginate(gu_type_demandes, page=page)
            result = gu_type_demandes
            result['data'] = gu_type_demande_schema.dump(gu_type_demandes['data'])
        else:
            result = gu_type_demande_schema.dump(gu_type_demandes.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        gu_type_demande:GUTypeDemande = session.query(GUTypeDemande)\
            .filter(GUTypeDemande.deleted_at == None,
                    GUTypeDemande.id == id).first()
        
        if gu_type_demande is None: raise NotFound('gu_type_demande not found')

        result = GUTypeDemandeSchema().dump(gu_type_demande)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        gu_type_demande:GUTypeDemande = session.query(GUTypeDemande)\
            .filter(User.id == current_user.id,
                    GUTypeDemande.deleted_at == None,
                    GUTypeDemande.id == id).first()
        
        if gu_type_demande is None: raise NotFound('gu_type_demande not found')

        result = GUTypeDemandeSchema().dump(gu_type_demande)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            gu_type_demande = GUTypeDemande(
                code = validated_data.code,
                libelle = validated_data.libelle,
                delai_traitement_jours = validated_data.delai_traitement_jours,
                cout = validated_data.cout,
                validite_mois = validated_data.validite_mois,
                
            )

            session.add(gu_type_demande)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUTypeDemandeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            gu_type_demande = GUTypeDemande(
                code = validated_data.code,
                libelle = validated_data.libelle,
                delai_traitement_jours = validated_data.delai_traitement_jours,
                cout = validated_data.cout,
                validite_mois = validated_data.validite_mois,
                
                user_id = current_user.id,
            )

            session.add(gu_type_demande)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUTypeDemandeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            gu_type_demande: GUTypeDemande = session.query(GUTypeDemande).filter(
                GUTypeDemande.id == id, GUTypeDemande.deleted_at == None).first()

            if gu_type_demande is None: raise NotFound('gu_type_demande not found')

            gu_type_demande.code = validated_data.code
            gu_type_demande.libelle = validated_data.libelle
            gu_type_demande.delai_traitement_jours = validated_data.delai_traitement_jours
            gu_type_demande.cout = validated_data.cout
            gu_type_demande.validite_mois = validated_data.validite_mois
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUTypeDemandeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            gu_type_demande: GUTypeDemande = session.query(GUTypeDemande).filter(
                User.id == current_user.id,
                GUTypeDemande.id == id, 
                GUTypeDemande.deleted_at == None).first()

            if gu_type_demande is None: raise NotFound('gu_type_demande not found')

            gu_type_demande.code = validated_data.code
            gu_type_demande.libelle = validated_data.libelle
            gu_type_demande.delai_traitement_jours = validated_data.delai_traitement_jours
            gu_type_demande.cout = validated_data.cout
            gu_type_demande.validite_mois = validated_data.validite_mois
            
            gu_type_demande.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUTypeDemandeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            gu_type_demande:GUTypeDemande = session.query(GUTypeDemande)\
                .filter(GUTypeDemande.deleted_at == None,
                        GUTypeDemande.id == id).first()
            if gu_type_demande is None: raise NotFound('gu_type_demande not found')

            gu_type_demande.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            gu_type_demande:GUTypeDemande = session.query(GUTypeDemande)\
                .filter(User.deleted_at == current_user.id,
                        GUTypeDemande.deleted_at == None,
                        GUTypeDemande.id == id).first()

            if gu_type_demande is None: raise NotFound('gu_type_demande not found')

            gu_type_demande.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK