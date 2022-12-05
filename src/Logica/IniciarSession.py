from src.Modelo.Usuario import Usuario
from src.Modelo.declarative_base import engine, Base, session

def __init__(self):
    Base.metadata.create_all(engine)
def IniciarSession(self,usuario,contrasena):
    busqueda = session.query(Usuario).filter(Usuario.usuario == usuario()).all()
    if len(busqueda)==0:
        Usuario.usuario = usuario
        Usuario.contrasena = contrasena
        session.commit()
        return True
    else:
        return False