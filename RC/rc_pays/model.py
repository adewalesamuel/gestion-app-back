from sqlalchemy import Column, BigInteger,  String, TIMESTAMP, func, text

from ...db import Base

class RCPays(Base):
    __tablename__ = 'rc_payss'

    id = Column(BigInteger, primary_key = True)
    nom = Column(String(225), unique = True)
    code_iso = Column(String(225), unique = True)
    indicatif = Column(String(225), unique = True)
    pavillon_url = Column(String(225), nullable = True)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)