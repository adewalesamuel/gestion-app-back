import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import RCEquipement
from .schema import RCEquipementSchema


class RCEquipementService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        rc_equipement_schema = RCEquipementSchema(many=True)
        page = request.args.get('page', '')
        rc_equipements = session.query(RCEquipement)\
                .filter(RCEquipement.deleted_at == None)\
                .order_by(RCEquipement.created_at.desc())

        if (page != ''):
            rc_equipements = paginate(rc_equipements, page=page)
            result = rc_equipements
            result['data'] = rc_equipement_schema.dump(rc_equipements['data'])
        else:
            result = rc_equipement_schema.dump(rc_equipements.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        rc_equipement_schema = RCEquipementSchema(many=True)
        page = request.args.get('page', '')
        rc_equipements = session.query(RCEquipement)\
                .filter(RCEquipement.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(RCEquipement.created_at.desc())

        if (page != ''):
            rc_equipements = paginate(rc_equipements, page=page)
            result = rc_equipements
            result['data'] = rc_equipement_schema.dump(rc_equipements['data'])
        else:
            result = rc_equipement_schema.dump(rc_equipements.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        rc_equipement:RCEquipement = session.query(RCEquipement)\
            .filter(RCEquipement.deleted_at == None,
                    RCEquipement.id == id).first()
        
        if rc_equipement is None: raise NotFound('rc_equipement not found')

        result = RCEquipementSchema().dump(rc_equipement)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        rc_equipement:RCEquipement = session.query(RCEquipement)\
            .filter(User.id == current_user.id,
                    RCEquipement.deleted_at == None,
                    RCEquipement.id == id).first()
        
        if rc_equipement is None: raise NotFound('rc_equipement not found')

        result = RCEquipementSchema().dump(rc_equipement)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            rc_equipement = RCEquipement(
                rc_engin_flottant_id = validated_data.rc_engin_flottant_id,
                nom = validated_data.nom,
                type = validated_data.type,
                numero_serie = validated_data.numero_serie,
                date_installation = validated_data.date_installation,
                
            )

            session.add(rc_equipement)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCEquipementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            rc_equipement = RCEquipement(
                rc_engin_flottant_id = validated_data.rc_engin_flottant_id,
                nom = validated_data.nom,
                type = validated_data.type,
                numero_serie = validated_data.numero_serie,
                date_installation = validated_data.date_installation,
                
                user_id = current_user.id,
            )

            session.add(rc_equipement)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCEquipementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            rc_equipement: RCEquipement = session.query(RCEquipement).filter(
                RCEquipement.id == id, RCEquipement.deleted_at == None).first()

            if rc_equipement is None: raise NotFound('rc_equipement not found')

            rc_equipement.rc_engin_flottant_id = validated_data.rc_engin_flottant_id
            rc_equipement.nom = validated_data.nom
            rc_equipement.type = validated_data.type
            rc_equipement.numero_serie = validated_data.numero_serie
            rc_equipement.date_installation = validated_data.date_installation
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCEquipementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            rc_equipement: RCEquipement = session.query(RCEquipement).filter(
                User.id == current_user.id,
                RCEquipement.id == id, 
                RCEquipement.deleted_at == None).first()

            if rc_equipement is None: raise NotFound('rc_equipement not found')

            rc_equipement.rc_engin_flottant_id = validated_data.rc_engin_flottant_id
            rc_equipement.nom = validated_data.nom
            rc_equipement.type = validated_data.type
            rc_equipement.numero_serie = validated_data.numero_serie
            rc_equipement.date_installation = validated_data.date_installation
            
            rc_equipement.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCEquipementSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            rc_equipement:RCEquipement = session.query(RCEquipement)\
                .filter(RCEquipement.deleted_at == None,
                        RCEquipement.id == id).first()
            if rc_equipement is None: raise NotFound('rc_equipement not found')

            rc_equipement.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            rc_equipement:RCEquipement = session.query(RCEquipement)\
                .filter(User.deleted_at == current_user.id,
                        RCEquipement.deleted_at == None,
                        RCEquipement.id == id).first()

            if rc_equipement is None: raise NotFound('rc_equipement not found')

            rc_equipement.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK