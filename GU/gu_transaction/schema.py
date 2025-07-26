import datetime
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE, pre_load

from ...constants import TransactionStatut
from ...utils import flatten_const_values
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
    montant = auto_field(validate=validate.Range(min=1))
    devise = auto_field(validate=validate.Length(min=1))
    date_transaction = auto_field(required = False)
    heure = auto_field(required = False)
    statut = auto_field(
        validate=[
            validate.Length(min=1),
            validate.OneOf(flatten_const_values(TransactionStatut))
        ]
    )
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @pre_load
    def set_date_heure_transaction(self, data, **kwargs):
        today_utc_date = datetime.datetime.now(datetime.timezone.utc)
        if (data.get('date_transaction') is None):
            data['date_transaction'] = today_utc_date.date()
        if (data.get('heure') is None):
            data['heure'] = today_utc_date.time()

        return data
