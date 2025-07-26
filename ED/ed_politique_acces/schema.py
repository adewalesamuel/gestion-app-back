from flask import json
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import post_load, pre_dump, validate, EXCLUDE
from .model import EDPolitiqueAcces

class EDPolitiqueAccesSchema(SQLAlchemySchema):
    class Meta:
        model = EDPolitiqueAcces
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    ed_api_id = auto_field(validate=validate.Range(min=1))
    role_id = auto_field()
    nom = auto_field(validate=validate.Length(min=1))
    regles = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @post_load
    def dump_regles(self, data, **kwargs):
        if (data.get('regles') != '' and 
            data.get('regles') is not None):
            data['regles'] = json.dumps(data['regles'])
        return data
    
    @pre_dump
    def load_regles(self, data, **kwargs):
        if (data.regles != '' and data.regles is not None):
            data.regles = json.loads(data.regles)
        return data
