from sqlalchemy import Column, BigInteger,  String, Text, Boolean, TIMESTAMP, ForeignKey, func, text
from sqlalchemy.orm import relationship

from ...db import Base

class INResultatItem(Base):
    __tablename__ = 'in_resultat_items'

    id = Column(BigInteger, primary_key = True)
    in_inspection_id = Column(BigInteger, ForeignKey('in_inspections.id', ondelete='CASCADE'), nullable = False)
    in_inspection = relationship('INInspection', back_populates = 'in_resultat_items')
    conforme = Column(Boolean, default = True)
    observations = Column(Text)
    checklist_item_code = Column(String(225))
    photo_url = Column(String(225), nullable = True)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)