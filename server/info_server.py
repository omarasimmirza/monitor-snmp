import libserver
from db.db_methods import insert_to_table
from db.db_model import Stats
from libserver import SystemCheck

list_of_machines = SystemCheck().parse_xml("data.xml")
for checker in list_of_machines:
    data = checker.ssh_connect()
    for items in data:
        print(items)

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

    insert_to_table(add_this)
    checker.email_user()