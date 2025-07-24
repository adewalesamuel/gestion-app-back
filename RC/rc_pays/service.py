import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import RCPays
from .schema import RCPaysSchema


class RCPaysService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        rc_pays_schema = RCPaysSchema(many=True)
        page = request.args.get('page', '')
        rc_payss = session.query(RCPays)\
                .filter(RCPays.deleted_at == None)\
                .order_by(RCPays.created_at.desc())

        if (page != ''):
            rc_payss = paginate(rc_payss, page=page)
            result = rc_payss
            result['data'] = rc_pays_schema.dump(rc_payss['data'])
        else:
            result = rc_pays_schema.dump(rc_payss.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        rc_pays_schema = RCPaysSchema(many=True)
        page = request.args.get('page', '')
        rc_payss = session.query(RCPays)\
                .filter(RCPays.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(RCPays.created_at.desc())

        if (page != ''):
            rc_payss = paginate(rc_payss, page=page)
            result = rc_payss
            result['data'] = rc_pays_schema.dump(rc_payss['data'])
        else:
            result = rc_pays_schema.dump(rc_payss.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        rc_pays:RCPays = session.query(RCPays)\
            .filter(RCPays.deleted_at == None,
                    RCPays.id == id).first()
        
        if rc_pays is None: raise NotFound('rc_pays not found')

        result = RCPaysSchema().dump(rc_pays)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        rc_pays:RCPays = session.query(RCPays)\
            .filter(User.id == current_user.id,
                    RCPays.deleted_at == None,
                    RCPays.id == id).first()
        
        if rc_pays is None: raise NotFound('rc_pays not found')

        result = RCPaysSchema().dump(rc_pays)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            rc_pays = RCPays(
                nom = validated_data.nom,
                code_iso = validated_data.code_iso,
                indicatif = validated_data.indicatif,
                pavillon_url = validated_data.pavillon_url,
                
            )

            session.add(rc_pays)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCPaysSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            rc_pays = RCPays(
                nom = validated_data.nom,
                code_iso = validated_data.code_iso,
                indicatif = validated_data.indicatif,
                pavillon_url = validated_data.pavillon_url,
                
                user_id = current_user.id,
            )

            session.add(rc_pays)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCPaysSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            rc_pays: RCPays = session.query(RCPays).filter(
                RCPays.id == id, RCPays.deleted_at == None).first()

            if rc_pays is None: raise NotFound('rc_pays not found')

            rc_pays.nom = validated_data.nom
            rc_pays.code_iso = validated_data.code_iso
            rc_pays.indicatif = validated_data.indicatif
            rc_pays.pavillon_url = validated_data.pavillon_url
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCPaysSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            rc_pays: RCPays = session.query(RCPays).filter(
                User.id == current_user.id,
                RCPays.id == id, 
                RCPays.deleted_at == None).first()

            if rc_pays is None: raise NotFound('rc_pays not found')

            rc_pays.nom = validated_data.nom
            rc_pays.code_iso = validated_data.code_iso
            rc_pays.indicatif = validated_data.indicatif
            rc_pays.pavillon_url = validated_data.pavillon_url
            
            rc_pays.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCPaysSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            rc_pays:RCPays = session.query(RCPays)\
                .filter(RCPays.deleted_at == None,
                        RCPays.id == id).first()
            if rc_pays is None: raise NotFound('rc_pays not found')

            rc_pays.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            rc_pays:RCPays = session.query(RCPays)\
                .filter(User.deleted_at == current_user.id,
                        RCPays.deleted_at == None,
                        RCPays.id == id).first()

            if rc_pays is None: raise NotFound('rc_pays not found')

            rc_pays.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK