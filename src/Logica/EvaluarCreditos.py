from src.Modelo.Asignatura import Asignatura
from src.Modelo.declarative_base import engine, Base, session
def __init__(self):
    Base.metadata.create_all(engine)
def evaluarCreditos(self,id,nombre,nota,credito,promedio,docente):
    busqueda = session.query(Asignatura).filter(Asignatura.id == id()).all()
    credito =

