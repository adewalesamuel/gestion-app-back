from sqlalchemy import Column, BigInteger,  Text, Date, TIMESTAMP, Enum, ForeignKey, Time, func, text
from sqlalchemy.orm import relationship

from ...enums import HistoriqueRelanceMode
from ...db import Base

class REHistoriqueRelance(Base):
    __tablename__ = 're_historique_relances'

    id = Column(BigInteger, primary_key = True)
    re_relance_id = Column(BigInteger, ForeignKey('re_relances.id', ondelete='CASCADE'), nullable = False)
    re_relance = relationship('RERelance', back_populates = 're_historique_relances')
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    user = relationship('User', back_populates = 're_historique_relances')
    date = Column(Date)
    heure = Column(Time)
    mode = Column(
        Enum(HistoriqueRelanceMode),
        default = HistoriqueRelanceMode.email
    )
    contenu = Column(Text)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)