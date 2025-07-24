from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class INNonConformite(Base):
    __tablename__ = 'in_non_conformites'

    id = Column(BigInteger, primary_key = True)
    in_inspection_id = Column(BigInteger, ForeignKey('in_inspections.id', ondelete='CASCADE'), nullable = False)
    in_inspection = relationship('INInspection', back_populates = 'in_non_conformites')
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 'in_non_conformites')
    description = Column(Text )
    gravite = Column(Enum('pending', 'canceled', 'validated') )
    date_decouverte = Column(Date )
    heure = Column(String(225) )
    date_resolution = Column(Date )
    statut = Column(Enum('pending', 'canceled', 'validated') )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)