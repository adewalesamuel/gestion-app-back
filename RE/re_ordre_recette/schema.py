from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import REOrdreRecette

class REOrdreRecetteSchema(SQLAlchemySchema):
    class Meta:
        model = REOrdreRecette
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    rc_acteur_id = auto_field(validate=validate.Range(min=1))
    reference = auto_field(validate=validate.Length(min=1))
    montant = auto_field(validate=validate.Range(min=1))
    devise = auto_field(validate=validate.Length(min=1))
    date_emission = auto_field(validate=validate.Length(min=1))
    date_echeance = auto_field(validate=validate.Length(min=1))
    statut = auto_field(validate=validate.Length(min=1))
    service_concerne = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
