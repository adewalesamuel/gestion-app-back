from sqlalchemy import Column, BigInteger,  String, TIMESTAMP, func, text

from ...db import Base

class EDFormatDonnees(Base):
    __tablename__ = 'ed_format_donneess'

    id = Column(BigInteger, primary_key = True)
    nom = Column(String(225), unique = True, nullable = False)
    mime_type = Column(String(225))
    schema_xsd_url = Column(String(225))
    exemple_url = Column(String(225))

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)