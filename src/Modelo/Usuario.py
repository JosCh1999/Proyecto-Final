from sqlalchemy import Column, Integer, String, ForeignKey
<<<<<<< HEAD

from declarative_base import Base

class Usuario(Base):
    __tablename__ = 'Usuario'

    usuario = Column(String)
    contraseña = Column(String)
=======
>>>>>>> 82ee579b9ee03fcd430a3a7e07644e4d990273d8

from declarative_base import Base

class Usuario(Base):
    __tablename__ = 'Usuario'

    usuario = Column(String)
    contraseña = Column(String)
