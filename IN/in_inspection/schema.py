from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import INInspection

class INInspectionSchema(SQLAlchemySchema):
    class Meta:
        model = INInspection
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    in_type_controle_id = auto_field(validate=validate.Range(min=1))
    in_equipe_inspection_id = auto_field(validate=validate.Range(min=1))
    rc_engin_flottant_id = auto_field(validate=validate.Range(min=1))
    user_id = auto_field(validate=validate.Range(min=1))
    reference = auto_field(validate=validate.Length(min=1))
    date_planifiee = auto_field(validate=validate.Length(min=1))
    heure = auto_field()
    date_reelle = auto_field(validate=validate.Length(min=1))
    statut = auto_field(validate=validate.Length(min=1))
    resultat = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
