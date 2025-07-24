from marshmallow import Schema, fields, validate, validates_schema, ValidationError


class LoginSchema(Schema):
    email = fields.Email(validate=validate.Email())
    password = fields.Str(validate=validate.Length(min=6))


class UpdatePasswordSchema(Schema):
    password = fields.Str(validate=validate.Length(min=6))
    password_confirmation = fields.Str(validate=validate.Length(min=6))
    
    @validates_schema
    def validate_password(self, data, **kwargs):
        if data['password'] != data['password_confirmation']:
            raise ValidationError('password must be equal to password_confirmation')

 
class InitPasswordSchema(Schema):
    password = fields.Str(validate=validate.Length(min=1))
    confirmPassword = fields.Str(validate=validate.Length(min=1))
    token = fields.Str(validate=validate.Length(min=1))
    
    @validates_schema
    def validate_password(self, data, **kwargs):
        if data.get('password') != data.get('password_confirmation'):
            raise ValidationError('password must be equal to password_confirmation')
            
