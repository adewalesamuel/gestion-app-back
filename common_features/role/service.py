import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate

from ..user.model import User
from .model import Role
from .schema import RoleSchema


class RoleService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        role_schema = RoleSchema(many=True)
        page = request.args.get('page', '')
        roles = session.query(Role)\
                .filter(Role.deleted_at == None)\
                .order_by(Role.created_at.desc())

        if (page != ''):
            roles = paginate(roles, page=page)
            result = roles
            result['data'] = role_schema.dump(roles['data'])
        else:
            result = role_schema.dump(roles.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        role:Role = session.query(Role)\
            .filter(Role.deleted_at == None,
                    Role.id == id).first()
        
        if role is None: raise NotFound('role not found')

        result = RoleSchema().dump(role)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            role = Role(
                name = validated_data.name,
                description = validated_data.description,
                permissions = validated_data.permissions,
                
            )

            session.add(role)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RoleSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            role: Role = session.query(Role).filter(
                Role.id == id, Role.deleted_at == None).first()

            if role is None: raise NotFound('role not found')

            role.name = validated_data.name
            role.description = validated_data.description
            role.permissions = validated_data.permissions
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RoleSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            role:Role = session.query(Role)\
                .filter(Role.deleted_at == None,
                        Role.id == id).first()
            if role is None: raise NotFound('role not found')

            role.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK