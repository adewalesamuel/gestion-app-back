from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(BigInteger, primary_key = True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 'notifications')
    titre = Column(String(225) )
    message = Column(Text )
    lu = Column(Boolean )
    type = Column(Enum('pending', 'canceled', 'validated') )
    entite_type = Column(String(225) )
    entite_id = Column(Integer )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)