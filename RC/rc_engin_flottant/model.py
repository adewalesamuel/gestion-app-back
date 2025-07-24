from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class RCEnginFlottant(Base):
    __tablename__ = 'rc_engin_flottants'

    id = Column(BigInteger, primary_key = True)
    rc_type_engin_id = Column(BigInteger, ForeignKey('rc_type_engins.id', ondelete='CASCADE'), nullable = False)
    rc_type_engin = relationship('RCTypeEngin', back_populates = 'rc_engin_flottants')
    rc_pays_id = Column(BigInteger, ForeignKey('rc_payss.id', ondelete='CASCADE'), nullable = False)
    rc_pays = relationship('RCPays', back_populates = 'rc_engin_flottants')
    rc_acteur_id = Column(BigInteger, ForeignKey('rc_acteurs.id', ondelete='CASCADE'), nullable = False)
    rc_acteur = relationship('RCActeur', back_populates = 'rc_engin_flottants')
    nom = Column(String(225) )
    immatriculation = Column(String(225) )
    tonnage_brut = Column(Integer )
    longueur = Column(Numeric)
    annee_construction = Column(Date )
    capacite_passagers = Column(Integer )
    capacite_fret = Column(Integer )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)