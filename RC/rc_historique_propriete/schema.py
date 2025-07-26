from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE

from ...constants import HistoriqueProprieteTypeTransaction
from ...utils import flatten_const_values
from .model import RCHistoriquePropriete

class RCHistoriqueProprieteSchema(SQLAlchemySchema):
    class Meta:
        model = RCHistoriquePropriete
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    rc_acteur_id = auto_field(validate=validate.Range(min=1))
    rc_engin_flottant_id = auto_field(validate=validate.Range(min=1))
    date_debut = auto_field()
    date_fin = auto_field()
    type_transaction = auto_field(
        validate=[
            validate.Length(min=1),
            validate.OneOf(flatten_const_values(HistoriqueProprieteTypeTransaction))
        ]
    )
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
