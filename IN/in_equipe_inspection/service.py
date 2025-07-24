import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import INEquipeInspection
from .schema import INEquipeInspectionSchema


class INEquipeInspectionService:
    @staticmethod
    def index(current_user: User | None):
        result = []
        in_equipe_inspection_schema = INEquipeInspectionSchema(many=True)
        page = request.args.get('page', '')
        in_equipe_inspections = session.query(INEquipeInspection)\
                .filter(INEquipeInspection.deleted_at == None)\
                .order_by(INEquipeInspection.created_at.desc())

        if (page != ''):
            in_equipe_inspections = paginate(in_equipe_inspections, page=page)
            result = in_equipe_inspections
            result['data'] = in_equipe_inspection_schema.dump(in_equipe_inspections['data'])
        else:
            result = in_equipe_inspection_schema.dump(in_equipe_inspections.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user: User | None):
        result = []
        in_equipe_inspection_schema = INEquipeInspectionSchema(many=True)
        page = request.args.get('page', '')
        in_equipe_inspections = session.query(INEquipeInspection)\
                .filter(INEquipeInspection.deleted_at == None,
                        INEquipeInspection.user_id == current_user.id)\
                .order_by(INEquipeInspection.created_at.desc())

        if (page != ''):
            in_equipe_inspections = paginate(in_equipe_inspections, page=page)
            result = in_equipe_inspections
            result['data'] = in_equipe_inspection_schema.dump(in_equipe_inspections['data'])
        else:
            result = in_equipe_inspection_schema.dump(in_equipe_inspections.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user: User | None, id: int):
        in_equipe_inspection:INEquipeInspection = session.query(INEquipeInspection)\
            .filter(INEquipeInspection.deleted_at == None,
                    INEquipeInspection.id == id).first()
        
        if in_equipe_inspection is None: raise NotFound('in_equipe_inspection not found')

        result = INEquipeInspectionSchema().dump(in_equipe_inspection)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user: User | None, id: int):
        in_equipe_inspection:INEquipeInspection = session.query(INEquipeInspection)\
            .filter(INEquipeInspection.user_id == current_user.id,
                    INEquipeInspection.deleted_at == None,
                    INEquipeInspection.id == id).first()
        
        if in_equipe_inspection is None: raise NotFound('in_equipe_inspection not found')

        result = INEquipeInspectionSchema().dump(in_equipe_inspection)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user: User | None, validated_data):
        try:
            in_equipe_inspection = INEquipeInspection(
                user_id = validated_data.user_id,
                nom = validated_data.nom,
                membres = validated_data.membres,
                
            )

            session.add(in_equipe_inspection)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INEquipeInspectionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user: User | None, validated_data):
        try:
            in_equipe_inspection = INEquipeInspection(
                nom = validated_data.nom,
                membres = validated_data.membres,
                
                user_id = current_user.id,
            )

            session.add(in_equipe_inspection)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INEquipeInspectionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user: User | None, id: int, validated_data):
        try:
            in_equipe_inspection: INEquipeInspection = session.query(INEquipeInspection).filter(
                INEquipeInspection.id == id, INEquipeInspection.deleted_at == None).first()

            if in_equipe_inspection is None: raise NotFound('in_equipe_inspection not found')

            in_equipe_inspection.user_id = validated_data.user_id
            in_equipe_inspection.nom = validated_data.nom
            in_equipe_inspection.membres = validated_data.membres
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INEquipeInspectionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user: User | None, id: int, validated_data):
        try:
            in_equipe_inspection: INEquipeInspection = session.query(INEquipeInspection).filter(
                INEquipeInspection.user_id == current_user.id,
                INEquipeInspection.id == id, 
                INEquipeInspection.deleted_at == None).first()

            if in_equipe_inspection is None: raise NotFound('in_equipe_inspection not found')

            in_equipe_inspection.user_id = validated_data.user_id
            in_equipe_inspection.nom = validated_data.nom
            in_equipe_inspection.membres = validated_data.membres
            
            in_equipe_inspection.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INEquipeInspectionSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user: User | None, id: int):    
        try:
            in_equipe_inspection:INEquipeInspection = session.query(INEquipeInspection)\
                .filter(INEquipeInspection.deleted_at == None,
                        INEquipeInspection.id == id).first()
            if in_equipe_inspection is None: raise NotFound('in_equipe_inspection not found')

            in_equipe_inspection.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user: User | None, id: int):    
        try:
            in_equipe_inspection:INEquipeInspection = session.query(INEquipeInspection)\
                .filter(User.deleted_at == current_user.id,
                        INEquipeInspection.deleted_at == None,
                        INEquipeInspection.id == id).first()

            if in_equipe_inspection is None: raise NotFound('in_equipe_inspection not found')

            in_equipe_inspection.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK