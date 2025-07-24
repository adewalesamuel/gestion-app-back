import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
from ..user.model import User
from .model import AuditLog
from .schema import AuditLogSchema


class AuditLogService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        audit_log_schema = AuditLogSchema(many=True)
        page = request.args.get('page', '')
        audit_logs = session.query(AuditLog)\
                .filter(AuditLog.deleted_at == None)\
                .order_by(AuditLog.created_at.desc())

        if (page != ''):
            audit_logs = paginate(audit_logs, page=page)
            result = audit_logs
            result['data'] = audit_log_schema.dump(audit_logs['data'])
        else:
            result = audit_log_schema.dump(audit_logs.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        audit_log_schema = AuditLogSchema(many=True)
        page = request.args.get('page', '')
        audit_logs = session.query(AuditLog)\
                .filter(AuditLog.deleted_at == None,
                        AuditLog.user_id == current_user.id)\
                .order_by(AuditLog.created_at.desc())

        if (page != ''):
            audit_logs = paginate(audit_logs, page=page)
            result = audit_logs
            result['data'] = audit_log_schema.dump(audit_logs['data'])
        else:
            result = audit_log_schema.dump(audit_logs.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        audit_log:AuditLog = session.query(AuditLog)\
            .filter(AuditLog.deleted_at == None,
                    AuditLog.id == id).first()
        
        if audit_log is None: raise NotFound('audit_log not found')

        result = AuditLogSchema().dump(audit_log)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        audit_log:AuditLog = session.query(AuditLog)\
            .filter(AuditLog.user_id == current_user.id,
                    AuditLog.deleted_at == None,
                    AuditLog.id == id).first()
        
        if audit_log is None: raise NotFound('audit_log not found')

        result = AuditLogSchema().dump(audit_log)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            audit_log = AuditLog(
                user_id = validated_data.user_id,
                action = validated_data.action,
                entite = validated_data.entite,
                entite_id = validated_data.entite_id,
                ancienne_valeur = validated_data.ancienne_valeur,
                nouvelle_valeur = validated_data.nouvelle_valeur,
                ip_address = validated_data.ip_address,
                
            )

            session.add(audit_log)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': AuditLogSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            audit_log = AuditLog(
                action = validated_data.action,
                entite = validated_data.entite,
                entite_id = validated_data.entite_id,
                ancienne_valeur = validated_data.ancienne_valeur,
                nouvelle_valeur = validated_data.nouvelle_valeur,
                ip_address = validated_data.ip_address,
                
                user_id = current_user.id,
            )

            session.add(audit_log)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': AuditLogSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            audit_log: AuditLog = session.query(AuditLog).filter(
                AuditLog.id == id, AuditLog.deleted_at == None).first()

            if audit_log is None: raise NotFound('audit_log not found')

            audit_log.user_id = validated_data.user_id
            audit_log.action = validated_data.action
            audit_log.entite = validated_data.entite
            audit_log.entite_id = validated_data.entite_id
            audit_log.ancienne_valeur = validated_data.ancienne_valeur
            audit_log.nouvelle_valeur = validated_data.nouvelle_valeur
            audit_log.ip_address = validated_data.ip_address
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': AuditLogSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            audit_log: AuditLog = session.query(AuditLog).filter(
                AuditLog.user_id == current_user.id,
                AuditLog.id == id, 
                AuditLog.deleted_at == None).first()

            if audit_log is None: raise NotFound('audit_log not found')

            audit_log.user_id = validated_data.user_id
            audit_log.action = validated_data.action
            audit_log.entite = validated_data.entite
            audit_log.entite_id = validated_data.entite_id
            audit_log.ancienne_valeur = validated_data.ancienne_valeur
            audit_log.nouvelle_valeur = validated_data.nouvelle_valeur
            audit_log.ip_address = validated_data.ip_address
            
            audit_log.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': AuditLogSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            audit_log:AuditLog = session.query(AuditLog)\
                .filter(AuditLog.deleted_at == None,
                        AuditLog.id == id).first()
            if audit_log is None: raise NotFound('audit_log not found')

            audit_log.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            audit_log:AuditLog = session.query(AuditLog)\
                .filter(AuditLog.user_id == current_user.id,
                        AuditLog.deleted_at == None,
                        AuditLog.id == id).first()

            if audit_log is None: raise NotFound('audit_log not found')

            audit_log.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK