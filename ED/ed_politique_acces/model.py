from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class EDPolitiqueAcces(Base):
    __tablename__ = 'ed_politique_access'

    id = Column(BigInteger, primary_key = True)
    ed_api_id = Column(BigInteger, ForeignKey('ed_apis.id', ondelete='CASCADE'), nullable = False)
    ed_api = relationship('EDApi', back_populates = 'ed_politique_access')
    role_id = Column(BigInteger, ForeignKey('roles.id', ondelete='CASCADE'), nullable = False)
    role = relationship('Role', back_populates = 'ed_politique_access')
    nom = Column(String(225) )
    regles = Column(JSON)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)