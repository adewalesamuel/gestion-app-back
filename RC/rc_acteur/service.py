import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import RCActeur
from .schema import RCActeurSchema


class RCActeurService:
    @staticmethod
    def index(current_user: User | None):
        result = []
        rc_acteur_schema = RCActeurSchema(many=True)
        page = request.args.get('page', '')
        rc_acteurs = session.query(RCActeur)\
                .filter(RCActeur.deleted_at == None)\
                .order_by(RCActeur.created_at.desc())

        if (page != ''):
            rc_acteurs = paginate(rc_acteurs, page=page)
            result = rc_acteurs
            result['data'] = rc_acteur_schema.dump(rc_acteurs['data'])
        else:
            result = rc_acteur_schema.dump(rc_acteurs.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user: User | None, id: int):
        rc_acteur:RCActeur = session.query(RCActeur)\
            .filter(RCActeur.deleted_at == None,
                    RCActeur.id == id).first()
        
        if rc_acteur is None: raise NotFound('rc_acteur not found')

        result = RCActeurSchema().dump(rc_acteur)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user: User | None, validated_data):
        try:
            rc_acteur = RCActeur(
                type = validated_data.type,
                nom = validated_data.nom,
                prenom = validated_data.prenom,
                raison_sociale = validated_data.raison_sociale,
                registre_commerce = validated_data.registre_commerce,
                email = validated_data.email,
                adresse = validated_data.adresse,
                telephone = validated_data.telephone,
                secteur_activite = validated_data.secteur_activite,
                pays_origine = validated_data.pays_origine,
                
            )

            session.add(rc_acteur)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCActeurSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user: User | None, id: int, validated_data):
        try:
            rc_acteur: RCActeur = session.query(RCActeur).filter(
                RCActeur.id == id, RCActeur.deleted_at == None).first()

            if rc_acteur is None: raise NotFound('rc_acteur not found')

            rc_acteur.type = validated_data.type
            rc_acteur.nom = validated_data.nom
            rc_acteur.prenom = validated_data.prenom
            rc_acteur.raison_sociale = validated_data.raison_sociale
            rc_acteur.registre_commerce = validated_data.registre_commerce
            rc_acteur.email = validated_data.email
            rc_acteur.adresse = validated_data.adresse
            rc_acteur.telephone = validated_data.telephone
            rc_acteur.secteur_activite = validated_data.secteur_activite
            rc_acteur.pays_origine = validated_data.pays_origine
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCActeurSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def delete(current_user: User | None, id: int):    
        try:
            rc_acteur:RCActeur = session.query(RCActeur)\
                .filter(RCActeur.deleted_at == None,
                        RCActeur.id == id).first()
            if rc_acteur is None: raise NotFound('rc_acteur not found')

            rc_acteur.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK