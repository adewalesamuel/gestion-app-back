from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE

from ...constants import ApiStatut
from ...utils import flatten_const_values
from .model import EDApi

class EDApiSchema(SQLAlchemySchema):
    class Meta:
        model = EDApi
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    nom = auto_field(validate=validate.Length(min=1))
    description = auto_field()
    url_base = auto_field()
    statut = auto_field(
        validate=[
            validate.Length(min=1),
            validate.OneOf(flatten_const_values(ApiStatut))
        ]
    )
    documentation_url = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
