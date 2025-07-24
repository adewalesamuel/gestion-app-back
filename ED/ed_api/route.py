from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.exceptions import UnprocessableEntity
from ... import config
from ...db import session
from ...decorators import user_required
from .schema import EDApiSchema
from .service import EDApiService

route = Blueprint(
    'ed_api', 
    __name__, 
    url_prefix = config.app.get('API_PREFIX')
)
ENDPOINT = '/ed-apis'

@route.get(f'{ENDPOINT}')
@user_required
def index(current_user): 
    return EDApiService.index(current_user)

@route.post(f'{ENDPOINT}')
@user_required
def store(current_user): 
    try:
        validated_data = EDApiSchema().load(
            request.json, session=session
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return EDApiService.store(current_user, validated_data)

@route.get(f'{ENDPOINT}/<int:id>')
@user_required
def show(current_user, id): 
    return EDApiService.show(current_user, id)

@route.put(f'{ENDPOINT}/<int:id>')
@user_required
def update(current_user, id):
    try:
        validated_data = EDApiSchema().load(
            request.json, 
            session=session,
            partial=True
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return EDApiService.update(current_user, id, validated_data)

@route.delete(f'{ENDPOINT}/<int:id>')
@user_required
def delete(current_user, id): 
    return EDApiService.delete(current_user, id)