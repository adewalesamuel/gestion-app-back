from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class EDSchemaDonnees(Base):
    __tablename__ = 'ed_schema_donneess'

    id = Column(BigInteger, primary_key = True)
    nom = Column(String(225) )
    version = Column(String(225) )
    schema_json = Column(JSON)
    statut = Column(Enum('pending', 'canceled', 'validated') )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)