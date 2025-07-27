from sqlalchemy import Column, BigInteger,  String, Text, TIMESTAMP, Enum, func, text


from ...enums import ApiStatut
from ...db import Base

class EDApi(Base):
    __tablename__ = 'ed_apis'

    id = Column(BigInteger, primary_key = True)
    nom = Column(String(225), unique = True, nullable = False)
    description = Column(Text)
    url_base = Column(String(225))
    statut = Column(
        Enum(ApiStatut),
        default = ApiStatut.actif
    )
    documentation_url = Column(String(225))

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)