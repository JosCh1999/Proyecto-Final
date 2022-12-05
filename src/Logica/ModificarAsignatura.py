from src.Modelo.Docente import Docente
from src.Modelo.Asignatura import Asignatura
from src.Modelo.declarative_base import engine , Base , session
def __init__(self):
    Base.metadata.create_all(engine)
def editarAsignatura(self,id,nombre,nota,credito,promedio,docente):
    busqueda = session.query(Asignatura).filter(Asignatura.nombre==nombre, Asignatura.id!=id).all()
    if len(busqueda)==0:
        Asignatura=session.query(Asignatura).filter(Asignatura.id==Asignatura.id),first()
        Asignatura.nombre=nombre
        Asignatura.nota=nota
        Asignatura.credito=credito
        Asignatura.docente=docente
        Asignatura.promedio=promedio
        session.commit()
        return True
    else:
        return False