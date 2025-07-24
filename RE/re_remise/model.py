from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class RERemise(Base):
    __tablename__ = 're_remises'

    id = Column(BigInteger, primary_key = True)
    re_ordre_recette_id = Column(BigInteger, ForeignKey('re_ordre_recettes.id', ondelete='CASCADE'), nullable = False)
    re_ordre_recette = relationship('REOrdreRecette', back_populates = 're_remises')
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 're_remises')
    montant = Column(Integer )
    pourcentage = Column(Numeric)
    raison = Column(Text )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)