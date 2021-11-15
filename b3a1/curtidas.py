from typing import Text
from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.orm import base, relationship
from sqlalchemy.sql.sqltypes import DATETIME, DECIMAL, INT, VARCHAR

class Atividade(base):
     tablename = "curtida"
     id = Column[INT](Integer, Sequence('publicação_id_seq'), primary_key= True)
     texto = Column (Text(100))
     usuario_id = Column(Integer, ForeignKey('usuario_id_seq'))
     atividade_id = Column(Integer, ForeignKey('usuario_id_seq'))

     Usuario = relationship("Usuario", backref= "Atividade")

     def _repr_(self):
        return f'Curtida {self.data}'