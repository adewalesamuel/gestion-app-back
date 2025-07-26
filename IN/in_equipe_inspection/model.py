from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship

from ...db import Base

class INEquipeInspection(Base):
    __tablename__ = 'in_equipe_inspections'

    id = Column(BigInteger, primary_key = True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 'in_equipe_inspections')
    nom = Column(String(225), unique = True)
    membres = Column(JSON, nullable = True)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)