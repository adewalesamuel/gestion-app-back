import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import RETarif
from .schema import RETarifSchema


class RETarifService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        re_tarif_schema = RETarifSchema(many=True)
        page = request.args.get('page', '')
        re_tarifs = session.query(RETarif)\
                .filter(RETarif.deleted_at == None)\
                .order_by(RETarif.created_at.desc())

        if (page != ''):
            re_tarifs = paginate(re_tarifs, page=page)
            result = re_tarifs
            result['data'] = re_tarif_schema.dump(re_tarifs['data'])
        else:
            result = re_tarif_schema.dump(re_tarifs.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        re_tarif_schema = RETarifSchema(many=True)
        page = request.args.get('page', '')
        re_tarifs = session.query(RETarif)\
                .filter(RETarif.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(RETarif.created_at.desc())

        if (page != ''):
            re_tarifs = paginate(re_tarifs, page=page)
            result = re_tarifs
            result['data'] = re_tarif_schema.dump(re_tarifs['data'])
        else:
            result = re_tarif_schema.dump(re_tarifs.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        re_tarif:RETarif = session.query(RETarif)\
            .filter(RETarif.deleted_at == None,
                    RETarif.id == id).first()
        
        if re_tarif is None: raise NotFound('re_tarif not found')

        result = RETarifSchema().dump(re_tarif)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        re_tarif:RETarif = session.query(RETarif)\
            .filter(User.id == current_user.id,
                    RETarif.deleted_at == None,
                    RETarif.id == id).first()
        
        if re_tarif is None: raise NotFound('re_tarif not found')

        result = RETarifSchema().dump(re_tarif)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            re_tarif = RETarif(
                service = validated_data.service,
                montant = validated_data.montant,
                devise = validated_data.devise,
                frequence = validated_data.frequence,
                type_acteur = validated_data.type_acteur,
                
            )

            session.add(re_tarif)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RETarifSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            re_tarif = RETarif(
                service = validated_data.service,
                montant = validated_data.montant,
                devise = validated_data.devise,
                frequence = validated_data.frequence,
                type_acteur = validated_data.type_acteur,
                
                user_id = current_user.id,
            )

            session.add(re_tarif)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RETarifSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            re_tarif: RETarif = session.query(RETarif).filter(
                RETarif.id == id, RETarif.deleted_at == None).first()

            if re_tarif is None: raise NotFound('re_tarif not found')

            re_tarif.service = validated_data.service
            re_tarif.montant = validated_data.montant
            re_tarif.devise = validated_data.devise
            re_tarif.frequence = validated_data.frequence
            re_tarif.type_acteur = validated_data.type_acteur
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RETarifSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            re_tarif: RETarif = session.query(RETarif).filter(
                User.id == current_user.id,
                RETarif.id == id, 
                RETarif.deleted_at == None).first()

            if re_tarif is None: raise NotFound('re_tarif not found')

            re_tarif.service = validated_data.service
            re_tarif.montant = validated_data.montant
            re_tarif.devise = validated_data.devise
            re_tarif.frequence = validated_data.frequence
            re_tarif.type_acteur = validated_data.type_acteur
            
            re_tarif.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RETarifSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            re_tarif:RETarif = session.query(RETarif)\
                .filter(RETarif.deleted_at == None,
                        RETarif.id == id).first()
            if re_tarif is None: raise NotFound('re_tarif not found')

            re_tarif.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            re_tarif:RETarif = session.query(RETarif)\
                .filter(User.deleted_at == current_user.id,
                        RETarif.deleted_at == None,
                        RETarif.id == id).first()

            if re_tarif is None: raise NotFound('re_tarif not found')

            re_tarif.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK