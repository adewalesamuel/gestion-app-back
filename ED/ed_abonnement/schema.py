from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import EDAbonnement

class EDAbonnementSchema(SQLAlchemySchema):
    class Meta:
        model = EDAbonnement
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    ed_api_id = auto_field(validate=validate.Range(min=1))
    rc_acteur_id = auto_field(validate=validate.Range(min=1))
    nom_client = auto_field(validate=validate.Length(min=1))
    token = auto_field(validate=validate.Length(min=1))
    date_expiration = auto_field(validate=validate.Length(min=1))
    limite_requetes_jour = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
