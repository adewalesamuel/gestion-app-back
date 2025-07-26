import datetime
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import post_load, validate, EXCLUDE

from ...constants import HistoriqueAction
from ...utils import flatten_const_values
from .model import GUHistorique

class GUHistoriqueSchema(SQLAlchemySchema):
    class Meta:
        model = GUHistorique
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    user_id = auto_field(validate=validate.Range(min=1))
    gu_demande_id = auto_field(validate=validate.Range(min=1))
    action = auto_field(
        validate=[
            validate.Length(min=1),
            validate.OneOf(flatten_const_values(HistoriqueAction))
        ]
    )
    details = auto_field()
    date = auto_field()
    heure = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @post_load
    def set_date_heure_historique(self, data, **kwargs):
        today_utc_date = datetime.datetime.now(datetime.timezone.utc)
        if (data.get('date') is not None): return data
        data['date'] = today_utc_date.date()
        if (data.get('heure') is not None): return data
        data['heure'] = str(today_utc_date.time())

        return data
