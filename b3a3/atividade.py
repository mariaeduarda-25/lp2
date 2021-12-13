import sqlalchemy as db


engine = db.create_engine("mysql+pymysql://primeiro_20202017612:cefetMG20202017612@localhost/primeiro_20202017612")
connection = engine.connect ()


metadata = db.MetaData()