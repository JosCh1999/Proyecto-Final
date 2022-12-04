from sqlalchemy import Column, Integer, String, ForeignKey

from declarative_base import Base


class Docente(Base):
    __tablename__ = 'Docente'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    telefono = Column(String)
    correo = Column(String)