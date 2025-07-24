import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import INPlanification
from .schema import INPlanificationSchema


class INPlanificationService:
    @staticmethod
    def index(current_user: User | None):
        result = []
        in_planification_schema = INPlanificationSchema(many=True)
        page = request.args.get('page', '')
        in_planifications = session.query(INPlanification)\
                .filter(INPlanification.deleted_at == None)\
                .order_by(INPlanification.created_at.desc())

        if (page != ''):
            in_planifications = paginate(in_planifications, page=page)
            result = in_planifications
            result['data'] = in_planification_schema.dump(in_planifications['data'])
        else:
            result = in_planification_schema.dump(in_planifications.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user: User | None, id: int):
        in_planification:INPlanification = session.query(INPlanification)\
            .filter(INPlanification.deleted_at == None,
                    INPlanification.id == id).first()
        
        if in_planification is None: raise NotFound('in_planification not found')

        result = INPlanificationSchema().dump(in_planification)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user: User | None, validated_data):
        try:
            in_planification = INPlanification(
                rc_engin_flottant_id = validated_data.rc_engin_flottant_id,
                in_checklist_id = validated_data.in_checklist_id,
                periodicite_jours = validated_data.periodicite_jours,
                prochaine_date = validated_data.prochaine_date,
                
            )

            session.add(in_planification)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INPlanificationSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user: User | None, id: int, validated_data):
        try:
            in_planification: INPlanification = session.query(INPlanification).filter(
                INPlanification.id == id, INPlanification.deleted_at == None).first()

            if in_planification is None: raise NotFound('in_planification not found')

            in_planification.rc_engin_flottant_id = validated_data.rc_engin_flottant_id
            in_planification.in_checklist_id = validated_data.in_checklist_id
            in_planification.periodicite_jours = validated_data.periodicite_jours
            in_planification.prochaine_date = validated_data.prochaine_date
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': INPlanificationSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def delete(current_user: User | None, id: int):    
        try:
            in_planification:INPlanification = session.query(INPlanification)\
                .filter(INPlanification.deleted_at == None,
                        INPlanification.id == id).first()
            if in_planification is None: raise NotFound('in_planification not found')

            in_planification.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK