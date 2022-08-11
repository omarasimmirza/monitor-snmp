from db.db_methods import insert_to_table
from db.db_model import Stats
from libserver import SystemCheck
import xml.etree.cElementTree as et

def parse_xml(filename):
    try:
        list_of_machines = []
        tree = et.parse(filename)
        root = tree.getroot()
        for child in root:
            machine = SystemCheck()
            machine.alert = []
            machine.ip = child.attrib.get("ip")
            machine.port = int(child.attrib.get("port"))
            machine.user = child.attrib.get("username")
            machine.password = child.attrib.get("password")
            machine.mail = child.attrib.get("mail")
            if len(child) > 0:
                alert_dict = dict()
                for alert_child in child:
                    alert_type = alert_child.attrib.get("type")
                    alert_dict[alert_type] = alert_child.attrib.get("limit")
                machine.alert.append(alert_dict)
            list_of_machines.append(machine)
    except Exception:
        print("Error: XML file not found.")
    for items in list_of_machines:
        print(items.ip)
    return list_of_machines

list_of_machines = parse_xml("data.xml")

for checker in list_of_machines:
    data = checker.ssh_connect()
    
    for items in data:
        print(items)
        
    print(checker.alert)

    add_this = Stats(
        ip=checker.ip,
        port=checker.port,
        username=checker.user,
        mail=checker.mail,
        cpu_uptime=data[2],
        cpu_usage=data[1],
        memory_usage=data[0],
        # alert_type=checker.type,
        # alert_limit=checker.limit
    )

    insert_to_table(add_this)
    # checker.email_user()