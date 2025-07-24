from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import RCEnginFlottant

class RCEnginFlottantSchema(SQLAlchemySchema):
    class Meta:
        model = RCEnginFlottant
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    rc_type_engin_id = auto_field(validate=validate.Range(min=1))
    rc_pays_id = auto_field(validate=validate.Range(min=1))
    rc_acteur_id = auto_field(validate=validate.Range(min=1))
    nom = auto_field(validate=validate.Length(min=1))
    immatriculation = auto_field(validate=validate.Length(min=1))
    tonnage_brut = auto_field(validate=validate.Length(min=1))
    longueur = auto_field(validate=validate.Length(min=1))
    annee_construction = auto_field(validate=validate.Length(min=1))
    capacite_passagers = auto_field(validate=validate.Length(min=1))
    capacite_fret = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
