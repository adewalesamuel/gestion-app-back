import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import INChecklist
from .schema import INChecklistSchema


class INChecklistService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        in_checklist_schema = INChecklistSchema(many=True)
        page = request.args.get('page', '')
        in_checklists = session.query(INChecklist)\
                .filter(INChecklist.deleted_at == None)\
                .order_by(INChecklist.created_at.desc())

        if (page != ''):
            in_checklists = paginate(in_checklists, page=page)
            result = in_checklists
            result['data'] = in_checklist_schema.dump(in_checklists['data'])
        else:
            result = in_checklist_schema.dump(in_checklists.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        in_checklist_schema = INChecklistSchema(many=True)
        page = request.args.get('page', '')
        in_checklists = session.query(INChecklist)\
                .filter(INChecklist.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(INChecklist.created_at.desc())

        if (page != ''):
            in_checklists = paginate(in_checklists, page=page)
            result = in_checklists
            result['data'] = in_checklist_schema.dump(in_checklists['data'])
        else:
            result = in_checklist_schema.dump(in_checklists.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        in_checklist:INChecklist = session.query(INChecklist)\
            .filter(INChecklist.deleted_at == None,
                    INChecklist.id == id).first()
        
        if in_checklist is None: raise NotFound('in_checklist not found')

        result = INChecklistSchema().dump(in_checklist)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        in_checklist:INChecklist = session.query(INChecklist)\
            .filter(User.id == current_user.id,
                    INChecklist.deleted_at == None,
                    INChecklist.id == id).first()
        
        if in_checklist is None: raise NotFound('in_checklist not found')

        result = INChecklistSchema().dump(in_checklist)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            in_checklist = INChecklist(
                rc_type_engin_id = validated_data.rc_type_engin_id,
                nom = validated_data.nom,
                version = validated_data.version,
                items = validated_data.items,
                
            )

            session.add(in_checklist)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INChecklistSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            in_checklist = INChecklist(
                rc_type_engin_id = validated_data.rc_type_engin_id,
                nom = validated_data.nom,
                version = validated_data.version,
                items = validated_data.items,
                
                user_id = current_user.id,
            )

            session.add(in_checklist)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INChecklistSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            in_checklist: INChecklist = session.query(INChecklist).filter(
                INChecklist.id == id, INChecklist.deleted_at == None).first()

            if in_checklist is None: raise NotFound('in_checklist not found')

            in_checklist.rc_type_engin_id = validated_data.rc_type_engin_id
            in_checklist.nom = validated_data.nom
            in_checklist.version = validated_data.version
            in_checklist.items = validated_data.items
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INChecklistSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            in_checklist: INChecklist = session.query(INChecklist).filter(
                User.id == current_user.id,
                INChecklist.id == id, 
                INChecklist.deleted_at == None).first()

            if in_checklist is None: raise NotFound('in_checklist not found')

            in_checklist.rc_type_engin_id = validated_data.rc_type_engin_id
            in_checklist.nom = validated_data.nom
            in_checklist.version = validated_data.version
            in_checklist.items = validated_data.items
            
            in_checklist.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INChecklistSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            in_checklist:INChecklist = session.query(INChecklist)\
                .filter(INChecklist.deleted_at == None,
                        INChecklist.id == id).first()
            if in_checklist is None: raise NotFound('in_checklist not found')

            in_checklist.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            in_checklist:INChecklist = session.query(INChecklist)\
                .filter(User.deleted_at == current_user.id,
                        INChecklist.deleted_at == None,
                        INChecklist.id == id).first()

            if in_checklist is None: raise NotFound('in_checklist not found')

            in_checklist.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK