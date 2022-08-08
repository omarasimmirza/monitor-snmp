import sqlalchemy as sql

base = sql.declarative_base()
class Stats(base):
    __tablename__ = "machines"
    ip = sql.Column(sql.String, primary_key=True)