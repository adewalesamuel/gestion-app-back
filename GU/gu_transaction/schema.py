from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE
from .model import GUTransaction

class GUTransactionSchema(SQLAlchemySchema):
    class Meta:
        model = GUTransaction
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    re_mode_paiement_id = auto_field(validate=validate.Range(min=1))
    gu_demande_id = auto_field(validate=validate.Range(min=1))
    user_id = auto_field(validate=validate.Range(min=1))
    reference = auto_field(validate=validate.Length(min=1))
    montant = auto_field(validate=validate.Length(min=1))
    devise = auto_field(validate=validate.Length(min=1))
    date_transaction = auto_field(validate=validate.Length(min=1))
    heure = auto_field()
    statut = auto_field(validate=validate.Length(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
