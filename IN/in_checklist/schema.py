from flask import json
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import post_load, pre_dump, validate, EXCLUDE
from .model import INChecklist

class INChecklistSchema(SQLAlchemySchema):
    class Meta:
        model = INChecklist
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    rc_type_engin_id = auto_field(validate=validate.Range(min=1))
    nom = auto_field(validate=validate.Length(min=1))
    version = auto_field()
    items = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @post_load
    def dump_items(self, data, **kwargs):
        if (data.get('items') != '' and 
        data.get('items') is not None):
            data['items'] = json.dumps(data['items'])
        return data
    
    @pre_dump
    def load_items(self, data, **kwargs):
        if (data.items != '' and 
        data.items is not None):
            data.items = json.loads(data.items)
        return data
