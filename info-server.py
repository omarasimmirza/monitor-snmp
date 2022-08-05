import libserver

checker = libserver.SystemCheck()
checker.parse_xml("data.xml")
checker.ssh_connect()