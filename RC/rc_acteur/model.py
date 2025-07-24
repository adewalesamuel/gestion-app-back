from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class RCActeur(Base):
    __tablename__ = 'rc_acteurs'

    id = Column(BigInteger, primary_key = True)
    type = Column(Enum('pending', 'canceled', 'validated') )
    nom = Column(String(225) )
    prenom = Column(String(225) )
    raison_sociale = Column(String(225) )
    registre_commerce = Column(String(225) )
    email = Column(String(225) , unique = True, nullable = False)
    adresse = Column(String(225) )
    telephone = Column(String(225) )
    secteur_activite = Column(String(225) )
    pays_origine = Column(String(225) )

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)