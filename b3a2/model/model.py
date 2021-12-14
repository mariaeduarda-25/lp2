from enum import unique
from typing import Sequence, Text
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import Float, Time

Base = declarative_base()

class Usuario(Base):

    __tablename__ = 'b3a1_usuario'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    senha = Column(String(45), nullable=False)
    '''
    #referencia para atividade
    atividade = relationship("Atividade", backref='Usuario')
    comentario = relationship("Comentario", backref="Usuario")
    '''

    def _repr_(self):
        return f'Usuario {self.id}'

class Atividade(Base):

    __tablename__ = 'b3a1_atividade'

    id = Column(Integer, primary_key=True)
    
    usuario_id = Column(Integer, ForeignKey('b3a1_usuario.id'))

    data = Column(Date, nullable=False)
    inicio = Column(Time, nullable=False)
    fim = Column(Time, nullable=False)
    local = Column(String(45), nullable=False)
    tipo_atividade = Column(String(45), nullable=False)
    quilometragem = Column(Float, nullable=False)

    usuario = relationship("Usuario", backref="Atividade")

    def _repr_(self):
        return f'Atividade {self.inicio}'

class Comentario(Base):

    __tablename__ = 'b3a1_comentario'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('b3a1_usuario.id'))
    atividade_id = Column(Integer, ForeignKey('b3a1_atividade.id'))
    texto_comentario = Column(String(555), nullable = False)

    usuario = relationship("Usuario", backref="Comentario")
    atividade = relationship("Atividade", backref="Comentario")

    def _repr_(self):
        return f'Comentario {self.texto_comentario}'

class Curtida(Base):
    
    __tablename__ = 'b3a1_curtida'
    
    usuario_id = Column(Integer, ForeignKey('b3a1_usuario.id'), primary_key=True)
    atividade_id = Column(Integer, ForeignKey('b3a1_atividade.id'), primary_key=True)

    usuario = relationship("Usuario", backref="Curtida")
    atividade = relationship("Atividade", backref="Curtitda")

    def _repr_(self):
        return f'Curtida {self.usuario_id}'   
