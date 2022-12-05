from sqlalchemy import Column, Integer, String, ForeignKey
from declarative_base import Base

<<<<<<< HEAD
class Asignatura(Base):
=======


class asignatura(Base):
>>>>>>> 82ee579b9ee03fcd430a3a7e07644e4d990273d8
    __tablename__ = 'Asignatura'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    nota = Column(Integer)
    credito = Column(Integer)
    promedio = (nota*credito)/credito
<<<<<<< HEAD
    docente = Column(Integer, ForeignKey('Docente.id'))
=======
    docente = Column(Integer, ForeignKey('Docente.id'))
>>>>>>> 82ee579b9ee03fcd430a3a7e07644e4d990273d8
