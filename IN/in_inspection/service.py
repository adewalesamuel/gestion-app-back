import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import INInspection
from .schema import INInspectionSchema


class INInspectionService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        in_inspection_schema = INInspectionSchema(many=True)
        page = request.args.get('page', '')
        in_inspections = session.query(INInspection)\
                .filter(INInspection.deleted_at == None)\
                .order_by(INInspection.created_at.desc())

        if (page != ''):
            in_inspections = paginate(in_inspections, page=page)
            result = in_inspections
            result['data'] = in_inspection_schema.dump(in_inspections['data'])
        else:
            result = in_inspection_schema.dump(in_inspections.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        in_inspection_schema = INInspectionSchema(many=True)
        page = request.args.get('page', '')
        in_inspections = session.query(INInspection)\
                .filter(INInspection.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(INInspection.created_at.desc())

        if (page != ''):
            in_inspections = paginate(in_inspections, page=page)
            result = in_inspections
            result['data'] = in_inspection_schema.dump(in_inspections['data'])
        else:
            result = in_inspection_schema.dump(in_inspections.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        in_inspection:INInspection = session.query(INInspection)\
            .filter(INInspection.deleted_at == None,
                    INInspection.id == id).first()
        
        if in_inspection is None: raise NotFound('in_inspection not found')

        result = INInspectionSchema().dump(in_inspection)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        in_inspection:INInspection = session.query(INInspection)\
            .filter(User.id == current_user.id,
                    INInspection.deleted_at == None,
                    INInspection.id == id).first()
        
        if in_inspection is None: raise NotFound('in_inspection not found')

        result = INInspectionSchema().dump(in_inspection)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            in_inspection = INInspection(
                in_type_controle_id = validated_data.in_type_controle_id,
                in_equipe_inspection_id = validated_data.in_equipe_inspection_id,
                rc_engin_flottant_id = validated_data.rc_engin_flottant_id,
                user_id = validated_data.user_id,
                reference = validated_data.reference,
                date_planifiee = validated_data.date_planifiee,
                heure = validated_data.heure,
                date_reelle = validated_data.date_reelle,
                statut = validated_data.statut,
                resultat = validated_data.resultat,
                
            )

            session.add(in_inspection)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INInspectionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            in_inspection = INInspection(
                in_type_controle_id = validated_data.in_type_controle_id,
                in_equipe_inspection_id = validated_data.in_equipe_inspection_id,
                rc_engin_flottant_id = validated_data.rc_engin_flottant_id,
                reference = validated_data.reference,
                date_planifiee = validated_data.date_planifiee,
                heure = validated_data.heure,
                date_reelle = validated_data.date_reelle,
                statut = validated_data.statut,
                resultat = validated_data.resultat,
                
                user_id = current_user.id,
            )

            session.add(in_inspection)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INInspectionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            in_inspection: INInspection = session.query(INInspection).filter(
                INInspection.id == id, INInspection.deleted_at == None).first()

            if in_inspection is None: raise NotFound('in_inspection not found')

            in_inspection.in_type_controle_id = validated_data.in_type_controle_id
            in_inspection.in_equipe_inspection_id = validated_data.in_equipe_inspection_id
            in_inspection.rc_engin_flottant_id = validated_data.rc_engin_flottant_id
            in_inspection.user_id = validated_data.user_id
            in_inspection.reference = validated_data.reference
            in_inspection.date_planifiee = validated_data.date_planifiee
            in_inspection.heure = validated_data.heure
            in_inspection.date_reelle = validated_data.date_reelle
            in_inspection.statut = validated_data.statut
            in_inspection.resultat = validated_data.resultat
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INInspectionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            in_inspection: INInspection = session.query(INInspection).filter(
                User.id == current_user.id,
                INInspection.id == id, 
                INInspection.deleted_at == None).first()

            if in_inspection is None: raise NotFound('in_inspection not found')

            in_inspection.in_type_controle_id = validated_data.in_type_controle_id
            in_inspection.in_equipe_inspection_id = validated_data.in_equipe_inspection_id
            in_inspection.rc_engin_flottant_id = validated_data.rc_engin_flottant_id
            in_inspection.user_id = validated_data.user_id
            in_inspection.reference = validated_data.reference
            in_inspection.date_planifiee = validated_data.date_planifiee
            in_inspection.heure = validated_data.heure
            in_inspection.date_reelle = validated_data.date_reelle
            in_inspection.statut = validated_data.statut
            in_inspection.resultat = validated_data.resultat
            
            in_inspection.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INInspectionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            in_inspection:INInspection = session.query(INInspection)\
                .filter(INInspection.deleted_at == None,
                        INInspection.id == id).first()
            if in_inspection is None: raise NotFound('in_inspection not found')

            in_inspection.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            in_inspection:INInspection = session.query(INInspection)\
                .filter(User.deleted_at == current_user.id,
                        INInspection.deleted_at == None,
                        INInspection.id == id).first()

            if in_inspection is None: raise NotFound('in_inspection not found')

            in_inspection.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK