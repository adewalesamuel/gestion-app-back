from sqlalchemy import Column, Integer, BigInteger,  String, TIMESTAMP, func, text

from ...db import Base

class GUTypeDemande(Base):
    __tablename__ = 'gu_type_demandes'

    id = Column(BigInteger, primary_key = True)
    code = Column(String(225) , unique = True, nullable = False)
    libelle = Column(String(225))
    delai_traitement_jours = Column(Integer)
    cout = Column(Integer)
    validite_mois = Column(Integer)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)