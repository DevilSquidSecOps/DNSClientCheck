import wmi
import sys

program_name = sys.argv[0]
ip = sys.argv[1]
c = wmi.WMI(computer=f'{ip}')
try:
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        print(f"Description: {interface.Description},\nMAC:{interface.MACAddress},\nIP/IPv6:{interface.IPAddress},\nDNS Servers:{interface.DNSServerSearchOrder}")
except Exception as e:
    print(e)
