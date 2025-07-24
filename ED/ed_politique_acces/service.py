import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import EDPolitiqueAcces
from .schema import EDPolitiqueAccesSchema


class EDPolitiqueAccesService:
    @staticmethod
    def index(current_user: User | None):
        result = []
        ed_politique_acces_schema = EDPolitiqueAccesSchema(many=True)
        page = request.args.get('page', '')
        ed_politique_access = session.query(EDPolitiqueAcces)\
                .filter(EDPolitiqueAcces.deleted_at == None)\
                .order_by(EDPolitiqueAcces.created_at.desc())

        if (page != ''):
            ed_politique_access = paginate(ed_politique_access, page=page)
            result = ed_politique_access
            result['data'] = ed_politique_acces_schema.dump(ed_politique_access['data'])
        else:
            result = ed_politique_acces_schema.dump(ed_politique_access.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user: User | None, id: int):
        ed_politique_acces:EDPolitiqueAcces = session.query(EDPolitiqueAcces)\
            .filter(EDPolitiqueAcces.deleted_at == None,
                    EDPolitiqueAcces.id == id).first()
        
        if ed_politique_acces is None: raise NotFound('ed_politique_acces not found')

        result = EDPolitiqueAccesSchema().dump(ed_politique_acces)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user: User | None, validated_data):
        try:
            ed_politique_acces = EDPolitiqueAcces(
                ed_api_id = validated_data.ed_api_id,
                role_id = validated_data.role_id,
                nom = validated_data.nom,
                regles = validated_data.regles,
                
            )

            session.add(ed_politique_acces)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDPolitiqueAccesSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user: User | None, id: int, validated_data):
        try:
            ed_politique_acces: EDPolitiqueAcces = session.query(EDPolitiqueAcces).filter(
                EDPolitiqueAcces.id == id, EDPolitiqueAcces.deleted_at == None).first()

            if ed_politique_acces is None: raise NotFound('ed_politique_acces not found')

            ed_politique_acces.ed_api_id = validated_data.ed_api_id
            ed_politique_acces.role_id = validated_data.role_id
            ed_politique_acces.nom = validated_data.nom
            ed_politique_acces.regles = validated_data.regles
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': EDPolitiqueAccesSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def delete(current_user: User | None, id: int):    
        try:
            ed_politique_acces:EDPolitiqueAcces = session.query(EDPolitiqueAcces)\
                .filter(EDPolitiqueAcces.deleted_at == None,
                        EDPolitiqueAcces.id == id).first()
            if ed_politique_acces is None: raise NotFound('ed_politique_acces not found')

            ed_politique_acces.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK