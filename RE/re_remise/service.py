import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import RERemise
from .schema import RERemiseSchema


class RERemiseService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        re_remise_schema = RERemiseSchema(many=True)
        page = request.args.get('page', '')
        re_remises = session.query(RERemise)\
                .filter(RERemise.deleted_at == None)\
                .order_by(RERemise.created_at.desc())

        if (page != ''):
            re_remises = paginate(re_remises, page=page)
            result = re_remises
            result['data'] = re_remise_schema.dump(re_remises['data'])
        else:
            result = re_remise_schema.dump(re_remises.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        re_remise_schema = RERemiseSchema(many=True)
        page = request.args.get('page', '')
        re_remises = session.query(RERemise)\
                .filter(RERemise.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(RERemise.created_at.desc())

        if (page != ''):
            re_remises = paginate(re_remises, page=page)
            result = re_remises
            result['data'] = re_remise_schema.dump(re_remises['data'])
        else:
            result = re_remise_schema.dump(re_remises.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        re_remise:RERemise = session.query(RERemise)\
            .filter(RERemise.deleted_at == None,
                    RERemise.id == id).first()
        
        if re_remise is None: raise NotFound('re_remise not found')

        result = RERemiseSchema().dump(re_remise)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        re_remise:RERemise = session.query(RERemise)\
            .filter(User.id == current_user.id,
                    RERemise.deleted_at == None,
                    RERemise.id == id).first()
        
        if re_remise is None: raise NotFound('re_remise not found')

        result = RERemiseSchema().dump(re_remise)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            re_remise = RERemise(
                re_ordre_recette_id = validated_data.re_ordre_recette_id,
                user_id = validated_data.user_id,
                montant = validated_data.montant,
                pourcentage = validated_data.pourcentage,
                raison = validated_data.raison,
                
            )

            session.add(re_remise)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RERemiseSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            re_remise = RERemise(
                re_ordre_recette_id = validated_data.re_ordre_recette_id,
                montant = validated_data.montant,
                pourcentage = validated_data.pourcentage,
                raison = validated_data.raison,
                
                user_id = current_user.id,
            )

            session.add(re_remise)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RERemiseSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            re_remise: RERemise = session.query(RERemise).filter(
                RERemise.id == id, RERemise.deleted_at == None).first()

            if re_remise is None: raise NotFound('re_remise not found')

            re_remise.re_ordre_recette_id = validated_data.re_ordre_recette_id
            re_remise.user_id = validated_data.user_id
            re_remise.montant = validated_data.montant
            re_remise.pourcentage = validated_data.pourcentage
            re_remise.raison = validated_data.raison
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RERemiseSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            re_remise: RERemise = session.query(RERemise).filter(
                User.id == current_user.id,
                RERemise.id == id, 
                RERemise.deleted_at == None).first()

            if re_remise is None: raise NotFound('re_remise not found')

            re_remise.re_ordre_recette_id = validated_data.re_ordre_recette_id
            re_remise.user_id = validated_data.user_id
            re_remise.montant = validated_data.montant
            re_remise.pourcentage = validated_data.pourcentage
            re_remise.raison = validated_data.raison
            
            re_remise.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RERemiseSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            re_remise:RERemise = session.query(RERemise)\
                .filter(RERemise.deleted_at == None,
                        RERemise.id == id).first()
            if re_remise is None: raise NotFound('re_remise not found')

            re_remise.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            re_remise:RERemise = session.query(RERemise)\
                .filter(User.deleted_at == current_user.id,
                        RERemise.deleted_at == None,
                        RERemise.id == id).first()

            if re_remise is None: raise NotFound('re_remise not found')

            re_remise.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK