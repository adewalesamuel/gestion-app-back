import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate

from ..user.model import User
from .model import ConfigSysteme
from .schema import ConfigSystemeSchema


class ConfigSystemeService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        config_systeme_schema = ConfigSystemeSchema(many=True)
        page = request.args.get('page', '')
        config_systemes = session.query(ConfigSysteme)\
                .filter(ConfigSysteme.deleted_at == None)\
                .order_by(ConfigSysteme.created_at.desc())

        if (page != ''):
            config_systemes = paginate(config_systemes, page=page)
            result = config_systemes
            result['data'] = config_systeme_schema.dump(config_systemes['data'])
        else:
            result = config_systeme_schema.dump(config_systemes.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        config_systeme_schema = ConfigSystemeSchema(many=True)
        page = request.args.get('page', '')
        config_systemes = session.query(ConfigSysteme)\
                .filter(ConfigSysteme.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(ConfigSysteme.created_at.desc())

        if (page != ''):
            config_systemes = paginate(config_systemes, page=page)
            result = config_systemes
            result['data'] = config_systeme_schema.dump(config_systemes['data'])
        else:
            result = config_systeme_schema.dump(config_systemes.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        config_systeme:ConfigSysteme = session.query(ConfigSysteme)\
            .filter(ConfigSysteme.deleted_at == None,
                    ConfigSysteme.id == id).first()
        
        if config_systeme is None: raise NotFound('config_systeme not found')

        result = ConfigSystemeSchema().dump(config_systeme)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        config_systeme:ConfigSysteme = session.query(ConfigSysteme)\
            .filter(User.id == current_user.id,
                    ConfigSysteme.deleted_at == None,
                    ConfigSysteme.id == id).first()
        
        if config_systeme is None: raise NotFound('config_systeme not found')

        result = ConfigSystemeSchema().dump(config_systeme)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            config_systeme = ConfigSysteme(
                parametre = validated_data.parametre,
                valeur = validated_data.valeur,
                module = validated_data.module,
                editable = validated_data.editable,
                
            )

            session.add(config_systeme)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': ConfigSystemeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            config_systeme = ConfigSysteme(
                parametre = validated_data.parametre,
                valeur = validated_data.valeur,
                module = validated_data.module,
                editable = validated_data.editable,
                
                user_id = current_user.id,
            )

            session.add(config_systeme)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': ConfigSystemeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            config_systeme: ConfigSysteme = session.query(ConfigSysteme).filter(
                ConfigSysteme.id == id, ConfigSysteme.deleted_at == None).first()

            if config_systeme is None: raise NotFound('config_systeme not found')

            config_systeme.parametre = validated_data.parametre
            config_systeme.valeur = validated_data.valeur
            config_systeme.module = validated_data.module
            config_systeme.editable = validated_data.editable
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': ConfigSystemeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            config_systeme: ConfigSysteme = session.query(ConfigSysteme).filter(
                User.id == current_user.id,
                ConfigSysteme.id == id, 
                ConfigSysteme.deleted_at == None).first()

            if config_systeme is None: raise NotFound('config_systeme not found')

            config_systeme.parametre = validated_data.parametre
            config_systeme.valeur = validated_data.valeur
            config_systeme.module = validated_data.module
            config_systeme.editable = validated_data.editable
            
            config_systeme.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': ConfigSystemeSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            config_systeme:ConfigSysteme = session.query(ConfigSysteme)\
                .filter(ConfigSysteme.deleted_at == None,
                        ConfigSysteme.id == id).first()
            if config_systeme is None: raise NotFound('config_systeme not found')

            config_systeme.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            config_systeme:ConfigSysteme = session.query(ConfigSysteme)\
                .filter(User.deleted_at == current_user.id,
                        ConfigSysteme.deleted_at == None,
                        ConfigSysteme.id == id).first()

            if config_systeme is None: raise NotFound('config_systeme not found')

            config_systeme.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK