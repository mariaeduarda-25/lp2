from re import S
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import user

from model.model import *

engine = create_engine("mysql+pymysql://primeiro_20202017612:cefetMG20202017612@primeiro.cefetvga.pro.br/primeiro_20202017612?charset=utf8mb4",echo=True)

Session = sessionmaker(bind=engine)
session = Session()

#clientes
cliente1 = Cliente(id=1, endereco_cliente = "Varginha", CPF = '37010000', telefone_cliente = '988776655')
session.add(cliente1)

cliente2 = Cliente(id=2, endereco_cliente = "Lavras", CPF = '37020000', telefone_cliente = '988776655')
session.add(cliente2)

cliente3 = Cliente(id=3, endereco_cliente = "BH", CPF = '37030000', telefone_cliente = '988776655')
session.add(cliente3)

#editoras
editora1 = Editora(id=1, codigo = "345", endereco_editora = "Varginha", telefone_editora = "32233333", gerente = "Andre")
session.add(editora1)

editora2 = Editora(id=2, codigo = "346", endereco_editora = "Lavras", telefone_editora = "3223333", gerente = "Bruna")
session.add(editora2)

editora3 = Editora(id=3, codigo = "347", endereco_editora = "BH", telefone_editora = "3223333", gerente = "Caio")
session.add(editora3)

#livros
livro1 = Livro(id=1, editora=editora1, autor="Hal Elrod", assunto="Mudança de Vida", ISBN='1234', quantidade=60)
session.add(livro1)

livro2 = Livro(id=2, editora=editora1, autor="Jojo Moyes", assunto="Romance", ISBN='5678', quantidade=23)
session.add(livro2)

livro3 = Livro(id=3, editora=editora1, autor="William Young", assunto="Fé e Superação", ISBN='91011', quantidade=76)
session.add(livro3)

#compras
compra1 = Compra(id=1, cliente=cliente1, livro=livro2, data_compra='2021-12-08 13:40:04')
session.add(compra1)

compra2 = Compra(id=2, cliente=cliente3, livro=livro1, data_compra='2021-12-05 15:30:05')
session.add(compra2)

compra3 = Compra(id=3, cliente=cliente2, livro=livro3, data_compra='2021-12-06 18:00:15')
session.add(compra3)

session.commit()