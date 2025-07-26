from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE
from .model import GUTypeDemande

class GUTypeDemandeSchema(SQLAlchemySchema):
    class Meta:
        model = GUTypeDemande
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    code = auto_field(validate=validate.Length(min=1))
    libelle = auto_field(validate=validate.Length(min=1))
    delai_traitement_jours = auto_field(validate=validate.Range(min=1))
    cout = auto_field(validate=validate.Range(min=1))
    validite_mois = auto_field(validate=validate.Range(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
