from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class INPlanification(Base):
    __tablename__ = 'in_planifications'

    id = Column(BigInteger, primary_key = True)
    rc_engin_flottant_id = Column(BigInteger, ForeignKey('rc_engin_flottants.id', ondelete='CASCADE'), nullable = False)
    rc_engin_flottant = relationship('RCEnginFlottant', back_populates = 'in_planifications')
    in_checklist_id = Column(BigInteger, ForeignKey('in_checklists.id', ondelete='CASCADE'), nullable = False)
    in_checklist = relationship('INChecklist', back_populates = 'in_planifications')
    periodicite_jours = Column(Integer )
    prochaine_date = Column(Date )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)