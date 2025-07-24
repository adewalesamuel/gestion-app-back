from flask import jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...libs import jwt, crypto
from ..user.model import User
from ..user.schema import UserSchema


class AuthService:
    @staticmethod
    def register(validated_data: User):
        try:
            user = User(
                nom = validated_data.nom,
                email = validated_data.email,
                password = validated_data.password
            )

            session.add(user)
            session.commit()
            session.refresh(user)
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))

        response_data = {
            'success': True,
            'data': UserSchema().dump(user),
            'token': jwt.make_token(user)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def login(validated_data):
        user: User = session.query(User).filter(
            User.email == validated_data['email'],
            User.deleted_at == None
        ).first()
        
        if (user is None or crypto.is_password(
                validated_data['password'], 
                user.password) is False): 
            raise NotFound('incorrect email or password')

        response_data = {
            'success': True,
            'data': UserSchema().dump(user),
            'token': jwt.make_token(user)
        }

        return jsonify(response_data), HTTPStatus.OK

    # @staticmethod
    # def admin_login(validated_data):
    #     print(validated_data)
    #     user: Admin = session.query(Admin).filter(
    #         Admin.email == validated_data['email'],
    #         Admin.deleted_at == None
    #     ).first()
        
    #     if (user is None or crypto.is_password(
    #             validated_data['password'], 
    #             user.password) is False): 
    #         raise NotFound('incorrect email or password')

    #     response_data = {
    #         'success': True,
    #         'data': AdminSchema().dump(user),
    #         'token': jwt.make_token(user, 'admin')
    #     }

    #     return jsonify(response_data), HTTPStatus.OK