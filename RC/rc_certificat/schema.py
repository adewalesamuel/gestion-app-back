from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import RCCertificat

class RCCertificatSchema(SQLAlchemySchema):
    class Meta:
        model = RCCertificat
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    rc_engin_flottant_id = auto_field(validate=validate.Range(min=1))
    type = auto_field(validate=validate.Length(min=1))
    numero = auto_field(validate=validate.Length(min=1))
    date_emission = auto_field(validate=validate.Length(min=1))
    date_expiration = auto_field(validate=validate.Length(min=1))
    organisme_emetteur = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
