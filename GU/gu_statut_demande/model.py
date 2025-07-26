from sqlalchemy import Column, Integer, BigInteger,  String, Boolean, TIMESTAMP, func, text

from ...db import Base

class GUStatutDemande(Base):
    __tablename__ = 'gu_statut_demandes'

    id = Column(BigInteger, primary_key = True)
    code = Column(String(225) , unique = True, nullable = False)
    libelle = Column(String(225))
    couleur_hex = Column(String(225))
    ordre = Column(Integer)
    notifiable = Column(Boolean, default = True)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)