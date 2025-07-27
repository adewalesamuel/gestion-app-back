from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE
from ...enums import NonConformiteGravite, NonConformiteStatut

from .model import INNonConformite

class INNonConformiteSchema(SQLAlchemySchema):
    class Meta:
        model = INNonConformite
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    in_inspection_id = auto_field(validate=validate.Range(min=1))
    user_id = auto_field(validate=validate.Range(min=1))
    description = auto_field()
    gravite = auto_field(validate=validate.OneOf(NonConformiteGravite))
    date_decouverte = auto_field()
    heure = auto_field()
    date_resolution = auto_field()
    statut = auto_field(validate=validate.OneOf(NonConformiteStatut))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
