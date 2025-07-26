from sqlalchemy import Column, Integer, BigInteger,  String, Date, TIMESTAMP, Enum, ForeignKey, Time, func, text
from sqlalchemy.orm import relationship

from ...utils import flatten_const_values
from ...constants import LogEchangeTypeRequete
from ...db import Base

class EDLogEchange(Base):
    __tablename__ = 'ed_log_echanges'

    id = Column(BigInteger, primary_key = True)
    ed_api_id = Column(BigInteger, ForeignKey('ed_apis.id', ondelete='CASCADE'), nullable = False)
    ed_api = relationship('EDApi', back_populates = 'ed_log_echanges')
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 'ed_log_echanges')
    date_heure = Column(Date)
    heure = Column(Time)
    type_requete = Column(
        Enum(*flatten_const_values(LogEchangeTypeRequete)),
        default = LogEchangeTypeRequete.GET
    )
    endpoint = Column(String(225))
    statut_reponse = Column(Integer)
    temps_reponse_ms = Column(Integer)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)