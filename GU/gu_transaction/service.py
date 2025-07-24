import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import GUTransaction
from .schema import GUTransactionSchema


class GUTransactionService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        gu_transaction_schema = GUTransactionSchema(many=True)
        page = request.args.get('page', '')
        gu_transactions = session.query(GUTransaction)\
                .filter(GUTransaction.deleted_at == None)\
                .order_by(GUTransaction.created_at.desc())

        if (page != ''):
            gu_transactions = paginate(gu_transactions, page=page)
            result = gu_transactions
            result['data'] = gu_transaction_schema.dump(gu_transactions['data'])
        else:
            result = gu_transaction_schema.dump(gu_transactions.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        gu_transaction_schema = GUTransactionSchema(many=True)
        page = request.args.get('page', '')
        gu_transactions = session.query(GUTransaction)\
                .filter(GUTransaction.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(GUTransaction.created_at.desc())

        if (page != ''):
            gu_transactions = paginate(gu_transactions, page=page)
            result = gu_transactions
            result['data'] = gu_transaction_schema.dump(gu_transactions['data'])
        else:
            result = gu_transaction_schema.dump(gu_transactions.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        gu_transaction:GUTransaction = session.query(GUTransaction)\
            .filter(GUTransaction.deleted_at == None,
                    GUTransaction.id == id).first()
        
        if gu_transaction is None: raise NotFound('gu_transaction not found')

        result = GUTransactionSchema().dump(gu_transaction)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        gu_transaction:GUTransaction = session.query(GUTransaction)\
            .filter(User.id == current_user.id,
                    GUTransaction.deleted_at == None,
                    GUTransaction.id == id).first()
        
        if gu_transaction is None: raise NotFound('gu_transaction not found')

        result = GUTransactionSchema().dump(gu_transaction)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            gu_transaction = GUTransaction(
                re_mode_paiement_id = validated_data.re_mode_paiement_id,
                gu_demande_id = validated_data.gu_demande_id,
                user_id = validated_data.user_id,
                reference = validated_data.reference,
                montant = validated_data.montant,
                devise = validated_data.devise,
                date_transaction = validated_data.date_transaction,
                heure = validated_data.heure,
                statut = validated_data.statut,
                
            )

            session.add(gu_transaction)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUTransactionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            gu_transaction = GUTransaction(
                re_mode_paiement_id = validated_data.re_mode_paiement_id,
                gu_demande_id = validated_data.gu_demande_id,

                reference = validated_data.reference,
                montant = validated_data.montant,
                devise = validated_data.devise,
                date_transaction = validated_data.date_transaction,
                heure = validated_data.heure,
                statut = validated_data.statut,
                
                user_id = current_user.id,
            )

            session.add(gu_transaction)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUTransactionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            gu_transaction: GUTransaction = session.query(GUTransaction).filter(
                GUTransaction.id == id, GUTransaction.deleted_at == None).first()

            if gu_transaction is None: raise NotFound('gu_transaction not found')

            gu_transaction.re_mode_paiement_id = validated_data.re_mode_paiement_id
            gu_transaction.gu_demande_id = validated_data.gu_demande_id
            gu_transaction.user_id = validated_data.user_id
            gu_transaction.reference = validated_data.reference
            gu_transaction.montant = validated_data.montant
            gu_transaction.devise = validated_data.devise
            gu_transaction.date_transaction = validated_data.date_transaction
            gu_transaction.heure = validated_data.heure
            gu_transaction.statut = validated_data.statut
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUTransactionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            gu_transaction: GUTransaction = session.query(GUTransaction).filter(
                User.id == current_user.id,
                GUTransaction.id == id, 
                GUTransaction.deleted_at == None).first()

            if gu_transaction is None: raise NotFound('gu_transaction not found')

            gu_transaction.re_mode_paiement_id = validated_data.re_mode_paiement_id
            gu_transaction.gu_demande_id = validated_data.gu_demande_id
            gu_transaction.user_id = validated_data.user_id
            gu_transaction.reference = validated_data.reference
            gu_transaction.montant = validated_data.montant
            gu_transaction.devise = validated_data.devise
            gu_transaction.date_transaction = validated_data.date_transaction
            gu_transaction.heure = validated_data.heure
            gu_transaction.statut = validated_data.statut
            
            gu_transaction.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUTransactionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            gu_transaction:GUTransaction = session.query(GUTransaction)\
                .filter(GUTransaction.deleted_at == None,
                        GUTransaction.id == id).first()
            if gu_transaction is None: raise NotFound('gu_transaction not found')

            gu_transaction.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            gu_transaction:GUTransaction = session.query(GUTransaction)\
                .filter(User.deleted_at == current_user.id,
                        GUTransaction.deleted_at == None,
                        GUTransaction.id == id).first()

            if gu_transaction is None: raise NotFound('gu_transaction not found')

            gu_transaction.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK