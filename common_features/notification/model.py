from sqlalchemy import Column, Integer, BigInteger,  String, Text, Boolean, TIMESTAMP, Enum, ForeignKey, func, text
from sqlalchemy.orm import relationship

from ...utils import flatten_const_values
from ...db import Base
from ...constants import NotificationType

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(BigInteger, primary_key = True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 'notifications')
    titre = Column(String(225), nullable = False)
    message = Column(Text)
    lu = Column(Boolean, default = True)
    type = Column(
        Enum(*flatten_const_values(NotificationType)),
        default = NotificationType.INFO)
    entite_type = Column(String(225))
    entite_id = Column(Integer)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)