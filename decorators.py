from flask import abort, json, request
from werkzeug.exceptions import Unauthorized, Forbidden
from functools import wraps

from . import utils
from .libs import jwt
from .db import session
#from .common_features.admin.model import Admin
from .common_features.user.model import User

def user_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = utils.get_bearer_token(request.headers.get('authorization', ''))

        if token is None: raise Unauthorized('no token found')
        try:
            data = jwt.decode_token(token)
        except jwt.exceptions.InvalidTokenError as e:
            raise Unauthorized('token in invalid')
            
        current_user =  session.query(User).filter(
            User.id == data.get('user_id'), 
            User.deleted_at == None
        ).first()

        if current_user is None:
            raise Unauthorized('unauthorized')

        return f(current_user, *args, **kwargs)
    return decorator


def admin_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = utils.get_bearer_token(request.headers.get('authorization', ''))

        if token is None: raise Unauthorized('token in missing')
        try:
            data = jwt.decode_token(token)
        except jwt.exceptions.InvalidTokenError as e:
            raise Unauthorized('token in invalid')

        current_admin: Admin =  session.query(Admin).filter(
                Admin.id == data.get('admin_id'), 
                Admin.deleted_at == None
            ).first()
        if current_admin is None: 
            raise Unauthorized('unauthorized')

        return f(current_admin, *args, **kwargs)
    return decorator


def can(permission):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            current_user: User = args[0]
            
            if (current_user.role is None or
                permission not in json.loads(
                    current_user.role.permissions
                    )):
                raise Forbidden('no permission found')

            return f(*args, **kwargs)
        return wrapper
    return decorator