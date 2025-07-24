from sqlalchemy import Column, Integer, Numeric, BigInteger,  String, Text, DateTime, Date, Boolean, TIMESTAMP, JSON, Enum, ForeignKey, func, text, inspect
from sqlalchemy.orm import relationship
from ...libs import crypto
from ...db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key = True)
    role_id = Column(BigInteger, ForeignKey('roles.id', ondelete='CASCADE'), nullable = False)
    role = relationship('Role', back_populates = 'users')
    rc_acteur_id = Column(BigInteger, ForeignKey('rc_acteurs.id', ondelete='CASCADE'), nullable = False)
    rc_acteur = relationship('RCActeur', back_populates = 'users')
    profil_img_url = Column(String(225) )
    nom = Column(String(225) )
    email = Column(String(225) , unique = True, nullable = False)
    password = Column(String(225) )
    last_login_date = Column(Date )
    last_login_heure = Column(String(225) )
    email_verified_at = Column(TIMESTAMP, default = None)

    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column(TIMESTAMP, default = None)