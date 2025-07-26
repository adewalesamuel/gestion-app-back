from sqlalchemy import Column, BigInteger,  String, Date, TIMESTAMP, ForeignKey, func, text
from sqlalchemy.orm import relationship

from ...db import Base

class RCEquipement(Base):
    __tablename__ = 'rc_equipements'

    id = Column(BigInteger, primary_key = True)
    rc_engin_flottant_id = Column(BigInteger, ForeignKey('rc_engin_flottants.id', ondelete='CASCADE'), nullable = False)
    rc_engin_flottant = relationship('RCEnginFlottant', back_populates = 'rc_equipements')
    nom = Column(String(225))
    type = Column(String(225))
    numero_serie = Column(String(225), unique = True)
    date_installation = Column(Date)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)