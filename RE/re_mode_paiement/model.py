from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Boolean, TIMESTAMP, func, text

from ...db import Base

class REModePaiement(Base):
    __tablename__ = 're_mode_paiements'

    id = Column(BigInteger, primary_key = True)
    code = Column(String(225) , unique = True, nullable = False)
    libelle = Column(String(225))
    frais_pourcentage = Column(Numeric)
    delai_jours = Column(Integer)
    actif = Column(Boolean, default = True)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)