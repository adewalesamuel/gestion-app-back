import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate

from ..user.model import User
from .model import Notification
from .schema import NotificationSchema


class NotificationService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        notification_schema = NotificationSchema(many=True)
        page = request.args.get('page', '')
        notifications = session.query(Notification)\
                .filter(Notification.deleted_at == None)\
                .order_by(Notification.created_at.desc())

        if (page != ''):
            notifications = paginate(notifications, page=page)
            result = notifications
            result['data'] = notification_schema.dump(notifications['data'])
        else:
            result = notification_schema.dump(notifications.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        notification_schema = NotificationSchema(many=True)
        page = request.args.get('page', '')
        notifications = session.query(Notification)\
                .filter(Notification.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(Notification.created_at.desc())

        if (page != ''):
            notifications = paginate(notifications, page=page)
            result = notifications
            result['data'] = notification_schema.dump(notifications['data'])
        else:
            result = notification_schema.dump(notifications.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        notification:Notification = session.query(Notification)\
            .filter(Notification.deleted_at == None,
                    Notification.id == id).first()
        
        if notification is None: raise NotFound('notification not found')

        result = NotificationSchema().dump(notification)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        notification:Notification = session.query(Notification)\
            .filter(User.id == current_user.id,
                    Notification.deleted_at == None,
                    Notification.id == id).first()
        
        if notification is None: raise NotFound('notification not found')

        result = NotificationSchema().dump(notification)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            notification = Notification(
                user_id = validated_data.user_id,
                titre = validated_data.titre,
                message = validated_data.message,
                lu = validated_data.lu,
                type = validated_data.type,
                entite_type = validated_data.entite_type,
                entite_id = validated_data.entite_id,
                
            )

            session.add(notification)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': NotificationSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            notification = Notification(
                titre = validated_data.titre,
                message = validated_data.message,
                lu = validated_data.lu,
                type = validated_data.type,
                entite_type = validated_data.entite_type,
                entite_id = validated_data.entite_id,
                
                user_id = current_user.id,
            )

            session.add(notification)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': NotificationSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            notification: Notification = session.query(Notification).filter(
                Notification.id == id, Notification.deleted_at == None).first()

            if notification is None: raise NotFound('notification not found')

            notification.user_id = validated_data.user_id
            notification.titre = validated_data.titre
            notification.message = validated_data.message
            notification.lu = validated_data.lu
            notification.type = validated_data.type
            notification.entite_type = validated_data.entite_type
            notification.entite_id = validated_data.entite_id
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': NotificationSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            notification: Notification = session.query(Notification).filter(
                User.id == current_user.id,
                Notification.id == id, 
                Notification.deleted_at == None).first()

            if notification is None: raise NotFound('notification not found')

            notification.user_id = validated_data.user_id
            notification.titre = validated_data.titre
            notification.message = validated_data.message
            notification.lu = validated_data.lu
            notification.type = validated_data.type
            notification.entite_type = validated_data.entite_type
            notification.entite_id = validated_data.entite_id
            
            notification.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': NotificationSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            notification:Notification = session.query(Notification)\
                .filter(Notification.deleted_at == None,
                        Notification.id == id).first()
            if notification is None: raise NotFound('notification not found')

            notification.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            notification:Notification = session.query(Notification)\
                .filter(User.deleted_at == current_user.id,
                        Notification.deleted_at == None,
                        Notification.id == id).first()

            if notification is None: raise NotFound('notification not found')

            notification.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK