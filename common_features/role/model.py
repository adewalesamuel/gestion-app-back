from sqlalchemy import Column, BigInteger,  String, Text, TIMESTAMP, JSON, func, text

from ...db import Base

class Role(Base):
    __tablename__ = 'roles'

    id = Column(BigInteger, primary_key = True)
    name = Column(String(225), unique = True)
    description = Column(Text, nullable = True)
    permissions = Column(JSON)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)