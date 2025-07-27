from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import RERemise

class RERemiseSchema(SQLAlchemySchema):
    class Meta:
        model = RERemise
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    re_ordre_recette_id = auto_field(validate=validate.Range(min=1))
    user_id = auto_field(validate=validate.Range(min=1))
    montant = auto_field(validate=validate.Range(min=1))
    pourcentage = auto_field(validate=validate.Range(min=0.0))
    raison = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
