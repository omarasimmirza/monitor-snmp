import libserver
from db import db_connection
from dotenv import load_dotenv
import os 

checker = libserver.SystemCheck()
checker.parse_xml("data.xml")
checker.ssh_connect()
# load_dotenv()
# store = db_connection.MySQL_connect(os.environ.get("user"), os.environ.get("password"), os.environ.get("server"))
# store.create_connection()

# class machines(store.db.Model):
#     ip = store.db.Column(store.db.Integer)