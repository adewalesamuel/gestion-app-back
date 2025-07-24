import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import RCCertificat
from .schema import RCCertificatSchema


class RCCertificatService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        rc_certificat_schema = RCCertificatSchema(many=True)
        page = request.args.get('page', '')
        rc_certificats = session.query(RCCertificat)\
                .filter(RCCertificat.deleted_at == None)\
                .order_by(RCCertificat.created_at.desc())

        if (page != ''):
            rc_certificats = paginate(rc_certificats, page=page)
            result = rc_certificats
            result['data'] = rc_certificat_schema.dump(rc_certificats['data'])
        else:
            result = rc_certificat_schema.dump(rc_certificats.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        rc_certificat_schema = RCCertificatSchema(many=True)
        page = request.args.get('page', '')
        rc_certificats = session.query(RCCertificat)\
                .filter(RCCertificat.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(RCCertificat.created_at.desc())

        if (page != ''):
            rc_certificats = paginate(rc_certificats, page=page)
            result = rc_certificats
            result['data'] = rc_certificat_schema.dump(rc_certificats['data'])
        else:
            result = rc_certificat_schema.dump(rc_certificats.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        rc_certificat:RCCertificat = session.query(RCCertificat)\
            .filter(RCCertificat.deleted_at == None,
                    RCCertificat.id == id).first()
        
        if rc_certificat is None: raise NotFound('rc_certificat not found')

        result = RCCertificatSchema().dump(rc_certificat)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        rc_certificat:RCCertificat = session.query(RCCertificat)\
            .filter(User.id == current_user.id,
                    RCCertificat.deleted_at == None,
                    RCCertificat.id == id).first()
        
        if rc_certificat is None: raise NotFound('rc_certificat not found')

        result = RCCertificatSchema().dump(rc_certificat)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            rc_certificat = RCCertificat(
                rc_engin_flottant_id = validated_data.rc_engin_flottant_id,
                type = validated_data.type,
                numero = validated_data.numero,
                date_emission = validated_data.date_emission,
                date_expiration = validated_data.date_expiration,
                organisme_emetteur = validated_data.organisme_emetteur,
                
            )

            session.add(rc_certificat)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCCertificatSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            rc_certificat = RCCertificat(
                rc_engin_flottant_id = validated_data.rc_engin_flottant_id,
                type = validated_data.type,
                numero = validated_data.numero,
                date_emission = validated_data.date_emission,
                date_expiration = validated_data.date_expiration,
                organisme_emetteur = validated_data.organisme_emetteur,
                
                user_id = current_user.id,
            )

            session.add(rc_certificat)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCCertificatSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            rc_certificat: RCCertificat = session.query(RCCertificat).filter(
                RCCertificat.id == id, RCCertificat.deleted_at == None).first()

            if rc_certificat is None: raise NotFound('rc_certificat not found')

            rc_certificat.rc_engin_flottant_id = validated_data.rc_engin_flottant_id
            rc_certificat.type = validated_data.type
            rc_certificat.numero = validated_data.numero
            rc_certificat.date_emission = validated_data.date_emission
            rc_certificat.date_expiration = validated_data.date_expiration
            rc_certificat.organisme_emetteur = validated_data.organisme_emetteur
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCCertificatSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            rc_certificat: RCCertificat = session.query(RCCertificat).filter(
                User.id == current_user.id,
                RCCertificat.id == id, 
                RCCertificat.deleted_at == None).first()

            if rc_certificat is None: raise NotFound('rc_certificat not found')

            rc_certificat.rc_engin_flottant_id = validated_data.rc_engin_flottant_id
            rc_certificat.type = validated_data.type
            rc_certificat.numero = validated_data.numero
            rc_certificat.date_emission = validated_data.date_emission
            rc_certificat.date_expiration = validated_data.date_expiration
            rc_certificat.organisme_emetteur = validated_data.organisme_emetteur
            
            rc_certificat.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCCertificatSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            rc_certificat:RCCertificat = session.query(RCCertificat)\
                .filter(RCCertificat.deleted_at == None,
                        RCCertificat.id == id).first()
            if rc_certificat is None: raise NotFound('rc_certificat not found')

            rc_certificat.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            rc_certificat:RCCertificat = session.query(RCCertificat)\
                .filter(User.deleted_at == current_user.id,
                        RCCertificat.deleted_at == None,
                        RCCertificat.id == id).first()

            if rc_certificat is None: raise NotFound('rc_certificat not found')

            rc_certificat.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK