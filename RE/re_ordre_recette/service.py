import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import REOrdreRecette
from .schema import REOrdreRecetteSchema


class REOrdreRecetteService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        re_ordre_recette_schema = REOrdreRecetteSchema(many=True)
        page = request.args.get('page', '')
        re_ordre_recettes = session.query(REOrdreRecette)\
                .filter(REOrdreRecette.deleted_at == None)\
                .order_by(REOrdreRecette.created_at.desc())

        if (page != ''):
            re_ordre_recettes = paginate(re_ordre_recettes, page=page)
            result = re_ordre_recettes
            result['data'] = re_ordre_recette_schema.dump(re_ordre_recettes['data'])
        else:
            result = re_ordre_recette_schema.dump(re_ordre_recettes.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        re_ordre_recette_schema = REOrdreRecetteSchema(many=True)
        page = request.args.get('page', '')
        re_ordre_recettes = session.query(REOrdreRecette)\
                .filter(REOrdreRecette.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(REOrdreRecette.created_at.desc())

        if (page != ''):
            re_ordre_recettes = paginate(re_ordre_recettes, page=page)
            result = re_ordre_recettes
            result['data'] = re_ordre_recette_schema.dump(re_ordre_recettes['data'])
        else:
            result = re_ordre_recette_schema.dump(re_ordre_recettes.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        re_ordre_recette:REOrdreRecette = session.query(REOrdreRecette)\
            .filter(REOrdreRecette.deleted_at == None,
                    REOrdreRecette.id == id).first()
        
        if re_ordre_recette is None: raise NotFound('re_ordre_recette not found')

        result = REOrdreRecetteSchema().dump(re_ordre_recette)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        re_ordre_recette:REOrdreRecette = session.query(REOrdreRecette)\
            .filter(User.id == current_user.id,
                    REOrdreRecette.deleted_at == None,
                    REOrdreRecette.id == id).first()
        
        if re_ordre_recette is None: raise NotFound('re_ordre_recette not found')

        result = REOrdreRecetteSchema().dump(re_ordre_recette)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            re_ordre_recette = REOrdreRecette(
                rc_acteur_id = validated_data.rc_acteur_id,
                reference = validated_data.reference,
                montant = validated_data.montant,
                devise = validated_data.devise,
                date_emission = validated_data.date_emission,
                date_echeance = validated_data.date_echeance,
                statut = validated_data.statut,
                service_concerne = validated_data.service_concerne,
                
            )

            session.add(re_ordre_recette)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REOrdreRecetteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            re_ordre_recette = REOrdreRecette(
                rc_acteur_id = validated_data.rc_acteur_id,
                reference = validated_data.reference,
                montant = validated_data.montant,
                devise = validated_data.devise,
                date_emission = validated_data.date_emission,
                date_echeance = validated_data.date_echeance,
                statut = validated_data.statut,
                service_concerne = validated_data.service_concerne,
                
                user_id = current_user.id,
            )

            session.add(re_ordre_recette)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REOrdreRecetteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            re_ordre_recette: REOrdreRecette = session.query(REOrdreRecette).filter(
                REOrdreRecette.id == id, REOrdreRecette.deleted_at == None).first()

            if re_ordre_recette is None: raise NotFound('re_ordre_recette not found')

            re_ordre_recette.rc_acteur_id = validated_data.rc_acteur_id
            re_ordre_recette.reference = validated_data.reference
            re_ordre_recette.montant = validated_data.montant
            re_ordre_recette.devise = validated_data.devise
            re_ordre_recette.date_emission = validated_data.date_emission
            re_ordre_recette.date_echeance = validated_data.date_echeance
            re_ordre_recette.statut = validated_data.statut
            re_ordre_recette.service_concerne = validated_data.service_concerne
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REOrdreRecetteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            re_ordre_recette: REOrdreRecette = session.query(REOrdreRecette).filter(
                User.id == current_user.id,
                REOrdreRecette.id == id, 
                REOrdreRecette.deleted_at == None).first()

            if re_ordre_recette is None: raise NotFound('re_ordre_recette not found')

            re_ordre_recette.rc_acteur_id = validated_data.rc_acteur_id
            re_ordre_recette.reference = validated_data.reference
            re_ordre_recette.montant = validated_data.montant
            re_ordre_recette.devise = validated_data.devise
            re_ordre_recette.date_emission = validated_data.date_emission
            re_ordre_recette.date_echeance = validated_data.date_echeance
            re_ordre_recette.statut = validated_data.statut
            re_ordre_recette.service_concerne = validated_data.service_concerne
            
            re_ordre_recette.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REOrdreRecetteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            re_ordre_recette:REOrdreRecette = session.query(REOrdreRecette)\
                .filter(REOrdreRecette.deleted_at == None,
                        REOrdreRecette.id == id).first()
            if re_ordre_recette is None: raise NotFound('re_ordre_recette not found')

            re_ordre_recette.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            re_ordre_recette:REOrdreRecette = session.query(REOrdreRecette)\
                .filter(User.deleted_at == current_user.id,
                        REOrdreRecette.deleted_at == None,
                        REOrdreRecette.id == id).first()

            if re_ordre_recette is None: raise NotFound('re_ordre_recette not found')

            re_ordre_recette.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK