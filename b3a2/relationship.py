from re import S
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import user

from model.model import *

engine = create_engine("mysql+pymysql://primeiro_20202017612:cefetMG202020176126@primeiro.cefetvga.pro.br/primeiro_20202017612?charset=utf8mb4",echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# #adicionando usuario 1 e  suas atividades
# usuario1 = Usuario(id=1, senha='123a', email='usu1@usu.com')

# atividade1 = Atividade(id=1, usuario=usuario1, data='2021-10-13', inicio='07:00:05', fim='10:05:04', local='VGA', tipo_atividade='Corrida', quilometragem=30.2)
# session.add(atividade1)

# atividade2 = Atividade(id=2, usuario=usuario1, data='2021-09-23', inicio='07:00:05', fim='10:05:04', local='VGA', tipo_atividade='Corrida', quilometragem=30.2)
# session.add(atividade2)

# atividade3 = Atividade(id=3, usuario=usuario1, data='2021-11-27'inicio='07:00:05', fim='10:05:04', local='VGA', tipo_atividade='Corrida', quilometragem=30.2)
# session.add(atividade3)

# #adicionando usuario 2 e suas atividades
# usuario2 = Usuario(id=2, senha='456b', email='usu2@usu.com')

# atividade4 = Atividade(id=4, usuario=usuario1, data='2021-05-01', inicio='07:00:05', fim='10:05:04', local='VGA', tipo_atividade='Corrida', quilometragem=30.2)
# session.add(atividade4)

# atividade5 = Atividade(id=5, usuario=usuario1, data='2021-02-25', inicio='07:00:05', fim='10:05:04', local='VGA', tipo_atividade='Corrida', quilometragem=30.2)
# session.add(atividade5)

# atividade6 = Atividade(id=6, usuario=usuario1, data='2021-04-20', inicio='07:00:05', fim='10:05:04', local='VGA', tipo_atividade='Corrida', quilometragem=30.2)
# session.add(atividade6)

# #adicionando usuario 3 e suas atividades
# usuario3 = Usuario(id=3, senha='789c', email='usu3@usu.com')

# atividade7 = Atividade(id=7, usuario=usuario1, data='2021-12-17', inicio='09:35:09', fim='11:40:22', local='VGA', tipo_atividade='Corrida', quilometragem=28.9)
# session.add(atividade7)

# atividade8 = Atividade(id=8, usuario=usuario1, data='2021-01-08', inicio='09:35:09', fim='11:40:22', local='VGA', tipo_atividade='Corrida', quilometragem=28.9)
# session.add(atividade8)

# atividade9 = Atividade(id=9, usuario=usuario1, data='2021-03-19', inicio='09:35:09', fim='11:40:22', local='VGA', tipo_atividade='Corrida', quilometragem=28.9)
# session.add(atividade9)

# #adicionando comentarios
# comentario1 = Comentario(id=1, usuario=usuario1, atividade=atividade2, texto_comentario="Fiquei super cansado!")
# session.add(comentario1)

# comentario2 = Comentario(id=2, usuario=usuario1, atividade=atividade3, texto_comentario="Gostei muito!")
# session.add(comentario1)

# comentario3 = Comentario(id=3, usuario=usuario3, atividade=atividade4, texto_comentario="Foi divertido!")
# session.add(comentario1)

# comentario4 = Comentario(id=4, usuario=usuario2, atividade=atividade7, texto_comentario="Tive uma experiência incrível!")
# session.add(comentario1)

# #adicionando curtidas
# curitda1 = Curtida(usuario=usuario1, atividade=atividade1)
# session.add(curitda1)

# curitda2 = Curtida(usuario=usuario1, atividade=atividade2)
# session.add(curitda2)

# session.commit()

tuplas = session.query(Atividade).order_by(Atividade.quilometragem) 

def select():
    for tuplas in session.query(Atividade).filter(Atividade.local=='VGA'):
        print(tuplas.usuario_id, "-" , tuplas.quilometragem, "-", tuplas.inicio, "-", tuplas.fim)

def update():
    Usuario.senha = "senhausu1"

def delete():
    for tuplas in session.query(Atividade).filter(Atividade.local=='VGA'):
        print("ENTREI")
        if tuplas.usuario_id == 'usu2@usu.com':
            print("deletei")
            var = tuplas.usuario_id
            session.delete(var)

delete()