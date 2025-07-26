from sqlalchemy import Column, Integer, BigInteger,  String, Date, TIMESTAMP, ForeignKey, Time, func, text
from sqlalchemy.orm import relationship

from ...db import Base

class REPaiement(Base):
    __tablename__ = 're_paiements'

    id = Column(BigInteger, primary_key = True)
    re_ordre_recette_id = Column(BigInteger, ForeignKey('re_ordre_recettes.id', ondelete='CASCADE'), nullable = False)
    re_ordre_recette = relationship('REOrdreRecette', back_populates = 're_paiements')
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 're_paiements')
    re_mode_paiement_id = Column(BigInteger, ForeignKey('re_mode_paiements.id', ondelete='CASCADE'), nullable = False)
    re_mode_paiement = relationship('REModePaiement', back_populates = 're_paiements')
    montant = Column(Integer)
    devise = Column(String(225))
    date_paiement = Column(Date)
    heure = Column(Time)
    reference_transaction = Column(String(225))

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)