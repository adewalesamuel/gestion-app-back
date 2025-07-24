from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class RCHistoriquePropriete(Base):
    __tablename__ = 'rc_historique_proprietes'

    id = Column(BigInteger, primary_key = True)
    rc_acteur_id = Column(BigInteger, ForeignKey('rc_acteurs.id', ondelete='CASCADE'), nullable = False)
    rc_acteur = relationship('RCActeur', back_populates = 'rc_historique_proprietes')
    rc_engin_flottant_id = Column(BigInteger, ForeignKey('rc_engin_flottants.id', ondelete='CASCADE'), nullable = False)
    rc_engin_flottant = relationship('RCEnginFlottant', back_populates = 'rc_historique_proprietes')
    date_debut = Column(Date )
    date_fin = Column(Date )
    type_transaction = Column(Enum('pending', 'canceled', 'validated') )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)