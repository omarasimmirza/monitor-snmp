from fastapi import UploadFile
import mysql
import paramiko 
import sys, os 
from tempfile import TemporaryDirectory
import smtplib
from email.message import EmailMessage
import Crypto
import xml.etree.cElementTree as et
import getpass

class SystemCheck:
    def __init__(self, ip, port, user, password, mail):
        self.ip = ip 
        self.port = port 
        self.user = user 
        self.password = password 
        self.mail = mail
        self.type = ""
        self.limit = ""

    def parse_xml(self, filename):
        try:
            tree = et.parse(filename)
            root = tree.getroot()
            client_num = len(root)
            print("\nThe number of total clients are: ", client_num)
            for child in root:
                self = SystemCheck(
                    child.attrib.get("id"), 
                    child.attrib.get("port"), 
                    child.attrib.get("username"), 
                    child.attrib.get("password"), 
                    child.attrib.get("mail"))
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
        remotepath = "info-client.py"
        path = r"C:\Users\Administrator\Documents\crossover-proj\info-client.py"
        try:
            client = paramiko.Transport((self.ip, self.port))
            client.banner_timeout = 10
            client.connect(username=self.user, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(client)
            sftp.mkdir('upload')
            sftp.chdir('upload')
            sftp.put(path, remotepath)
            sftp.close()
            client.close()
        except Exception as e:
            print(e)

    def ssh_connect(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.ip, self.port, self.user, self.password)
        self.upload_file()       
        client.exec_command("cd upload/")
        client.exec_command("python3 info-client.py") #Take a look at this buddy.
        client.close()
    
    



