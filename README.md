# monitor-snmp
Monitor client machine statistics using snmp. Use socket and paramiko modules to communicate between server and client

pip install python-dotenv

You will need to create a .xml file inside the server folder and include the list of machines and their data in this manner:
<?xml version='1.0' encoding='utf-8'?>
<data>
    <client ip='{ip here}' port='{port number here}' username='{username here}' password='{password here}' mail='{email here}'>
        <alert type="memory" limit="50%"/>
        <alert type="cpu" limit="20%"/>
    </client>
    <!-- <client ip='' port='' username='ubuntu' password='' mail=''>
        <alert type="memory" limit="50%"/>
        <alert type="cpu" limit="20%"/>
    </client> -->
</data>

In the db folder, you will need to create a .env file and include the database credentials in this manner:
user = '{user in database}'
password = '{database password}'
server = '{the server to connect to}'
database = '{the database name}'