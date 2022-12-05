from sqlalchemy import Column, Integer, String, ForeignKey

from declarative_base import Base

class Usuario(Base):
    __tablename__ = 'Usuario'

    usuario = Column(String)
    contraseña = Column(String)
