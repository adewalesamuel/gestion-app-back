import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import INResultatItem
from .schema import INResultatItemSchema


class INResultatItemService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        in_resultat_item_schema = INResultatItemSchema(many=True)
        page = request.args.get('page', '')
        in_resultat_items = session.query(INResultatItem)\
                .filter(INResultatItem.deleted_at == None)\
                .order_by(INResultatItem.created_at.desc())

        if (page != ''):
            in_resultat_items = paginate(in_resultat_items, page=page)
            result = in_resultat_items
            result['data'] = in_resultat_item_schema.dump(in_resultat_items['data'])
        else:
            result = in_resultat_item_schema.dump(in_resultat_items.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        in_resultat_item_schema = INResultatItemSchema(many=True)
        page = request.args.get('page', '')
        in_resultat_items = session.query(INResultatItem)\
                .filter(INResultatItem.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(INResultatItem.created_at.desc())

        if (page != ''):
            in_resultat_items = paginate(in_resultat_items, page=page)
            result = in_resultat_items
            result['data'] = in_resultat_item_schema.dump(in_resultat_items['data'])
        else:
            result = in_resultat_item_schema.dump(in_resultat_items.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        in_resultat_item:INResultatItem = session.query(INResultatItem)\
            .filter(INResultatItem.deleted_at == None,
                    INResultatItem.id == id).first()
        
        if in_resultat_item is None: raise NotFound('in_resultat_item not found')

        result = INResultatItemSchema().dump(in_resultat_item)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        in_resultat_item:INResultatItem = session.query(INResultatItem)\
            .filter(User.id == current_user.id,
                    INResultatItem.deleted_at == None,
                    INResultatItem.id == id).first()
        
        if in_resultat_item is None: raise NotFound('in_resultat_item not found')

        result = INResultatItemSchema().dump(in_resultat_item)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            in_resultat_item = INResultatItem(
                in_inspection_id = validated_data.in_inspection_id,
                conforme = validated_data.conforme,
                observations = validated_data.observations,
                checklist_item_code = validated_data.checklist_item_code,
                photo_url = validated_data.photo_url,
                
            )

            session.add(in_resultat_item)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INResultatItemSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            in_resultat_item = INResultatItem(
                in_inspection_id = validated_data.in_inspection_id,
                conforme = validated_data.conforme,
                observations = validated_data.observations,
                checklist_item_code = validated_data.checklist_item_code,
                photo_url = validated_data.photo_url,
                
                user_id = current_user.id,
            )

            session.add(in_resultat_item)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INResultatItemSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            in_resultat_item: INResultatItem = session.query(INResultatItem).filter(
                INResultatItem.id == id, INResultatItem.deleted_at == None).first()

            if in_resultat_item is None: raise NotFound('in_resultat_item not found')

            in_resultat_item.in_inspection_id = validated_data.in_inspection_id
            in_resultat_item.conforme = validated_data.conforme
            in_resultat_item.observations = validated_data.observations
            in_resultat_item.checklist_item_code = validated_data.checklist_item_code
            in_resultat_item.photo_url = validated_data.photo_url
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INResultatItemSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            in_resultat_item: INResultatItem = session.query(INResultatItem).filter(
                User.id == current_user.id,
                INResultatItem.id == id, 
                INResultatItem.deleted_at == None).first()

            if in_resultat_item is None: raise NotFound('in_resultat_item not found')

            in_resultat_item.in_inspection_id = validated_data.in_inspection_id
            in_resultat_item.conforme = validated_data.conforme
            in_resultat_item.observations = validated_data.observations
            in_resultat_item.checklist_item_code = validated_data.checklist_item_code
            in_resultat_item.photo_url = validated_data.photo_url
            
            in_resultat_item.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INResultatItemSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            in_resultat_item:INResultatItem = session.query(INResultatItem)\
                .filter(INResultatItem.deleted_at == None,
                        INResultatItem.id == id).first()
            if in_resultat_item is None: raise NotFound('in_resultat_item not found')

            in_resultat_item.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            in_resultat_item:INResultatItem = session.query(INResultatItem)\
                .filter(User.deleted_at == current_user.id,
                        INResultatItem.deleted_at == None,
                        INResultatItem.id == id).first()

            if in_resultat_item is None: raise NotFound('in_resultat_item not found')

            in_resultat_item.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK