import datetime
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import pre_load, validate, EXCLUDE
from .model import GUCommentaire

class GUCommentaireSchema(SQLAlchemySchema):
    class Meta:
        model = GUCommentaire
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    contenu = auto_field(validate=validate.Length(min=1))
    date = auto_field(required = False)
    heure = auto_field(required = False)
    user_id = auto_field(validate=validate.Range(min=1))
    gu_demande_id = auto_field(validate=validate.Range(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @pre_load
    def set_date_heure(self, data, **kwargs):
        today_utc_date = datetime.datetime.now(datetime.timezone.utc)
        if (data.get('date') is not None): return data
        data['date'] = today_utc_date.date()
        if (data.get('heure') is not None): return data
        data['heure'] = today_utc_date.time()

        return data
