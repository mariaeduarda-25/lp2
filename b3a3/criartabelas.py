from sqlalchemy import *

from model.model import *

engine = create_engine("mysql+pymysql://primeiro_20202017612:cefetMG20202017612@primeiro.cefetvga.pro.br/primeiro_20202017612?charset=utf8mb4",echo=True)

usuario = Cliente.__table__
usuario.create(engine, checkfirst=True)

atividade = Editora.__table__
atividade.create(engine, checkfirst=True)

comentario = Livro.__table__
comentario.create(engine, checkfirst=True)

curtida = Compra.__table__
curtida.create(engine, checkfirst=True)