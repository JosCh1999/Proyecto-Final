from sqlalchemy import Column, Integer, String, ForeignKey

from declarative_base import Base



class Asignatura(Base):
    __tablename__ = 'Asignatura'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    nota = Column(Integer)
    credito = Column(Integer)
    promedio = Column(Integer)
    docente = Column(Integer, ForeignKey('Docente.id'))