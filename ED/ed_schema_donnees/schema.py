from flask import json
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import post_load, pre_dump, validate, EXCLUDE

from ...constants import SchemaDonneesStatut
from ...utils import flatten_const_values
from .model import EDSchemaDonnees

class EDSchemaDonneesSchema(SQLAlchemySchema):
    class Meta:
        model = EDSchemaDonnees
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    nom = auto_field(validate=validate.Length(min=1))
    version = auto_field()
    schema_json = auto_field()
    statut = auto_field(
        validate=[
            validate.Length(min=1),
            validate.OneOf(flatten_const_values(SchemaDonneesStatut))
        ]
    )
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @post_load
    def dump_schema_json(self, data, **kwargs):
        if (data.get('schema_json') == '' or data.get('schema_json') is None): return data
        data['schema_json'] = json.dumps(data['schema_json'])
        return data
    
    @pre_dump
    def load_schema_json(self, data, **kwargs):
        if (data.schema_json == '' or data.schema_json is None): return data
        data.schema_json = json.loads(data.schema_json)
        return data
