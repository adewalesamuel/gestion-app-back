from sqlalchemy import Column, Integer, BigInteger,  String, TIMESTAMP, Enum, func, text

from ...enums import TarifFrequence
from ...db import Base

class RETarif(Base):
    __tablename__ = 're_tarifs'

    id = Column(BigInteger, primary_key = True)
    service = Column(String(225))
    montant = Column(Integer)
    devise = Column(String(225))
    frequence = Column(
        Enum(TarifFrequence),
        default = TarifFrequence.mensuelle
    )
    type_acteur = Column(String(225))

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)