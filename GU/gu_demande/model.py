from sqlalchemy import Column, BigInteger,  String, Date, TIMESTAMP, JSON, ForeignKey, Time, func, text
from sqlalchemy.orm import relationship

from ...db import Base

class GUDemande(Base):
    __tablename__ = 'gu_demandes'

    id = Column(BigInteger, primary_key = True)
    gu_type_demande_id = Column(BigInteger, ForeignKey('gu_type_demandes.id', ondelete='CASCADE'), nullable = False)
    gu_type_demande = relationship('GUTypeDemande', back_populates = 'gu_demandes')
    gu_statut_demande_id = Column(BigInteger, ForeignKey('gu_statut_demandes.id', ondelete='CASCADE'), nullable = False)
    gu_statut_demande = relationship('GUStatutDemande', back_populates = 'gu_demandes')
    rc_acteur_id = Column(BigInteger, ForeignKey('rc_acteurs.id', ondelete='CASCADE'), nullable = False)
    rc_acteur = relationship('RCActeur', back_populates = 'gu_demandes')
    rc_engin_flottant_id = Column(BigInteger, ForeignKey('rc_engin_flottants.id', ondelete='CASCADE'), nullable = False)
    rc_engin_flottant = relationship('RCEnginFlottant', back_populates = 'gu_demandes')
    reference = Column(String(225))
    date_depot = Column(Date)
    heure = Column(Time)
    date_traitement = Column(Date, nullable = True)
    date_expiration = Column(Date, nullable = True)
    fichiers_joints = Column(JSON)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)