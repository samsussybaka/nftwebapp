#!/usr/bin/env python3

import nmap

nmScan = nmap.PortScanner()

ip = input("ip address to scan: ")

nmScan.scan(ip, '21-443')

for host in nmScan.all_hosts():
    print('Host : %s (%s)' % (host, nmScan[host].hostname()))
    print('State : %s' % nmScan[host].state())
    for proto in nmScan[host].all_protocols():
        print('-----------')
        print('Protocol : $s' % proto)

        lport = nmScan[host][proto].keys()
        lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' % (port, nmScan[host][proto]['state'])


