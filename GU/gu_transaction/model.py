from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class GUTransaction(Base):
    __tablename__ = 'gu_transactions'

    id = Column(BigInteger, primary_key = True)
    re_mode_paiement_id = Column(BigInteger, ForeignKey('re_mode_paiements.id', ondelete='CASCADE'), nullable = False)
    re_mode_paiement = relationship('REModePaiement', back_populates = 'gu_transactions')
    gu_demande_id = Column(BigInteger, ForeignKey('gu_demandes.id', ondelete='CASCADE'), nullable = False)
    gu_demande = relationship('GUDemande', back_populates = 'gu_transactions')
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 'gu_transactions')
    reference = Column(String(225) )
    montant = Column(Integer )
    devise = Column(String(225) )
    date_transaction = Column(Date )
    heure = Column(String(225) )
    statut = Column(Enum('pending', 'canceled', 'validated') )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)