from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE

from ...enums import HistoriqueProprieteTypeTransaction

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
    type_transaction = auto_field(validate=validate.OneOf(HistoriqueProprieteTypeTransaction))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
