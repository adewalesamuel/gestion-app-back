from sqlalchemy import Column, Integer, BigInteger,  String, TIMESTAMP, JSON, ForeignKey, func, text
from sqlalchemy.orm import relationship

from ...db import Base

class AuditLog(Base):
    __tablename__ = 'audit_logs'

    id = Column(BigInteger, primary_key = True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 'audit_logs')
    action = Column(String(225))
    entite = Column(String(225))
    entite_id = Column(Integer)
    ancienne_valeur = Column(JSON)
    nouvelle_valeur = Column(JSON)
    ip_address = Column(String(225))

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)