from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class EDAbonnement(Base):
    __tablename__ = 'ed_abonnements'

    id = Column(BigInteger, primary_key = True)
    ed_api_id = Column(BigInteger, ForeignKey('ed_apis.id', ondelete='CASCADE'), nullable = False)
    ed_api = relationship('EDApi', back_populates = 'ed_abonnements')
    rc_acteur_id = Column(BigInteger, ForeignKey('rc_acteurs.id', ondelete='CASCADE'), nullable = False)
    rc_acteur = relationship('RCActeur', back_populates = 'ed_abonnements')
    nom_client = Column(String(225) )
    token = Column(String(225) )
    date_expiration = Column(Date )
    limite_requetes_jour = Column(Integer )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)