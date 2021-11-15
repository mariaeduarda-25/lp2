from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.orm import base, relationship
from sqlalchemy.sql.sqltypes import DATETIME, DECIMAL, VARCHAR
class Usuario(Base):
    _tablename_ = 'usuario'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)

    nome = Column(String(25))
    publicacoes = relationship("Publicacao",backref='Usuario', lazy=True)

    def _repr_(self):
        return f'Usuario {self.nome}'

    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).one()