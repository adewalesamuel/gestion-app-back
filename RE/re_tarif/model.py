from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship

from ...db import Base

class RETarif(Base):
    __tablename__ = 're_tarifs'

    id = Column(BigInteger, primary_key = True)
    service = Column(String(225))
    montant = Column(Integer)
    devise = Column(String(225))
    frequence = Column(Enum('pending', 'canceled', 'validated') )
    type_acteur = Column(String(225))

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)