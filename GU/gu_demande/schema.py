import datetime
from flask import json
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import post_load, pre_load, pre_dump, validate, EXCLUDE
from .model import GUDemande

class GUDemandeSchema(SQLAlchemySchema):
    class Meta:
        model = GUDemande
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    gu_type_demande_id = auto_field(validate=validate.Range(min=1))
    gu_statut_demande_id = auto_field(validate=validate.Range(min=1))
    rc_acteur_id = auto_field(validate=validate.Range(min=1))
    rc_engin_flottant_id = auto_field(validate=validate.Range(min=1))
    reference = auto_field(validate=validate.Length(min=1))
    date_depot = auto_field(required = False)
    heure = auto_field(required = False)
    date_traitement = auto_field()
    date_expiration = auto_field()
    fichiers_joints = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @post_load
    def dump_fichiers_joints(self, data, **kwargs):
        if (data.get('fichiers_joints') != '' and 
        data.get('fichiers_joints') is not None):
            data['fichiers_joints'] = json.dumps(data['fichiers_joints'])
        return data
    
    @pre_load
    def set_date_heure_depot(self, data, **kwargs):
        today_utc_date = datetime.datetime.now(datetime.timezone.utc)
        
        if (data.get('date_depot') is None):
            data['date_depot'] = today_utc_date.date()
        if (data.get('heure') is None):
            data['heure'] = today_utc_date.time()

        return data
    
    @pre_dump
    def load_fichiers_joints(self, data, **kwargs):
        if (data.fichiers_joints != '' and 
        data.fichiers_joints is not None):
            data.fichiers_joints = json.loads(data.fichiers_joints)
        return data
