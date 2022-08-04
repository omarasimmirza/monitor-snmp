import psutil, uptime
import os
from pysnmp.entity.rfc3413.oneliner import cmdgen
# import libserver

# _oid_memory_usage = '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.7'
# _oid_cpu_usage = '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5'
# _oid_total_uptime = '1.3.6.1.2.1.1.3'
# _oid_test = '.1.3.6.1.2.1.1.1.0'

class Stats:
    def __init__(self, memory_used, cpu_used, total_uptime):
        self.memory_used = memory_used
        self.cpu_used = cpu_used
        self.total_uptime = total_uptime

results = []

cmdGen = cmdgen.CommandGenerator()
errorIndication, errorStatus, errorIndex, varBinds = cmdGen.nextCmd(
    cmdgen.CommunityData('public'),
    cmdgen.UdpTransportTarget(('localhost', 161)),
    '1.3.6.1.4.1.2021.11.53'
 )
if errorIndication:
    print(errorIndication)
else:
    if errorStatus:
        print('%s at %s' %(
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?'
        ))
    else:
        for lines in varBinds:
            for name, val in lines:
                results.append(val)
    if len(results) == 1:
        print(results[0])
        print('also here')
    else:
        print(results)