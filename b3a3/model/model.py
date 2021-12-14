from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

class Cliente(Base):
    __tablename__= 'b3a3_cliente'

    id = Column(Integer, primary_key=True)
    endereco_cliente = Column(String(255), nullable=False)
    CPF = Column(String(45), nullable=False)
    telefone_cliente = Column(String(45), nullable=False)

    def _repr_(self):
        return f'Cliente {self.id}'

class Editora(Base):
    __tablename__= 'b3a3_editora'

    id = Column(Integer, primary_key=True)
    codigo = Column(String(45), nullable=False)
    endereco_editora = Column(String(45), nullable=False)
    telefone_editora = Column(String(45), nullable=False)
    gerente = Column(String(255), nullable=False)

    def _repr_(self):
        return f'Editora {self.codigo}'

class Livro(Base):
    __tablename__= 'b3a3_livro'

    id = Column(Integer, primary_key=True)
    id_editora = Column(Integer, ForeignKey('b3a3_editora.id'))
    autor = Column(String(255), nullable=False)
    assunto = Column(String(255), nullable=False)
    ISBN = Column(String(45), nullable=False)
    quantidade = Column(Integer, nullable=False)

    editora = relationship("Editora", backref="Livro")

    def _repr_(self):
        return f'Livro {self.autor}'

class Compra(Base):
    __tablename__ = 'b3a3_compra'

    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('b3a3_cliente.id'))
    id_livro = Column(Integer, ForeignKey('b3a3_livro.id'))
    data_compra = Column(DateTime, nullable=False)

    cliente = relationship("Cliente", backref="Compra")
    livro = relationship("Livro", backref="Compra")

    def _repr_(self):
        return f'Livro {self.id}'