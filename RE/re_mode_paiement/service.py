import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import REModePaiement
from .schema import REModePaiementSchema


class REModePaiementService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        re_mode_paiement_schema = REModePaiementSchema(many=True)
        page = request.args.get('page', '')
        re_mode_paiements = session.query(REModePaiement)\
                .filter(REModePaiement.deleted_at == None)\
                .order_by(REModePaiement.created_at.desc())

        if (page != ''):
            re_mode_paiements = paginate(re_mode_paiements, page=page)
            result = re_mode_paiements
            result['data'] = re_mode_paiement_schema.dump(re_mode_paiements['data'])
        else:
            result = re_mode_paiement_schema.dump(re_mode_paiements.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        re_mode_paiement_schema = REModePaiementSchema(many=True)
        page = request.args.get('page', '')
        re_mode_paiements = session.query(REModePaiement)\
                .filter(REModePaiement.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(REModePaiement.created_at.desc())

        if (page != ''):
            re_mode_paiements = paginate(re_mode_paiements, page=page)
            result = re_mode_paiements
            result['data'] = re_mode_paiement_schema.dump(re_mode_paiements['data'])
        else:
            result = re_mode_paiement_schema.dump(re_mode_paiements.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        re_mode_paiement:REModePaiement = session.query(REModePaiement)\
            .filter(REModePaiement.deleted_at == None,
                    REModePaiement.id == id).first()
        
        if re_mode_paiement is None: raise NotFound('re_mode_paiement not found')

        result = REModePaiementSchema().dump(re_mode_paiement)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        re_mode_paiement:REModePaiement = session.query(REModePaiement)\
            .filter(User.id == current_user.id,
                    REModePaiement.deleted_at == None,
                    REModePaiement.id == id).first()
        
        if re_mode_paiement is None: raise NotFound('re_mode_paiement not found')

        result = REModePaiementSchema().dump(re_mode_paiement)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            re_mode_paiement = REModePaiement(
                code = validated_data.code,
                libelle = validated_data.libelle,
                frais_pourcentage = validated_data.frais_pourcentage,
                delai_jours = validated_data.delai_jours,
                actif = validated_data.actif,
                
            )

            session.add(re_mode_paiement)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REModePaiementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            re_mode_paiement = REModePaiement(
                code = validated_data.code,
                libelle = validated_data.libelle,
                frais_pourcentage = validated_data.frais_pourcentage,
                delai_jours = validated_data.delai_jours,
                actif = validated_data.actif,
                
                user_id = current_user.id,
            )

            session.add(re_mode_paiement)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REModePaiementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            re_mode_paiement: REModePaiement = session.query(REModePaiement).filter(
                REModePaiement.id == id, REModePaiement.deleted_at == None).first()

            if re_mode_paiement is None: raise NotFound('re_mode_paiement not found')

            re_mode_paiement.code = validated_data.code
            re_mode_paiement.libelle = validated_data.libelle
            re_mode_paiement.frais_pourcentage = validated_data.frais_pourcentage
            re_mode_paiement.delai_jours = validated_data.delai_jours
            re_mode_paiement.actif = validated_data.actif
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REModePaiementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            re_mode_paiement: REModePaiement = session.query(REModePaiement).filter(
                User.id == current_user.id,
                REModePaiement.id == id, 
                REModePaiement.deleted_at == None).first()

            if re_mode_paiement is None: raise NotFound('re_mode_paiement not found')

            re_mode_paiement.code = validated_data.code
            re_mode_paiement.libelle = validated_data.libelle
            re_mode_paiement.frais_pourcentage = validated_data.frais_pourcentage
            re_mode_paiement.delai_jours = validated_data.delai_jours
            re_mode_paiement.actif = validated_data.actif
            
            re_mode_paiement.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REModePaiementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            re_mode_paiement:REModePaiement = session.query(REModePaiement)\
                .filter(REModePaiement.deleted_at == None,
                        REModePaiement.id == id).first()
            if re_mode_paiement is None: raise NotFound('re_mode_paiement not found')

            re_mode_paiement.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            re_mode_paiement:REModePaiement = session.query(REModePaiement)\
                .filter(User.deleted_at == current_user.id,
                        REModePaiement.deleted_at == None,
                        REModePaiement.id == id).first()

            if re_mode_paiement is None: raise NotFound('re_mode_paiement not found')

            re_mode_paiement.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK