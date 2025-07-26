from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship

from ...db import Base

class ConfigSysteme(Base):
    __tablename__ = 'config_systemes'

    id = Column(BigInteger, primary_key = True)
    parametre = Column(String(225))
    valeur = Column(Text)
    module = Column(String(225))
    editable = Column(Boolean, default = True)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)