import ipaddress
import sys

if len(sys.argv) != 2:
    print("Usage: python ip_analysis.py <IP>")
    sys.exit(1)

ip = sys.argv[1]

try:
    address = ipaddress.ip_address(ip)

    print("IP Address:", address)
    print("Version:", address.version)
    print("Private:", address.is_private)
    print("Global:", address.is_global)
    print("Loopback:", address.is_loopback)

except ValueError:
    print("Invalid IP address")