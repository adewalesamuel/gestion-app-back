from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.exceptions import UnprocessableEntity
from ... import config
from ...db import session
from ...decorators import user_required
from .schema import RCActeurSchema
from .service import RCActeurService

route = Blueprint(
    'rc_acteur', 
    __name__, 
    url_prefix = config.app.get('API_PREFIX')
)
ENDPOINT = '/rc-acteurs'

@route.get(f'{ENDPOINT}')
# @user_required
def index(current_user=None): 
    return RCActeurService.index(current_user)

@route.post(f'{ENDPOINT}')
# @user_required
def store(current_user=None): 
    try:
        validated_data = RCActeurSchema().load(
            request.json, session=session
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return RCActeurService.store(None, validated_data)

@route.get(f'{ENDPOINT}/<int:id>')
# @user_required
def show(current_user=None, id=1): 
    return RCActeurService.show(current_user, id)

@route.put(f'{ENDPOINT}/<int:id>')
@user_required
def update(current_user, id):
    try:
        validated_data = RCActeurSchema().load(
            request.json, 
            session=session,
            partial=True
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return RCActeurService.update(current_user, id, validated_data)

@route.delete(f'{ENDPOINT}/<int:id>')
@user_required
def delete(current_user, id): 
    return RCActeurService.delete(current_user, id)