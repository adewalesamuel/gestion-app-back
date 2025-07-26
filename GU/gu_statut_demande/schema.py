from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE
from .model import GUStatutDemande

class GUStatutDemandeSchema(SQLAlchemySchema):
    class Meta:
        model = GUStatutDemande
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    code = auto_field(validate=validate.Length(min=1))
    libelle = auto_field(validate=validate.Length(min=1))
    couleur_hex = auto_field(validate=validate.Length(min=1))
    ordre = auto_field(validate=validate.Range(min=1))
    notifiable = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
