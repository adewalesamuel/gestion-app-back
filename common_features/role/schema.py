from flask import json
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import post_load, pre_dump, validate, EXCLUDE
from .model import Role

class RoleSchema(SQLAlchemySchema):
    class Meta:
        model = Role
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    name = auto_field(validate=validate.Length(min=1))
    description = auto_field()
    permissions = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @post_load
    def dump_permissions(self, data, **kwargs):
        if (data.get('permissions') != '' and 
        data.get('permissions') is not None):
            data['permissions'] = json.dumps(data['permissions'])
        return data
    
    @pre_dump
    def load_permissions(self, data, **kwargs):
        if (data.permissions != '' and 
        data.permissions is not None):
            data.permissions = json.loads(data.permissions)
        return data
    
