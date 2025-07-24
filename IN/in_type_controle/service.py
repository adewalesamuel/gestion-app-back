import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import INTypeControle
from .schema import INTypeControleSchema


class INTypeControleService:
    @staticmethod
    def index(current_user: User | None):
        result = []
        in_type_controle_schema = INTypeControleSchema(many=True)
        page = request.args.get('page', '')
        in_type_controles = session.query(INTypeControle)\
                .filter(INTypeControle.deleted_at == None)\
                .order_by(INTypeControle.created_at.desc())

        if (page != ''):
            in_type_controles = paginate(in_type_controles, page=page)
            result = in_type_controles
            result['data'] = in_type_controle_schema.dump(in_type_controles['data'])
        else:
            result = in_type_controle_schema.dump(in_type_controles.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user: User | None, id: int):
        in_type_controle:INTypeControle = session.query(INTypeControle)\
            .filter(INTypeControle.deleted_at == None,
                    INTypeControle.id == id).first()
        
        if in_type_controle is None: raise NotFound('in_type_controle not found')

        result = INTypeControleSchema().dump(in_type_controle)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user: User | None, validated_data):
        try:
            in_type_controle = INTypeControle(
                code = validated_data.code,
                libelle = validated_data.libelle,
                norme_reference = validated_data.norme_reference,
                frequence_mois = validated_data.frequence_mois,
                gravite_min = validated_data.gravite_min,
                
            )

            session.add(in_type_controle)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INTypeControleSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user: User | None, id: int, validated_data):
        try:
            in_type_controle: INTypeControle = session.query(INTypeControle).filter(
                INTypeControle.id == id, INTypeControle.deleted_at == None).first()

            if in_type_controle is None: raise NotFound('in_type_controle not found')

            in_type_controle.code = validated_data.code
            in_type_controle.libelle = validated_data.libelle
            in_type_controle.norme_reference = validated_data.norme_reference
            in_type_controle.frequence_mois = validated_data.frequence_mois
            in_type_controle.gravite_min = validated_data.gravite_min
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INTypeControleSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def delete(current_user: User | None, id: int):    
        try:
            in_type_controle:INTypeControle = session.query(INTypeControle)\
                .filter(INTypeControle.deleted_at == None,
                        INTypeControle.id == id).first()
            if in_type_controle is None: raise NotFound('in_type_controle not found')

            in_type_controle.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK