import datetime
from flask import abort, request, jsonify
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest
from ...db import session
from ...utils import paginate
#from ..admin.model import Admin
from ...common_features.user.model import User
from .model import RCPort
from .schema import RCPortSchema


class RCPortService:
    @staticmethod
    def index(current_user: User | None):
        result = []
        rc_port_schema = RCPortSchema(many=True)
        page = request.args.get('page', '')
        rc_ports = session.query(RCPort)\
                .filter(RCPort.deleted_at == None)\
                .order_by(RCPort.created_at.desc())

        if (page != ''):
            rc_ports = paginate(rc_ports, page=page)
            result = rc_ports
            result['data'] = rc_port_schema.dump(rc_ports['data'])
        else:
            result = rc_port_schema.dump(rc_ports.all())

        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def show(current_user: User | None, id: int):
        rc_port:RCPort = session.query(RCPort)\
            .filter(RCPort.deleted_at == None,
                    RCPort.id == id).first()
        
        if rc_port is None: raise NotFound('rc_port not found')

        result = RCPortSchema().dump(rc_port)
        response_data = {
            'success': True,
            'data': result
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def store(current_user: User | None, validated_data):
        try:
            rc_port = RCPort(
                rc_pays_id = validated_data.rc_pays_id,
                nom = validated_data.nom,
                code = validated_data.code,
                capacite_accueil = validated_data.capacite_accueil,
                profondeur_max = validated_data.profondeur_max,
                
            )

            session.add(rc_port)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCPortSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK

    @staticmethod
    def update(current_user: User | None, id: int, validated_data):
        try:
            rc_port: RCPort = session.query(RCPort).filter(
                RCPort.id == id, RCPort.deleted_at == None).first()

            if rc_port is None: raise NotFound('rc_port not found')

            rc_port.rc_pays_id = validated_data.rc_pays_id
            rc_port.nom = validated_data.nom
            rc_port.code = validated_data.code
            rc_port.capacite_accueil = validated_data.capacite_accueil
            rc_port.profondeur_max = validated_data.profondeur_max
            

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        response_data = {
            'success': True,
            'data': RCPortSchema().dump(validated_data)
        }

        return jsonify(response_data), HTTPStatus.OK 

    @staticmethod    
    def delete(current_user: User | None, id: int):    
        try:
            rc_port:RCPort = session.query(RCPort)\
                .filter(RCPort.deleted_at == None,
                        RCPort.id == id).first()
            if rc_port is None: raise NotFound('rc_port not found')

            rc_port.deleted_at = datetime.datetime.now(datetime.timezone.utc)

            session.commit()
        except Exception as e:
            session.rollback()
            raise BadRequest(str(e))
        
        return jsonify(succss=True), HTTPStatus.OK