from sqlalchemy import Column, BigInteger,  String, Date, TIMESTAMP, Enum, ForeignKey, func, text
from sqlalchemy.orm import relationship

from ...constants import CertificatType
from ...utils import flatten_const_values

from ...db import Base

class RCCertificat(Base):
    __tablename__ = 'rc_certificats'

    id = Column(BigInteger, primary_key = True)
    rc_engin_flottant_id = Column(BigInteger, ForeignKey('rc_engin_flottants.id', ondelete='CASCADE'), nullable = False)
    rc_engin_flottant = relationship('RCEnginFlottant', back_populates = 'rc_certificats')
    type = Column(
        Enum(*flatten_const_values(CertificatType)),
        default = CertificatType.NAVIRE
    )
    numero = Column(String(225), unique = True)
    date_emission = Column(Date)
    date_expiration = Column(Date)
    organisme_emetteur = Column(String(225))

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)