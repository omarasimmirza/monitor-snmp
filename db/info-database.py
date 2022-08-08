import sqlalchemy

class MySQL_connect:
    def __init__(self, user, password, server):
        self.user = user
        self.password = password
        self.server = server
    
    def create_connection(self):
        engine = sqlalchemy.create_engine(f'mysql://{self.user}:{self.password}@{self.server}')
        engine.execute("create database if not exists crossover;")
        engine.execute("use crossover;")       