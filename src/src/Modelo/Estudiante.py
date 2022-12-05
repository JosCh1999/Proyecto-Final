from sqlalchemy import Column, Integer, String, ForeignKey
from declarative_base import Base


class Estudiamte(Base):
    __tablename__ = 'Estudiante'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    genero = Column(String)
    fechanacimiento = Column(String)