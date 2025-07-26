from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE, post_load

from ...libs import crypto
from .model import User

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    role_id = auto_field(validate=validate.Range(min=1))
    rc_acteur_id = auto_field()
    profil_img_url = auto_field()
    nom = auto_field(validate=validate.Length(min=1))
    email = auto_field(validate=validate.Email())
    password = auto_field(load_only=True, validate=validate.Length(min=6))
    last_login_date = auto_field(dump_only=True)
    last_login_heure = auto_field(dump_only=True)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @post_load
    def hash_password(self, data, **kwargs):
        if (data.get('password') == '' or data.get('password') is None): return data
        data['password'] = crypto.hash_password(data['password'])
        return data
