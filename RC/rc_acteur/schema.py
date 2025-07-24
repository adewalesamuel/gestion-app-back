from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import RCActeur

class RCActeurSchema(SQLAlchemySchema):
    class Meta:
        model = RCActeur
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    type = auto_field(validate=validate.Length(min=1))
    nom = auto_field(validate=validate.Length(min=1))
    prenom = auto_field(validate=validate.Length(min=1))
    raison_sociale = auto_field(validate=validate.Length(min=1))
    registre_commerce = auto_field(validate=validate.Length(min=1))
    email = auto_field(validate=validate.Email())
    adresse = auto_field(validate=validate.Length(min=1))
    telephone = auto_field(validate=validate.Length(min=1))
    secteur_activite = auto_field(validate=validate.Length(min=1))
    pays_origine = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
