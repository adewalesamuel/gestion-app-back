import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import EDApi
from .schema import EDApiSchema


class EDApiService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        ed_api_schema = EDApiSchema(many=True)
        page = request.args.get('page', '')
        ed_apis = session.query(EDApi)\
                .filter(EDApi.deleted_at == None)\
                .order_by(EDApi.created_at.desc())

        if (page != ''):
            ed_apis = paginate(ed_apis, page=page)
            result = ed_apis
            result['data'] = ed_api_schema.dump(ed_apis['data'])
        else:
            result = ed_api_schema.dump(ed_apis.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        ed_api_schema = EDApiSchema(many=True)
        page = request.args.get('page', '')
        ed_apis = session.query(EDApi)\
                .filter(EDApi.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(EDApi.created_at.desc())

        if (page != ''):
            ed_apis = paginate(ed_apis, page=page)
            result = ed_apis
            result['data'] = ed_api_schema.dump(ed_apis['data'])
        else:
            result = ed_api_schema.dump(ed_apis.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        ed_api:EDApi = session.query(EDApi)\
            .filter(EDApi.deleted_at == None,
                    EDApi.id == id).first()
        
        if ed_api is None: raise NotFound('ed_api not found')

        result = EDApiSchema().dump(ed_api)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        ed_api:EDApi = session.query(EDApi)\
            .filter(User.id == current_user.id,
                    EDApi.deleted_at == None,
                    EDApi.id == id).first()
        
        if ed_api is None: raise NotFound('ed_api not found')

        result = EDApiSchema().dump(ed_api)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            ed_api = EDApi(
                nom = validated_data.nom,
                description = validated_data.description,
                url_base = validated_data.url_base,
                statut = validated_data.statut,
                documentation_url = validated_data.documentation_url,
                
            )

            session.add(ed_api)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDApiSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            ed_api = EDApi(
                nom = validated_data.nom,
                description = validated_data.description,
                url_base = validated_data.url_base,
                statut = validated_data.statut,
                documentation_url = validated_data.documentation_url,
                
                user_id = current_user.id,
            )

            session.add(ed_api)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDApiSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            ed_api: EDApi = session.query(EDApi).filter(
                EDApi.id == id, EDApi.deleted_at == None).first()

            if ed_api is None: raise NotFound('ed_api not found')

            ed_api.nom = validated_data.nom
            ed_api.description = validated_data.description
            ed_api.url_base = validated_data.url_base
            ed_api.statut = validated_data.statut
            ed_api.documentation_url = validated_data.documentation_url
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDApiSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            ed_api: EDApi = session.query(EDApi).filter(
                User.id == current_user.id,
                EDApi.id == id, 
                EDApi.deleted_at == None).first()

            if ed_api is None: raise NotFound('ed_api not found')

            ed_api.nom = validated_data.nom
            ed_api.description = validated_data.description
            ed_api.url_base = validated_data.url_base
            ed_api.statut = validated_data.statut
            ed_api.documentation_url = validated_data.documentation_url
            
            ed_api.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDApiSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            ed_api:EDApi = session.query(EDApi)\
                .filter(EDApi.deleted_at == None,
                        EDApi.id == id).first()
            if ed_api is None: raise NotFound('ed_api not found')

            ed_api.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            ed_api:EDApi = session.query(EDApi)\
                .filter(User.deleted_at == current_user.id,
                        EDApi.deleted_at == None,
                        EDApi.id == id).first()

            if ed_api is None: raise NotFound('ed_api not found')

            ed_api.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK