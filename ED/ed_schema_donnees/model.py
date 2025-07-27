from sqlalchemy import Column, BigInteger,  String, TIMESTAMP, JSON, Enum, func, text


from ...enums import SchemaDonneesStatut
from ...db import Base

class EDSchemaDonnees(Base):
    __tablename__ = 'ed_schema_donneess'

    id = Column(BigInteger, primary_key = True)
    nom = Column(String(225), unique = True, nullable = False)
    version = Column(String(225))
    schema_json = Column(JSON)
    statut = Column(
        Enum(SchemaDonneesStatut),
        default = SchemaDonneesStatut.brouillon
    )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)