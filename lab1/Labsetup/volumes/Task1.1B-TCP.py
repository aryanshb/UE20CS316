#!/usr/bin/python3
from scapy.all import *
print ("SNIFFING PACKETS...")
def print_pkt(pkt):
    pkt.show()
pkt = sniff (iface = "br-f2cc6eca9a5e",filter='tcp and src host 10.9.0.6 and dst port 23', prn=print_pkt)

