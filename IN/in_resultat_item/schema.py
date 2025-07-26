from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE
from .model import INResultatItem

class INResultatItemSchema(SQLAlchemySchema):
    class Meta:
        model = INResultatItem
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    in_inspection_id = auto_field(validate=validate.Range(min=1))
    conforme = auto_field(validate=validate.OneOf([True, False]))
    observations = auto_field(validate=validate.Length(min=1))
    checklist_item_code = auto_field(validate=validate.Length(min=1))
    photo_url = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
