from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import GUDemande

class GUDemandeSchema(SQLAlchemySchema):
    class Meta:
        model = GUDemande
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    gu_type_demande_id = auto_field(validate=validate.Range(min=1))
    gu_statut_demande_id = auto_field(validate=validate.Range(min=1))
    rc_acteur_id = auto_field(validate=validate.Range(min=1))
    rc_engin_flottant_id = auto_field(validate=validate.Range(min=1))
    reference = auto_field(validate=validate.Length(min=1))
    date_depot = auto_field()
    heure = auto_field()
    date_traitement = auto_field()
    date_expiration = auto_field()
    fichiers_joints = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
