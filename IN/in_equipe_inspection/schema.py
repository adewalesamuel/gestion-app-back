import json
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import post_load, pre_dump, validate, EXCLUDE
from .model import INEquipeInspection

class INEquipeInspectionSchema(SQLAlchemySchema):
    class Meta:
        model = INEquipeInspection
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    user_id = auto_field(validate=validate.Range(min=1))
    nom = auto_field(validate=validate.Length(min=1))
    membres = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
    
    @post_load
    def dump_membres(self, data, **kwargs):
        if (data.get('membres') != '' and 
        data.get('membres') is not None):
            data['membres'] = json.dumps(data['membres'])
        return data
    
    @pre_dump
    def load_membres(self, data, **kwargs):
        if (data.membres != '' and 
        data.membres is not None):
            data.membres = json.loads(data.membres)
        return data