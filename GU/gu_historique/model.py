from sqlalchemy import Column, BigInteger,  Text, Date, TIMESTAMP, Enum, ForeignKey, Time, func, text
from sqlalchemy.orm import relationship


from ...enums import HistoriqueAction
from ...db import Base

class GUHistorique(Base):
    __tablename__ = 'gu_historiques'

    id = Column(BigInteger, primary_key = True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 'gu_historiques')
    gu_demande_id = Column(BigInteger, ForeignKey('gu_demandes.id', ondelete='CASCADE'), nullable = False)
    gu_demande = relationship('GUDemande', back_populates = 'gu_historiques')
    action = Column(
        Enum(HistoriqueAction),
        default = HistoriqueAction.creation
    )
    details = Column(Text)
    date = Column(Date)
    heure = Column(Time)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)