from sqlalchemy import Column, Integer, BigInteger,  String, TIMESTAMP, Enum, func, text

from ...constants import TypeControleGraviteMin
from ...utils import flatten_const_values

from ...db import Base

class INTypeControle(Base):
    __tablename__ = 'in_type_controles'

    id = Column(BigInteger, primary_key = True)
    code = Column(String(225) , unique = True, nullable = False)
    libelle = Column(String(225))
    norme_reference = Column(String(225))
    frequence_mois = Column(Integer)
    gravite_min = Column(
         Enum(*flatten_const_values(TypeControleGraviteMin)),
         default = TypeControleGraviteMin.MINEURE
    )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)