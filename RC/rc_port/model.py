from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class RCPort(Base):
    __tablename__ = 'rc_ports'

    id = Column(BigInteger, primary_key = True)
    rc_pays_id = Column(BigInteger, ForeignKey('rc_payss.id', ondelete='CASCADE'), nullable = False)
    rc_pays = relationship('RCPays', back_populates = 'rc_ports')
    nom = Column(String(225) )
    code = Column(String(225) , unique = True, nullable = False)
    capacite_accueil = Column(Integer )
    profondeur_max = Column(Numeric)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)