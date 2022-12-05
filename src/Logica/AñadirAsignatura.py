from src.Modelo.Asignatura import Asignatura
from src.Modelo.declarative_base import engine, Base, session
def __init__(self):
    Base.metadata.create_all(engine)
def agregarAsignatura(self,id,nombre,nota,credito,promedio,docente):
    busqueda = session.query(Asignatura).filter(Asignatura.id == id()).all()
    if len(busqueda) == 0:
        asignatura = Asignatura(id,nombre,nota,credito,promedio,docente)
        session.add(asignatura)
        session.commit()
        return True
    else:
        return False
