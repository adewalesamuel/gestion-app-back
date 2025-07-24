from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.exceptions import UnprocessableEntity
from ... import config
from ...db import session
from ...decorators import user_required
from .schema import REModePaiementSchema
from .service import REModePaiementService

route = Blueprint(
    're_mode_paiement', 
    __name__, 
    url_prefix = config.app.get('API_PREFIX')
)
ENDPOINT = '/re-mode-paiements'

@route.get(f'{ENDPOINT}')
@user_required
def index(current_user): 
    return REModePaiementService.index(current_user)

@route.post(f'{ENDPOINT}')
@user_required
def store(current_user): 
    try:
        validated_data = REModePaiementSchema().load(
            request.json, session=session
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return REModePaiementService.store(current_user, validated_data)

@route.get(f'{ENDPOINT}/<int:id>')
@user_required
def show(current_user, id): 
    return REModePaiementService.show(current_user, id)

@route.put(f'{ENDPOINT}/<int:id>')
@user_required
def update(current_user, id):
    try:
        validated_data = REModePaiementSchema().load(
            request.json, 
            session=session,
            partial=True
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return REModePaiementService.update(current_user, id, validated_data)

@route.delete(f'{ENDPOINT}/<int:id>')
@user_required
def delete(current_user, id): 
    return REModePaiementService.delete(current_user, id)