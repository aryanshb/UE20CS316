#!/usr/bin/python3
from scapy.all import *
print("SNIFFING PACKETS...")
def print_pkt(pkt):
    pkt.show()
pkt = sniff(iface = "br-f2cc6eca9a5e",filter='src net 172.19.0.0/24', prn=print_pkt)


