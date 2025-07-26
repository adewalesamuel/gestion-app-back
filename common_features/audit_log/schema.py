from flask import json, request
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import post_load, pre_dump, pre_load, validate, EXCLUDE
from .model import AuditLog

class AuditLogSchema(SQLAlchemySchema):
    class Meta:
        model = AuditLog
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(dump_only=True)
    user_id = auto_field(validate=validate.Range(min=1))
    action = auto_field(validate=validate.Length(min=1))
    entite = auto_field(validate=validate.Length(min=1))
    entite_id = auto_field(validate=validate.Range(min=1))
    ancienne_valeur = auto_field()
    nouvelle_valeur = auto_field()
    ip_address = auto_field()
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @post_load
    def dump_ancienne_valeur(self, data, **kwargs):
        if (data.get('ancienne_valeur') != '' and 
            data.get('ancienne_valeur') is not None):
            data['ancienne_valeur'] = json.dumps(data['ancienne_valeur'])
        return data
    
    @post_load
    def dump_nouvelle_valeur(self, data, **kwargs):
        if (data.get('nouvelle_valeur') != '' and 
            data.get('nouvelle_valeur') is not None):
            data['nouvelle_valeur'] = json.dumps(data['nouvelle_valeur'])
        return data
    
    @pre_load
    def set_ip_address(self, data, **kwargs):
        data['ip_address'] = request.remote_addr
        return data
    
    @pre_dump
    def load_ancienne_valeur(self, data, **kwargs):
        if (data.ancienne_valeur != '' and 
            data.ancienne_valeur is not None):
            data.ancienne_valeur = json.loads(data.ancienne_valeur)
        return data
    
    
    @pre_dump
    def load_nouvelle_valeur(self, data, **kwargs):
        if (data.nouvelle_valeur != '' and 
            data.nouvelle_valeur is not None):
            data.nouvelle_valeur = json.loads(data.nouvelle_valeur)
        return data