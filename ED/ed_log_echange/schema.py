from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE

from ...enums import LogEchangeTypeRequete

from .model import EDLogEchange

class EDLogEchangeSchema(SQLAlchemySchema):
    class Meta:
        model = EDLogEchange
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    ed_api_id = auto_field(validate=validate.Range(min=1))
    user_id = auto_field(validate=validate.Range(min=1))
    date_heure = auto_field()
    heure = auto_field()
    type_requete = auto_field(validate=validate.OneOf(LogEchangeTypeRequete))
    endpoint = auto_field(validate=validate.Length(min=1))
    statut_reponse = auto_field(validate=validate.Range(min=0, max=511))
    temps_reponse_ms = auto_field(validate=validate.Range(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
