from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.exceptions import UnprocessableEntity
from ... import config
from ...db import session
from ...decorators import user_required
from .schema import INNonConformiteSchema
from .service import INNonConformiteService

route = Blueprint(
    'in_non_conformite', 
    __name__, 
    url_prefix = config.app.get('API_PREFIX')
)
ENDPOINT = '/in-non-conformites'

@route.get(f'{ENDPOINT}')
@user_required
def index(current_user): 
    return INNonConformiteService.index(current_user)

@route.post(f'{ENDPOINT}')
@user_required
def store(current_user): 
    try:
        validated_data = INNonConformiteSchema().load(
            request.json, session=session
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return INNonConformiteService.store(current_user, validated_data)

@route.get(f'{ENDPOINT}/<int:id>')
@user_required
def show(current_user, id): 
    return INNonConformiteService.show(current_user, id)

@route.put(f'{ENDPOINT}/<int:id>')
@user_required
def update(current_user, id):
    try:
        validated_data = INNonConformiteSchema().load(
            request.json, 
            session=session,
            partial=True
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return INNonConformiteService.update(current_user, id, validated_data)

@route.delete(f'{ENDPOINT}/<int:id>')
@user_required
def delete(current_user, id): 
    return INNonConformiteService.delete(current_user, id)