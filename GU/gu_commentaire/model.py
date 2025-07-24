from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class GUCommentaire(Base):
    __tablename__ = 'gu_commentaires'

    id = Column(BigInteger, primary_key = True)
    contenu = Column(Text )
    date = Column(Date )
    heure = Column(String(225) )
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 'gu_commentaires')
    gu_demande_id = Column(BigInteger, ForeignKey('gu_demandes.id', ondelete='CASCADE'), nullable = False)
    gu_demande = relationship('GUDemande', back_populates = 'gu_commentaires')

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)