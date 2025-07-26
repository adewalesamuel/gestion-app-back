from sqlalchemy import Column, Integer, BigInteger,  String, TIMESTAMP, ForeignKey, func, text
from sqlalchemy.orm import relationship

from ...db import Base

class GUWorkflow(Base):
    __tablename__ = 'gu_workflows'

    id = Column(BigInteger, primary_key = True)
    role_id = Column(BigInteger, ForeignKey('roles.id', ondelete='CASCADE'), nullable = False)
    role = relationship('Role', back_populates = 'gu_workflows')
    gu_type_demande_id = Column(BigInteger, ForeignKey('gu_type_demandes.id', ondelete='CASCADE'), nullable = False)
    gu_type_demande = relationship('GUTypeDemande', back_populates = 'gu_workflows')
    etape = Column(String(225))
    ordre = Column(Integer)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)