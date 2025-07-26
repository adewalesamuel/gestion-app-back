from sqlalchemy import Column, BigInteger,  String, TIMESTAMP, JSON, ForeignKey, func, text
from sqlalchemy.orm import relationship

from ...db import Base

class INChecklist(Base):
    __tablename__ = 'in_checklists'

    id = Column(BigInteger, primary_key = True)
    rc_type_engin_id = Column(BigInteger, ForeignKey('rc_type_engins.id', ondelete='CASCADE'), nullable = False)
    rc_type_engin = relationship('RCTypeEngin', back_populates = 'in_checklists')
    nom = Column(String(225), unique = True, nullable = False)
    version = Column(String(225))
    items = Column(JSON)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)