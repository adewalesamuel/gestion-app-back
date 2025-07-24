from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.exceptions import UnprocessableEntity
from ... import config
from ...db import session
from ...decorators import user_required
from .schema import UserSchema
from .service import UserService

route = Blueprint(
    'user', 
    __name__, 
    url_prefix = config.app.get('API_PREFIX')
)
ENDPOINT = '/users'

@route.get(f'{ENDPOINT}')
def index(current_user=None): 
    return UserService.index(current_user)

@route.post(f'{ENDPOINT}')
# @user_required
def store(current_user=None): 
    try:
        validated_data = UserSchema().load(
            request.json, session=session
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return UserService.store(None, validated_data)

@route.get(f'{ENDPOINT}/<int:id>')
@user_required
def show(current_user=None, id=1): 
    return UserService.show(current_user, id)

@route.put(f'{ENDPOINT}/<int:id>')
@user_required
def update(current_user, id):
    try:
        validated_data = UserSchema().load(
            request.json, 
            session=session,
            partial=True
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return UserService.update(current_user, id, validated_data)

@route.delete(f'{ENDPOINT}/<int:id>')
@user_required
def delete(current_user, id): 
    return UserService.delete(current_user, id)