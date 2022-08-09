from platform import machine
from sqlalchemy import create_engine
from .info_model import Stats
from .db_connection import session, engine
from sqlalchemy.orm import sessionmaker

# class MySQL_connect:
#     def __init__(self, user, password, server):
#         self.user = user
#         self.password = password
#         self.server = server
#         self.connection = None
    
# def create_connection(self):
#     self.connection = create_engine(f'mysql://{self.user}:{self.password}@{self.server}')
    # self.connection = engine.connect()
    # app = Flask(__name__)
    # app.config['SECRET_KEY']='SuperSecretKey'
    # app.config['SQLALCHEMY_DATABASE_URI'] = self.connection
    # self.db = SQLAlchemy(app)

# def create_database():
#     engine.execute("create database if not exists crossover;")

# def create_table():
#     engine.execute("use crossover;")       
    # self.connection.execute("create table if not exists machines ("
    #                     + "ip varchar(255), "
    #                     + "port int, "
    #                     + "username varchar(255), "
    #                     + "mail varchar(255), "
    #                     + "cpu_uptime float, "
    #                     + "cpu_usage float, "
    #                     + "memory_usage float, "
    #                     + "alert_type varchar(255), "
    #                     + "alert_limit varchar(255), "
    #                     + "primary key (ip));")
    
def insert_to_table(info:Stats):
    try:
        session.add(info)
        session.commit()
        print(f"Created new record for {info.ip}")
        # return info
    except Exception as e:
        print(e)