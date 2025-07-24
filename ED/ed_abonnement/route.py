from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.exceptions import UnprocessableEntity
from ... import config
from ...db import session
from ...decorators import user_required
from .schema import EDAbonnementSchema
from .service import EDAbonnementService

route = Blueprint(
    'ed_abonnement', 
    __name__, 
    url_prefix = config.app.get('API_PREFIX')
)
ENDPOINT = '/ed-abonnements'

@route.get(f'{ENDPOINT}')
@user_required
def index(current_user): 
    return EDAbonnementService.index(current_user)

@route.post(f'{ENDPOINT}')
@user_required
def store(current_user): 
    try:
        validated_data = EDAbonnementSchema().load(
            request.json, session=session
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return EDAbonnementService.store(current_user, validated_data)

@route.get(f'{ENDPOINT}/<int:id>')
@user_required
def show(current_user, id): 
    return EDAbonnementService.show(current_user, id)

@route.put(f'{ENDPOINT}/<int:id>')
@user_required
def update(current_user, id):
    try:
        validated_data = EDAbonnementSchema().load(
            request.json, 
            session=session,
            partial=True
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return EDAbonnementService.update(current_user, id, validated_data)

@route.delete(f'{ENDPOINT}/<int:id>')
@user_required
def delete(current_user, id): 
    return EDAbonnementService.delete(current_user, id)