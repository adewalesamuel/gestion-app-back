import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import REPaiement
from .schema import REPaiementSchema


class REPaiementService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        re_paiement_schema = REPaiementSchema(many=True)
        page = request.args.get('page', '')
        re_paiements = session.query(REPaiement)\
                .filter(REPaiement.deleted_at == None)\
                .order_by(REPaiement.created_at.desc())

        if (page != ''):
            re_paiements = paginate(re_paiements, page=page)
            result = re_paiements
            result['data'] = re_paiement_schema.dump(re_paiements['data'])
        else:
            result = re_paiement_schema.dump(re_paiements.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        re_paiement_schema = REPaiementSchema(many=True)
        page = request.args.get('page', '')
        re_paiements = session.query(REPaiement)\
                .filter(REPaiement.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(REPaiement.created_at.desc())

        if (page != ''):
            re_paiements = paginate(re_paiements, page=page)
            result = re_paiements
            result['data'] = re_paiement_schema.dump(re_paiements['data'])
        else:
            result = re_paiement_schema.dump(re_paiements.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        re_paiement:REPaiement = session.query(REPaiement)\
            .filter(REPaiement.deleted_at == None,
                    REPaiement.id == id).first()
        
        if re_paiement is None: raise NotFound('re_paiement not found')

        result = REPaiementSchema().dump(re_paiement)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        re_paiement:REPaiement = session.query(REPaiement)\
            .filter(User.id == current_user.id,
                    REPaiement.deleted_at == None,
                    REPaiement.id == id).first()
        
        if re_paiement is None: raise NotFound('re_paiement not found')

        result = REPaiementSchema().dump(re_paiement)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            re_paiement = REPaiement(
                re_ordre_recette_id = validated_data.re_ordre_recette_id,
                user_id = validated_data.user_id,
                re_mode_paiement_id = validated_data.re_mode_paiement_id,
                montant = validated_data.montant,
                devise = validated_data.devise,
                date_paiement = validated_data.date_paiement,
                heure = validated_data.heure,
                reference_transaction = validated_data.reference_transaction,
                
            )

            session.add(re_paiement)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REPaiementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            re_paiement = REPaiement(
                re_ordre_recette_id = validated_data.re_ordre_recette_id,
                re_mode_paiement_id = validated_data.re_mode_paiement_id,
                montant = validated_data.montant,
                devise = validated_data.devise,
                date_paiement = validated_data.date_paiement,
                heure = validated_data.heure,
                reference_transaction = validated_data.reference_transaction,
                
                user_id = current_user.id,
            )

            session.add(re_paiement)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REPaiementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            re_paiement: REPaiement = session.query(REPaiement).filter(
                REPaiement.id == id, REPaiement.deleted_at == None).first()

            if re_paiement is None: raise NotFound('re_paiement not found')

            re_paiement.re_ordre_recette_id = validated_data.re_ordre_recette_id
            re_paiement.user_id = validated_data.user_id
            re_paiement.re_mode_paiement_id = validated_data.re_mode_paiement_id
            re_paiement.montant = validated_data.montant
            re_paiement.devise = validated_data.devise
            re_paiement.date_paiement = validated_data.date_paiement
            re_paiement.heure = validated_data.heure
            re_paiement.reference_transaction = validated_data.reference_transaction
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REPaiementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            re_paiement: REPaiement = session.query(REPaiement).filter(
                User.id == current_user.id,
                REPaiement.id == id, 
                REPaiement.deleted_at == None).first()

            if re_paiement is None: raise NotFound('re_paiement not found')

            re_paiement.re_ordre_recette_id = validated_data.re_ordre_recette_id
            re_paiement.user_id = validated_data.user_id
            re_paiement.re_mode_paiement_id = validated_data.re_mode_paiement_id
            re_paiement.montant = validated_data.montant
            re_paiement.devise = validated_data.devise
            re_paiement.date_paiement = validated_data.date_paiement
            re_paiement.heure = validated_data.heure
            re_paiement.reference_transaction = validated_data.reference_transaction
            
            re_paiement.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': REPaiementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            re_paiement:REPaiement = session.query(REPaiement)\
                .filter(REPaiement.deleted_at == None,
                        REPaiement.id == id).first()
            if re_paiement is None: raise NotFound('re_paiement not found')

            re_paiement.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            re_paiement:REPaiement = session.query(REPaiement)\
                .filter(User.deleted_at == current_user.id,
                        REPaiement.deleted_at == None,
                        REPaiement.id == id).first()

            if re_paiement is None: raise NotFound('re_paiement not found')

            re_paiement.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK