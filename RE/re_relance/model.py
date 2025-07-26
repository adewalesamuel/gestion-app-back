from sqlalchemy import Column, BigInteger,  Date, TIMESTAMP, Enum, ForeignKey, Time, func, text
from sqlalchemy.orm import relationship

from ...db import Base

class RERelance(Base):
    __tablename__ = 're_relances'

    id = Column(BigInteger, primary_key = True)
    re_ordre_recette_id = Column(BigInteger, ForeignKey('re_ordre_recettes.id', ondelete='CASCADE'), nullable = False)
    re_ordre_recette = relationship('REOrdreRecette', back_populates = 're_relances')
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 're_relances')
    date = Column(Date)
    heure = Column(Time)
    mode = Column(Enum('pending', 'canceled', 'validated') )
    statut = Column(Enum('pending', 'canceled', 'validated') )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)