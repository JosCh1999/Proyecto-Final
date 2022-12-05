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
