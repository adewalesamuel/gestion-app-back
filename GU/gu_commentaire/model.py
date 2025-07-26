from sqlalchemy import Column, BigInteger,  Text, Date, TIMESTAMP, ForeignKey, Time, func, text
from sqlalchemy.orm import relationship

from ...db import Base

class GUCommentaire(Base):
    __tablename__ = 'gu_commentaires'

    id = Column(BigInteger, primary_key = True)
    contenu = Column(Text)
    date = Column(Date, nullable = True)
    heure = Column(Time, nullable = True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 'gu_commentaires')
    gu_demande_id = Column(BigInteger, ForeignKey('gu_demandes.id', ondelete='CASCADE'), nullable = False)
    gu_demande = relationship('GUDemande', back_populates = 'gu_commentaires')

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)