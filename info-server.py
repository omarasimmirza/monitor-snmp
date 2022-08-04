import libserver
import os

checker = libserver.SystemCheck('10.8.128.39', 22, 'ubuntu', 'fawazA5AD2%', 'omar8786270@gmail.com')

checker.ssh_connect()
# print(os.getcwd() + r"\info-client.py")