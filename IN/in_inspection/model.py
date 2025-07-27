from sqlalchemy import Column, BigInteger,  String, Date, TIMESTAMP, Enum, ForeignKey, Time, func, text
from sqlalchemy.orm import relationship

from ...enums import InspectionResultat, InspectionStatut


from ...db import Base

class INInspection(Base):
    __tablename__ = 'in_inspections'

    id = Column(BigInteger, primary_key = True)
    in_type_controle_id = Column(BigInteger, ForeignKey('in_type_controles.id', ondelete='CASCADE'), nullable = False)
    in_type_controle = relationship('INTypeControle', back_populates = 'in_inspections')
    in_equipe_inspection_id = Column(BigInteger, ForeignKey('in_equipe_inspections.id', ondelete='CASCADE'), nullable = False)
    in_equipe_inspection = relationship('INEquipeInspection', back_populates = 'in_inspections')
    rc_engin_flottant_id = Column(BigInteger, ForeignKey('rc_engin_flottants.id', ondelete='CASCADE'), nullable = False)
    rc_engin_flottant = relationship('RCEnginFlottant', back_populates = 'in_inspections')
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 'in_inspections')
    reference = Column(String(225))
    date_planifiee = Column(Date)
    heure = Column(Time)
    date_reelle = Column(Date)
    statut = Column(
        Enum(InspectionStatut),
        default = InspectionStatut.planifiee
    )
    resultat = Column(
        Enum(InspectionResultat),
        default = InspectionResultat.conforme 
    )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)