from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE

from ...enums import ActeurType

from .model import RCActeur

class RCActeurSchema(SQLAlchemySchema):
    class Meta:
        model = RCActeur
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    type = auto_field(validate=validate.OneOf(ActeurType))
    nom = auto_field(validate=validate.Length(min=1))
    prenom = auto_field(validate=validate.Length(min=1))
    raison_sociale = auto_field(validate=validate.Length(min=1))
    registre_commerce = auto_field(validate=validate.Length(min=1))
    email = auto_field(validate=validate.Email())
    adresse = auto_field()
    telephone = auto_field(validate=validate.Length(min=1, max=10))
    secteur_activite = auto_field()
    pays_origine = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
