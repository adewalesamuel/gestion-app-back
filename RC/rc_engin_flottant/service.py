import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import RCEnginFlottant
from .schema import RCEnginFlottantSchema


class RCEnginFlottantService:
    @staticmethod
    def index(current_user: User | None):
        result = []
        rc_engin_flottant_schema = RCEnginFlottantSchema(many=True)
        page = request.args.get('page', '')
        rc_engin_flottants = session.query(RCEnginFlottant)\
                .filter(RCEnginFlottant.deleted_at == None)\
                .order_by(RCEnginFlottant.created_at.desc())

        if (page != ''):
            rc_engin_flottants = paginate(rc_engin_flottants, page=page)
            result = rc_engin_flottants
            result['data'] = rc_engin_flottant_schema.dump(rc_engin_flottants['data'])
        else:
            result = rc_engin_flottant_schema.dump(rc_engin_flottants.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user: User | None, id: int):
        rc_engin_flottant:RCEnginFlottant = session.query(RCEnginFlottant)\
            .filter(RCEnginFlottant.deleted_at == None,
                    RCEnginFlottant.id == id).first()
        
        if rc_engin_flottant is None: raise NotFound('rc_engin_flottant not found')

        result = RCEnginFlottantSchema().dump(rc_engin_flottant)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user: User | None, validated_data):
        try:
            rc_engin_flottant = RCEnginFlottant(
                rc_type_engin_id = validated_data.rc_type_engin_id,
                rc_pays_id = validated_data.rc_pays_id,
                rc_acteur_id = validated_data.rc_acteur_id,
                nom = validated_data.nom,
                immatriculation = validated_data.immatriculation,
                tonnage_brut = validated_data.tonnage_brut,
                longueur = validated_data.longueur,
                annee_construction = validated_data.annee_construction,
                capacite_passagers = validated_data.capacite_passagers,
                capacite_fret = validated_data.capacite_fret,
                
            )

            session.add(rc_engin_flottant)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCEnginFlottantSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user: User | None, id: int, validated_data):
        try:
            rc_engin_flottant: RCEnginFlottant = session.query(RCEnginFlottant).filter(
                RCEnginFlottant.id == id, RCEnginFlottant.deleted_at == None).first()

            if rc_engin_flottant is None: raise NotFound('rc_engin_flottant not found')

            rc_engin_flottant.rc_type_engin_id = validated_data.rc_type_engin_id
            rc_engin_flottant.rc_pays_id = validated_data.rc_pays_id
            rc_engin_flottant.rc_acteur_id = validated_data.rc_acteur_id
            rc_engin_flottant.nom = validated_data.nom
            rc_engin_flottant.immatriculation = validated_data.immatriculation
            rc_engin_flottant.tonnage_brut = validated_data.tonnage_brut
            rc_engin_flottant.longueur = validated_data.longueur
            rc_engin_flottant.annee_construction = validated_data.annee_construction
            rc_engin_flottant.capacite_passagers = validated_data.capacite_passagers
            rc_engin_flottant.capacite_fret = validated_data.capacite_fret
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCEnginFlottantSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def delete(current_user: User | None, id: int):    
        try:
            rc_engin_flottant:RCEnginFlottant = session.query(RCEnginFlottant)\
                .filter(RCEnginFlottant.deleted_at == None,
                        RCEnginFlottant.id == id).first()
            if rc_engin_flottant is None: raise NotFound('rc_engin_flottant not found')

            rc_engin_flottant.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK