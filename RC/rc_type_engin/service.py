import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import RCTypeEngin
from .schema import RCTypeEnginSchema


class RCTypeEnginService:
    @staticmethod
    def index(current_user: User | None):
        result = []
        rc_type_engin_schema = RCTypeEnginSchema(many=True)
        page = request.args.get('page', '')
        rc_type_engins = session.query(RCTypeEngin)\
                .filter(RCTypeEngin.deleted_at == None)\
                .order_by(RCTypeEngin.created_at.desc())

        if (page != ''):
            rc_type_engins = paginate(rc_type_engins, page=page)
            result = rc_type_engins
            result['data'] = rc_type_engin_schema.dump(rc_type_engins['data'])
        else:
            result = rc_type_engin_schema.dump(rc_type_engins.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user: User | None, id: int):
        rc_type_engin:RCTypeEngin = session.query(RCTypeEngin)\
            .filter(RCTypeEngin.deleted_at == None,
                    RCTypeEngin.id == id).first()
        
        if rc_type_engin is None: raise NotFound('rc_type_engin not found')

        result = RCTypeEnginSchema().dump(rc_type_engin)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user: User | None, validated_data):
        try:
            rc_type_engin = RCTypeEngin(
                code = validated_data.code,
                libelle = validated_data.libelle,
                categorie = validated_data.categorie,
                tonnage_min = validated_data.tonnage_min,
                tonnage_max = validated_data.tonnage_max,
                
            )

            session.add(rc_type_engin)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCTypeEnginSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user: User | None, id: int, validated_data):
        try:
            rc_type_engin: RCTypeEngin = session.query(RCTypeEngin).filter(
                RCTypeEngin.id == id, RCTypeEngin.deleted_at == None).first()

            if rc_type_engin is None: raise NotFound('rc_type_engin not found')

            rc_type_engin.code = validated_data.code
            rc_type_engin.libelle = validated_data.libelle
            rc_type_engin.categorie = validated_data.categorie
            rc_type_engin.tonnage_min = validated_data.tonnage_min
            rc_type_engin.tonnage_max = validated_data.tonnage_max
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCTypeEnginSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def delete(current_user: User | None, id: int):    
        try:
            rc_type_engin:RCTypeEngin = session.query(RCTypeEngin)\
                .filter(RCTypeEngin.deleted_at == None,
                        RCTypeEngin.id == id).first()
            if rc_type_engin is None: raise NotFound('rc_type_engin not found')

            rc_type_engin.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK