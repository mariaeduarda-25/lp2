from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.orm import base, relationship
from sqlalchemy.sql.sqltypes import DATETIME, DECIMAL, VARCHAR

class Atividade(base):
    tablename = "publicação"
    id = Column (Integer, Sequence('publicação_id_seq'), primary_key= True)
    data = Column(DATETIME)
    hora_inicial = Column(DATETIME)
    hora_final  = Column(VARCHAR(45))
    tipo = Column(VARCHAR(45))
    local = Column(VARCHAR(45))
    km_percorridos = Column(DECIMAL)
    usuario_id = Column(Integer, ForeignKey('usuario_id_seq'))

    Usuario = relationship("Usuario", backref= "Atividade")

    def _repr_(self):
        return f'Publicacao {self.data}'