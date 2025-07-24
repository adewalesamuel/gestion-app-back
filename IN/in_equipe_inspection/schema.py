from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import INEquipeInspection

class INEquipeInspectionSchema(SQLAlchemySchema):
    class Meta:
        model = INEquipeInspection
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    user_id = auto_field(validate=validate.Range(min=1))
    nom = auto_field(validate=validate.Length(min=1))
    membres = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
