from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE
from .model import EDFormatDonnees

class EDFormatDonneesSchema(SQLAlchemySchema):
    class Meta:
        model = EDFormatDonnees
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    nom = auto_field(validate=validate.Length(min=1))
    mime_type = auto_field()
    schema_xsd_url = auto_field()
    exemple_url = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
