import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ...admin.model import Admin
from ...common_features.user.model import User
from .model import GUCommentaire
from .schema import GUCommentaireSchema


class GUCommentaireService:
    @staticmethod
    def index(current_user:User | None):
        result = []
        gu_commentaire_schema = GUCommentaireSchema(many=True)
        page = request.args.get('page', '')
        gu_commentaires = session.query(GUCommentaire)\
                .filter(GUCommentaire.deleted_at == None)\
                .order_by(GUCommentaire.created_at.desc())

        if (page != ''):
            gu_commentaires = paginate(gu_commentaires, page=page)
            result = gu_commentaires
            result['data'] = gu_commentaire_schema.dump(gu_commentaires['data'])
        else:
            result = gu_commentaire_schema.dump(gu_commentaires.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_index(current_user:User | None):
        result = []
        gu_commentaire_schema = GUCommentaireSchema(many=True)
        page = request.args.get('page', '')
        gu_commentaires = session.query(GUCommentaire)\
                .filter(GUCommentaire.deleted_at == None,
                        User.id == current_user.id)\
                .order_by(GUCommentaire.created_at.desc())

        if (page != ''):
            gu_commentaires = paginate(gu_commentaires, page=page)
            result = gu_commentaires
            result['data'] = gu_commentaire_schema.dump(gu_commentaires['data'])
        else:
            result = gu_commentaire_schema.dump(gu_commentaires.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user:User | None, id: int):
        gu_commentaire:GUCommentaire = session.query(GUCommentaire)\
            .filter(GUCommentaire.deleted_at == None,
                    GUCommentaire.id == id).first()
        
        if gu_commentaire is None: raise NotFound('gu_commentaire not found')

        result = GUCommentaireSchema().dump(gu_commentaire)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK
    @staticmethod
        
    def user_show(current_user:User | None, id: int):
        gu_commentaire:GUCommentaire = session.query(GUCommentaire)\
            .filter(User.id == current_user.id,
                    GUCommentaire.deleted_at == None,
                    GUCommentaire.id == id).first()
        
        if gu_commentaire is None: raise NotFound('gu_commentaire not found')

        result = GUCommentaireSchema().dump(gu_commentaire)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user:User | None, validated_data):
        try:
            gu_commentaire = GUCommentaire(
                contenu = validated_data.contenu,
                date = validated_data.date,
                heure = validated_data.heure,
                user_id = validated_data.user_id,
                gu_demande_id = validated_data.gu_demande_id,
                
            )

            session.add(gu_commentaire)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUCommentaireSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def user_store(current_user:User | None, validated_data):
        try:
            gu_commentaire = GUCommentaire(
                contenu = validated_data.contenu,
                date = validated_data.date,
                heure = validated_data.heure,
                gu_demande_id = validated_data.gu_demande_id,
                
                user_id = current_user.id,
            )

            session.add(gu_commentaire)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUCommentaireSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user:User | None, id: int, validated_data):
        try:
            gu_commentaire: GUCommentaire = session.query(GUCommentaire).filter(
                GUCommentaire.id == id, GUCommentaire.deleted_at == None).first()

            if gu_commentaire is None: raise NotFound('gu_commentaire not found')

            gu_commentaire.contenu = validated_data.contenu
            gu_commentaire.date = validated_data.date
            gu_commentaire.heure = validated_data.heure
            gu_commentaire.user_id = validated_data.user_id
            gu_commentaire.gu_demande_id = validated_data.gu_demande_id
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUCommentaireSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def user_update(current_user:User | None, id: int, validated_data):
        try:
            gu_commentaire: GUCommentaire = session.query(GUCommentaire).filter(
                User.id == current_user.id,
                GUCommentaire.id == id, 
                GUCommentaire.deleted_at == None).first()

            if gu_commentaire is None: raise NotFound('gu_commentaire not found')

            gu_commentaire.contenu = validated_data.contenu
            gu_commentaire.date = validated_data.date
            gu_commentaire.heure = validated_data.heure
            gu_commentaire.user_id = validated_data.user_id
            gu_commentaire.gu_demande_id = validated_data.gu_demande_id
            
            gu_commentaire.user_id = current_user.id

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': GUCommentaireSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK
    

    @staticmethod    
    def delete(current_user:User | None, id: int):    
        try:
            gu_commentaire:GUCommentaire = session.query(GUCommentaire)\
                .filter(GUCommentaire.deleted_at == None,
                        GUCommentaire.id == id).first()
            if gu_commentaire is None: raise NotFound('gu_commentaire not found')

            gu_commentaire.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK

    @staticmethod    
    def user_delete(current_user:User | None, id: int):    
        try:
            gu_commentaire:GUCommentaire = session.query(GUCommentaire)\
                .filter(User.deleted_at == current_user.id,
                        GUCommentaire.deleted_at == None,
                        GUCommentaire.id == id).first()

            if gu_commentaire is None: raise NotFound('gu_commentaire not found')

            gu_commentaire.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK