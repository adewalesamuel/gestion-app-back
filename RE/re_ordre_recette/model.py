from sqlalchemy import Column, Integer, BigInteger,  String, Date, TIMESTAMP, Enum, ForeignKey, func, text
from sqlalchemy.orm import relationship

from ...enums import OrdreRecetteStatut
from ...db import Base

class REOrdreRecette(Base):
    __tablename__ = 're_ordre_recettes'

    id = Column(BigInteger, primary_key = True)
    rc_acteur_id = Column(BigInteger, ForeignKey('rc_acteurs.id', ondelete='CASCADE'), nullable = False)
    rc_acteur = relationship('RCActeur', back_populates = 're_ordre_recettes')
    reference = Column(String(225))
    montant = Column(Integer)
    devise = Column(String(225))
    date_emission = Column(Date)
    date_echeance = Column(Date)
    statut = Column(
        Enum(OrdreRecetteStatut),
        default =  OrdreRecetteStatut.emis
    )
    service_concerne = Column(String(225))

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)