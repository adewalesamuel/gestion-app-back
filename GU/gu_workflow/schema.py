from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, EXCLUDE
from .model import GUWorkflow

class GUWorkflowSchema(SQLAlchemySchema):
    class Meta:
        model = GUWorkflow
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    role_id = auto_field(validate=validate.Range(min=1))
    gu_type_demande_id = auto_field(validate=validate.Range(min=1))
    etape = auto_field(validate=validate.Length(min=1))
    ordre = auto_field(validate=validate.Range(min=1))
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
