<<<<<<< HEAD
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
=======
from src.Modelo.Asignatura import asignatura
from src.Modelo.declarative_base import engine , Base , session

class AgregarAsigntura():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agrega_asig(self,nombre,nota,credito,promedio,docente):
        busqueda=session.query(asignatura).filter(asignatura.nombre==nombre).all()
        if len(busqueda) == 0:
            Asignatura=asignatura(nombre=nombre,nota=nota,credito=credito,promedio=promedio,docente=docente)
            session.add(Asignatura)
            session.commit()
            return True
        else:
            return False
>>>>>>> 82ee579b9ee03fcd430a3a7e07644e4d990273d8
