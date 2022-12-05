from src.Modelo.Asignatura import Asignatura
from src.Modelo.declarative_base import engine , Base , session
def __init__(self):
    Base.metadata.create_all(engine)

def EliminarAsignatura(self,id):
    try:
        asignatura = session.query(Asignatura).filter(Asignatura.id == id).first()
        session.delete(asignatura)
        session.commit()
        return True
    except:
        return False