from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import EDSchemaDonnees

class EDSchemaDonneesSchema(SQLAlchemySchema):
    class Meta:
        model = EDSchemaDonnees
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    nom = auto_field(validate=validate.Length(min=1))
    version = auto_field(validate=validate.Length(min=1))
    schema_json = auto_field()
    statut = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
