from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class EDApi(Base):
    __tablename__ = 'ed_apis'

    id = Column(BigInteger, primary_key = True)
    nom = Column(String(225) )
    description = Column(Text )
    url_base = Column(String(225) )
    statut = Column(Enum('pending', 'canceled', 'validated') )
    documentation_url = Column(String(225) )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)