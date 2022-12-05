from sqlalchemy import Column, Integer, String, ForeignKey

from declarative_base import Base


class Matricula(Base):
    __tablename__ = 'Matricula'

    id = Column(Integer, primary_key=True)
    fecha = Column(String)
    Estudiante = Column(Integer, ForeignKey('estudiante.id'))
    Asignatura = Column(Integer, ForeignKey('Asignatura.id'))