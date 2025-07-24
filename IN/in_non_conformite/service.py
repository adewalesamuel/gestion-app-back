import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import INNonConformite
from .schema import INNonConformiteSchema


class INNonConformiteService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        in_non_conformite_schema = INNonConformiteSchema(many=True)
        page = request.args.get('page', '')
        in_non_conformites = session.query(INNonConformite)\
                .filter(INNonConformite.deleted_at == None)\
                .order_by(INNonConformite.created_at.desc())

        if (page != ''):
            in_non_conformites = paginate(in_non_conformites, page=page)
            result = in_non_conformites
            result['data'] = in_non_conformite_schema.dump(in_non_conformites['data'])
        else:
            result = in_non_conformite_schema.dump(in_non_conformites.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        in_non_conformite_schema = INNonConformiteSchema(many=True)
        page = request.args.get('page', '')
        in_non_conformites = session.query(INNonConformite)\
                .filter(INNonConformite.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(INNonConformite.created_at.desc())

        if (page != ''):
            in_non_conformites = paginate(in_non_conformites, page=page)
            result = in_non_conformites
            result['data'] = in_non_conformite_schema.dump(in_non_conformites['data'])
        else:
            result = in_non_conformite_schema.dump(in_non_conformites.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        in_non_conformite:INNonConformite = session.query(INNonConformite)\
            .filter(INNonConformite.deleted_at == None,
                    INNonConformite.id == id).first()
        
        if in_non_conformite is None: raise NotFound('in_non_conformite not found')

        result = INNonConformiteSchema().dump(in_non_conformite)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        in_non_conformite:INNonConformite = session.query(INNonConformite)\
            .filter(User.id == current_user.id,
                    INNonConformite.deleted_at == None,
                    INNonConformite.id == id).first()
        
        if in_non_conformite is None: raise NotFound('in_non_conformite not found')

        result = INNonConformiteSchema().dump(in_non_conformite)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            in_non_conformite = INNonConformite(
                in_inspection_id = validated_data.in_inspection_id,
                user_id = validated_data.user_id,
                description = validated_data.description,
                gravite = validated_data.gravite,
                date_decouverte = validated_data.date_decouverte,
                heure = validated_data.heure,
                date_resolution = validated_data.date_resolution,
                statut = validated_data.statut,
                
            )

            session.add(in_non_conformite)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INNonConformiteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            in_non_conformite = INNonConformite(
                in_inspection_id = validated_data.in_inspection_id,
                description = validated_data.description,
                gravite = validated_data.gravite,
                date_decouverte = validated_data.date_decouverte,
                heure = validated_data.heure,
                date_resolution = validated_data.date_resolution,
                statut = validated_data.statut,
                
                user_id = current_user.id,
            )

            session.add(in_non_conformite)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INNonConformiteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            in_non_conformite: INNonConformite = session.query(INNonConformite).filter(
                INNonConformite.id == id, INNonConformite.deleted_at == None).first()

            if in_non_conformite is None: raise NotFound('in_non_conformite not found')

            in_non_conformite.in_inspection_id = validated_data.in_inspection_id
            in_non_conformite.user_id = validated_data.user_id
            in_non_conformite.description = validated_data.description
            in_non_conformite.gravite = validated_data.gravite
            in_non_conformite.date_decouverte = validated_data.date_decouverte
            in_non_conformite.heure = validated_data.heure
            in_non_conformite.date_resolution = validated_data.date_resolution
            in_non_conformite.statut = validated_data.statut
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INNonConformiteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            in_non_conformite: INNonConformite = session.query(INNonConformite).filter(
                User.id == current_user.id,
                INNonConformite.id == id, 
                INNonConformite.deleted_at == None).first()

            if in_non_conformite is None: raise NotFound('in_non_conformite not found')

            in_non_conformite.in_inspection_id = validated_data.in_inspection_id
            in_non_conformite.user_id = validated_data.user_id
            in_non_conformite.description = validated_data.description
            in_non_conformite.gravite = validated_data.gravite
            in_non_conformite.date_decouverte = validated_data.date_decouverte
            in_non_conformite.heure = validated_data.heure
            in_non_conformite.date_resolution = validated_data.date_resolution
            in_non_conformite.statut = validated_data.statut
            
            in_non_conformite.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INNonConformiteSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            in_non_conformite:INNonConformite = session.query(INNonConformite)\
                .filter(INNonConformite.deleted_at == None,
                        INNonConformite.id == id).first()
            if in_non_conformite is None: raise NotFound('in_non_conformite not found')

            in_non_conformite.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            in_non_conformite:INNonConformite = session.query(INNonConformite)\
                .filter(User.deleted_at == current_user.id,
                        INNonConformite.deleted_at == None,
                        INNonConformite.id == id).first()

            if in_non_conformite is None: raise NotFound('in_non_conformite not found')

            in_non_conformite.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK