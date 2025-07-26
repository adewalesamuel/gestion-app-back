from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE
from .model import INPlanification

class INPlanificationSchema(SQLAlchemySchema):
    class Meta:
        model = INPlanification
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    rc_engin_flottant_id = auto_field(validate=validate.Range(min=1))
    in_checklist_id = auto_field(validate=validate.Range(min=1))
    periodicite_jours = auto_field(validate=validate.Range(min=1))
    prochaine_date = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
