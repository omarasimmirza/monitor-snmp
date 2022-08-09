import os
import libserver
from db.db_methods import insert_to_table
from db.info_model import Stats
# from dotenv import load_dotenv

checker = libserver.SystemCheck()
checker.parse_xml("data.xml")
data = checker.ssh_connect()
# load_dotenv()
for item in data:
    print(item)
add_this = Stats(
    ip=checker.ip,
    port=checker.port,
    username=checker.user,
    mail=checker.mail,
    cpu_uptime=data[2],
    cpu_usage=data[1],
    memory_usage=data[0],
    alert_type=checker.type,
    alert_limit=checker.limit
)
# ip = Column(String(255), primary_key=True)
# port = Column(Integer)
# username = Column(String(255))
# mail = Column(String(255))
# cpu_uptime = Column(Float)
# cpu_usage = Column(Float)
# memory_usage = Column(Float)
# alert_type = Column(String(255))
# alert_limit = Column(String(255))
insert_to_table(add_this)
# store = db.db_methods.MySQL_connect(os.environ.get("user"), os.environ.get("password"), os.environ.get("server"))
# store.create_connection()
# store.create_database()
# store.create_table()