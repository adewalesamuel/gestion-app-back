import datetime
import jwt

from .. import config
from ..common_features.user.model import User
#from ..common_features.admin.model import Admin

exceptions = jwt.exceptions

ALGORITHMS = ["HS256"]

def make_token(user: User, user_type='user') -> str:
    return (
        jwt.encode(
            {
                f'{user_type}_id' : user.id, 
                'exp' : datetime.datetime.now(datetime.timezone.utc) + 
                datetime.timedelta(config.jwt.get('EXPIRATION_DAYS'))
            }, 
            key=config.jwt.get('SECRET_KEY'), 
            algorithm=ALGORITHMS[0]
        ) 
    )

def decode_token(token: str) -> dict:
    return (
        jwt.decode(
            jwt=token, 
            key=config.jwt.get('SECRET_KEY'), 
            algorithms=ALGORITHMS
        )
    )