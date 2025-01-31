from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base, engine

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telefono = Column(String, unique=True, index=True, nullable=False)
    dni = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    incendios = relationship("Incendio", back_populates="usuario")

class Incendio(Base):
    __tablename__ = "incendios"

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    latitud = Column(Float, nullable=False)
    longitud = Column(Float, nullable=False)
    intensidad = Column(Float)
    tamano = Column(Float, nullable=False)
    fecha_hora_adq = Column(DateTime)
    temperatura = Column(Float, nullable=False)

    usuario = relationship("Usuario", back_populates="incendios")

def create_tables():
    Base.metadata.create_all(engine)
