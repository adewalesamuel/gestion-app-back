from os import environ
from environs import Env

env = Env()
env.read_env()

app = {
    'API_PREFIX': environ.get('APP_API_PREFIX')
}

db = {
    'HOST': environ.get('DB_HOST', 'localhost'),
    'USERNAME': environ.get('USERNAME', 'root'),
    'PASSWORD': environ.get('PASSWORD', ''),
    'DATABASE': environ.get('DATABASE', ''),
    'POOL_SIZE': environ.get('DB_POOL_SIZE', 100),
    'MAX_OVERFLOW': environ.get('DB_MAX_OVERFLOW', 10)
}

mail = {
    'FROM': environ.get('MAIL_FROM', '')
}

jwt = {
    'SECRET_KEY': environ.get('JWT_SECRET_KEY', 'secret'),
    'EXPIRATION_DAYS': float(environ.get('JWT_EXPIRATION_DAYS', 3))
}