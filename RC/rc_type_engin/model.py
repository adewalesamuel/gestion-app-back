from sqlalchemy import Column, Integer, BigInteger,  String, TIMESTAMP, Enum, func, text

from ...enums import TypeEnginCategorie


from ...db import Base

class RCTypeEngin(Base):
    __tablename__ = 'rc_type_engins'

    id = Column(BigInteger, primary_key = True)
    code = Column(String(225) , unique = True, nullable = False)
    libelle = Column(String(225))
    categorie = Column(
        Enum(TypeEnginCategorie),
        default = TypeEnginCategorie.commerce
    )
    tonnage_min = Column(Integer)
    tonnage_max = Column(Integer)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)