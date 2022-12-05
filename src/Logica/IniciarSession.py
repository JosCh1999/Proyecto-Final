<<<<<<< HEAD
from src.Modelo.Usuario import Usuario
from src.Modelo.declarative_base import engine, Base, session

def __init__(self):
    Base.metadata.create_all(engine)
def IniciarSession(self,usuario,contraseña):
    busqueda = session.query(Usuario).filter(Usuario.usuario == usuario()).all()
    if len(busqueda)==0:
        Usuario.usuario = usuario
        Usuario.contraseña = contraseña
        session.commit()
        return True
    else:
        return False
=======
from src.Modelo.Usuario import Usuario
from src.Modelo.declarative_base import engine, Base, session

def __init__(self):
    Base.metadata.create_all(engine)
def IniciarSession(self,usuario,contraseña):
    busqueda = session.query(Usuario).filter(Usuario.usuario == usuario()).all()
    if len(busqueda)==0:
        Usuario.usuario = usuario
        Usuario.contraseña = contraseña
        session.commit()
        return True
    else:
        return False
>>>>>>> 82ee579b9ee03fcd430a3a7e07644e4d990273d8
