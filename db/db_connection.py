import sqlalchemy as sql

class MySQL_connect:
    def __init__(self, user, password, server):
        self.user = user
        self.password = password
        self.server = server
        self.connection = None
    
    def create_connection(self):
        engine = sql.create_engine(f'mysql://{self.user}:{self.password}@{self.server}')
        self.connection = engine.connect()
        

    def create_database(self):
        self.connection.execute("create database if not exists crossover;")
        self.connection.execute("use crossover;")       
    
    def create_table(self):
        self.connection.execute("create table if not exists machines ("
                            + "ip varchar(255), "
                            + "port int, "
                            + "username varchar(255), "
                            + "mail varchar(255), "
                            + "alert_type varchar(255), "
                            + "alert_limit varchar(255), "
                            + "primary key (ip));")
    def insert_to_table(self, ip, port, user, mail, alert_type, alert_limit):
        query = sql.insert("machines").values(ip=ip, port=port, user=user, mail=mail, alert_type=alert_type, alert_limit=alert_limit)