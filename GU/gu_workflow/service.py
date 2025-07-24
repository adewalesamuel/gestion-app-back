import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import GUWorkflow
from .schema import GUWorkflowSchema


class GUWorkflowService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        gu_workflow_schema = GUWorkflowSchema(many=True)
        page = request.args.get('page', '')
        gu_workflows = session.query(GUWorkflow)\
                .filter(GUWorkflow.deleted_at == None)\
                .order_by(GUWorkflow.created_at.desc())

        if (page != ''):
            gu_workflows = paginate(gu_workflows, page=page)
            result = gu_workflows
            result['data'] = gu_workflow_schema.dump(gu_workflows['data'])
        else:
            result = gu_workflow_schema.dump(gu_workflows.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        gu_workflow_schema = GUWorkflowSchema(many=True)
        page = request.args.get('page', '')
        gu_workflows = session.query(GUWorkflow)\
                .filter(GUWorkflow.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(GUWorkflow.created_at.desc())

        if (page != ''):
            gu_workflows = paginate(gu_workflows, page=page)
            result = gu_workflows
            result['data'] = gu_workflow_schema.dump(gu_workflows['data'])
        else:
            result = gu_workflow_schema.dump(gu_workflows.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        gu_workflow:GUWorkflow = session.query(GUWorkflow)\
            .filter(GUWorkflow.deleted_at == None,
                    GUWorkflow.id == id).first()
        
        if gu_workflow is None: raise NotFound('gu_workflow not found')

        result = GUWorkflowSchema().dump(gu_workflow)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        gu_workflow:GUWorkflow = session.query(GUWorkflow)\
            .filter(User.id == current_user.id,
                    GUWorkflow.deleted_at == None,
                    GUWorkflow.id == id).first()
        
        if gu_workflow is None: raise NotFound('gu_workflow not found')

        result = GUWorkflowSchema().dump(gu_workflow)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            gu_workflow = GUWorkflow(
                etape = validated_data.etape,
                ordre = validated_data.ordre,
                role_id = validated_data.role_id,
                gu_type_demande_id = validated_data.gu_type_demande_id,
                
            )

            session.add(gu_workflow)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUWorkflowSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            gu_workflow = GUWorkflow(
                etape = validated_data.etape,
                ordre = validated_data.ordre,
                role_id = validated_data.role_id,
                gu_type_demande_id = validated_data.gu_type_demande_id,
                
                user_id = current_user.id,
            )

            session.add(gu_workflow)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUWorkflowSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            gu_workflow: GUWorkflow = session.query(GUWorkflow).filter(
                GUWorkflow.id == id, GUWorkflow.deleted_at == None).first()

            if gu_workflow is None: raise NotFound('gu_workflow not found')

            gu_workflow.etape = validated_data.etape
            gu_workflow.ordre = validated_data.ordre
            gu_workflow.role_id = validated_data.role_id
            gu_workflow.gu_type_demande_id = validated_data.gu_type_demande_id
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUWorkflowSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            gu_workflow: GUWorkflow = session.query(GUWorkflow).filter(
                User.id == current_user.id,
                GUWorkflow.id == id, 
                GUWorkflow.deleted_at == None).first()

            if gu_workflow is None: raise NotFound('gu_workflow not found')

            gu_workflow.etape = validated_data.etape
            gu_workflow.ordre = validated_data.ordre
            gu_workflow.role_id = validated_data.role_id
            gu_workflow.gu_type_demande_id = validated_data.gu_type_demande_id
            
            gu_workflow.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUWorkflowSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            gu_workflow:GUWorkflow = session.query(GUWorkflow)\
                .filter(GUWorkflow.deleted_at == None,
                        GUWorkflow.id == id).first()
            if gu_workflow is None: raise NotFound('gu_workflow not found')

            gu_workflow.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            gu_workflow:GUWorkflow = session.query(GUWorkflow)\
                .filter(User.deleted_at == current_user.id,
                        GUWorkflow.deleted_at == None,
                        GUWorkflow.id == id).first()

            if gu_workflow is None: raise NotFound('gu_workflow not found')

            gu_workflow.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK