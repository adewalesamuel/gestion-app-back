from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import GUCommentaire

class GUCommentaireSchema(SQLAlchemySchema):
    class Meta:
        model = GUCommentaire
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    contenu = auto_field(validate=validate.Length(min=1))
    date = auto_field()
    heure = auto_field()
    user_id = auto_field(validate=validate.Range(min=1))
    gu_demande_id = auto_field(validate=validate.Range(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
