import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
from ...libs import crypto

from ..user.model import User
from .model import User
from .schema import UserSchema


class UserService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        user_schema = UserSchema(many=True)
        page = request.args.get('page', '')
        users = session.query(User)\
                .filter(User.deleted_at == None)\
                .order_by(User.created_at.desc())

        if (page != ''):
            users = paginate(users, page=page)
            result = users
            result['data'] = user_schema.dump(users['data'])
        else:
            result = user_schema.dump(users.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        user:User = session.query(User)\
            .filter(User.deleted_at == None,
                    User.id == id).first()
        
        if user is None: raise NotFound('user not found')

        result = UserSchema().dump(user)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            user = User(
                role_id = validated_data.role_id,
                rc_acteur_id = validated_data.rc_acteur_id,
                profil_img_url = validated_data.profil_img_url,
                nom = validated_data.nom,
                email = validated_data.email,
                password = crypto.hash_password(validated_data.password),
                last_login_date = validated_data.last_login_date,
                last_login_heure = validated_data.last_login_heure,
                
            )

            session.add(user)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': UserSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            user: User = session.query(User).filter(
                User.id == id, User.deleted_at == None).first()

            if user is None: raise NotFound('user not found')

            user.role_id = validated_data.role_id
            user.rc_acteur_id = validated_data.rc_acteur_id
            user.profil_img_url = validated_data.profil_img_url
            user.nom = validated_data.nom
            user.email = validated_data.email
            user.password = validated_data.password
            user.last_login_date = validated_data.last_login_date
            user.last_login_heure = validated_data.last_login_heure
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': UserSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            user:User = session.query(User)\
                .filter(User.deleted_at == None,
                        User.id == id).first()
            if user is None: raise NotFound('user not found')

            user.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK