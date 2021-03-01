from scapy.all import IP
from scapy.all import sniff
from scapy.layers import http

import re
# Extracting all URLS
def processStr(data):
#    pattern = re.compile('^b\'(.*?)\'$', re.S)
#    res = re.findall(pattern, str(data))
#    final = re.split('\\\\r\\\\n', res[0]a)
    final = re.split('\\\\r\\\\n', data)
    return final

def sniff_urls(packet):
    if 'Raw' in packet:
        src = packet['IP'].src
        dst = packet['IP'].dst
        sport = packet['TCP'].sport
        dport = packet['TCP'].dport
        seq = packet['TCP'].seq
        ack = packet['TCP'].ack
        print("{}({})->{}({}), seq={},ack={}".format(src, sport, dst, dport, seq, ack))
        load = packet['Raw'].load.decode("utf-8","ignore")
        items = processStr(load)
        for i in items:
            print(i)

    packet.show()

    print("-"*80)

#sniff(filter='tcp port 8000 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)', prn=sniff_urls)
sniff(filter='tcp port 8000', prn=sniff_urls)

