from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import REModePaiement

class REModePaiementSchema(SQLAlchemySchema):
    class Meta:
        model = REModePaiement
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    code = auto_field(validate=validate.Length(min=1))
    libelle = auto_field(validate=validate.Length(min=1))
    frais_pourcentage = auto_field(validate=validate.Range(min=0))
    delai_jours = auto_field(validate=validate.Range(min=0))
    actif = auto_field(validate=validate.OneOf([True, False]))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
