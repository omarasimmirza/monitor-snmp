import mysql
import paramiko 
import smtplib
from email.message import EmailMessage
import xml.etree.cElementTree as et
# import getpass

class SystemCheck:
    def __init__(self, ip=None, port=None, user=None, password=None, mail=None):
        self.ip = ip 
        self.port = port 
        self.user = user 
        self.password = password 
        self.mail = mail
        self.type = ""
        self.limit = ""

    def print_self(self):
        print(self.ip)
        print(self.port)
        print(self.user)
        print(self.password)
        print(self.mail)

    def parse_xml(self, filename):
        try:
            tree = et.parse(filename)
            root = tree.getroot()
            client_num = len(root)
            print("The number of total clients are: ", client_num)
            for child in root:
                self.ip = child.attrib.get("ip")
                self.port = int(child.attrib.get("port"))
                self.user = child.attrib.get("username")
                self.password = child.attrib.get("password")
                self.mail = child.attrib.get("mail")
                if len(child) > 0:
                    for alert_child in child:
                        self.type = alert_child.attrib.get("type")
                        if self.type == "memory":
                            self.limit = alert_child.attrib.get("limit")
                        elif self.type == "cpu":
                            self.limit = alert_child.attrib.get("limit")
        except Exception:
            print("Error: XML file not found.")

    def upload_file(self):
        client_file = "info-client.py"
        client_lib = "libclient.py"
        path_file = r"C:\Users\Administrator\Documents\crossover-proj\info-client.py"
        path_lib = r"C:\Users\Administrator\Documents\crossover-proj\libclient.py"
        try:
            client = paramiko.Transport((self.ip, self.port))
            client.banner_timeout = 10
            client.connect(username=self.user, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(client)
            sftp.mkdir('upload')
            sftp.chdir('upload')
            sftp.put(path_file, client_file)
            sftp.put(path_lib, client_lib)
            sftp.close()
            client.close()
        except Exception as e:
            print(e)

    def ssh_connect(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.ip, self.port, self.user, self.password)
        self.upload_file()       
        stdin, stdout, stderr = client.exec_command("cd upload/;python3 info-client.py")
        for lines in stdout.readlines():
            print(lines)
        for lines in stderr.readlines():
            print(lines)
        client.exec_command('sudo rm -rf upload/')
        client.close()