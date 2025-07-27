from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE

from ...enums import TypeControleGraviteMin
from .model import INTypeControle

class INTypeControleSchema(SQLAlchemySchema):
    class Meta:
        model = INTypeControle
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    code = auto_field(validate=validate.Length(min=1))
    libelle = auto_field(validate=validate.Length(min=1))
    norme_reference = auto_field(validate=validate.Length(min=1))
    frequence_mois = auto_field(validate=validate.Range(min=1))
    gravite_min = auto_field(validate=validate.OneOf(TypeControleGraviteMin))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
