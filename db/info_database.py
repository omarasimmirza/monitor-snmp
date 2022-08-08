import sqlalchemy as sql

base = sql.declarative_base()
class Stats(base):
    __tablename__ = "machines"
    ip = sql.Column('ip', sql.String, primary_key=True)
    port = sql.Column('port', sql.Integer)
    username = sql.Column('username', sql.String)
    mail = sql.Column('mail', sql.String)
    alert_type = sql.Column('alert_type', sql.String)
    alert_limit = sql.Column('alert_limit', sql.String)