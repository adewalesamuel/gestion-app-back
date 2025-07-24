from flask import Blueprint, abort, request
from marshmallow import ValidationError
from werkzeug.exceptions import UnprocessableEntity
from ... import config
from ...db import session
from ..user.schema import UserSchema
from .schema import LoginSchema
from .service import AuthService

route = Blueprint(
    'auth', 
    __name__, 
    url_prefix = config.app.get('API_PREFIX')
)

@route.post(f'/register')
def register():
    try:
        validated_data: UserSchema = UserSchema().load(
            request.json, session=session # type: ignore
        )
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return AuthService.register(validated_data)

@route.post(f'/login')
def login():
    try:
        validated_data = LoginSchema().load(request.json)
    except ValidationError as e:
        raise UnprocessableEntity(e.messages)
    return AuthService.login(validated_data)