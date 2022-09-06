from unittest import result
from xmlrpc.client import DateTime
import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

target = input(str("Target IP: "))

print("-" * 50)
print("Scanning Target: " + target)
print("Scan started at: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(440, 3000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting")
    sys.exit()
except socket.error:
    print("\n Host not responding")
    sys.exit()
