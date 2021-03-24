'''#!/usr/bin/python3'''

# Version 1.0
# BasicPortScanner
#   Super simple single host/port scanner. Lots of ideas to expand as i learn
#   more python.

import socket

txtName = "rayder13"
txtURL = "https://github.com/rayder13/BasicPortScanner"
scanTimeOut = 2

print(r"""
__________                 .__        __________  _________ 
\______   \_____     ______|__|  ____ \______   \/   _____/ 
 |    |  _/\__  \   /  ___/|  |_/ ___\ |     ___/\_____  \  
 |    |   \ / __ \_ \___ \ |  |\  \___ |    |    /        \ 
 |______  /(____  //____  >|__| \___  >|____|   /_______  / 
        \/      \/      \/          \/                  \/  """)
print("\n" +  txtName.center(60, '-'))
print("\n" +  txtURL.center(60, '-') + "\n")

# AF_INIT = IPv4 - AF_INIT6 used for IPv6
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set timeout between scans 
s.settimeout(scanTimeOut)

# get HOST and PORT
host = input("Host: ")
port = int(input("Port: "))

# basic scan function
def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

# initiate scan
portScanner(port)

# make sure socket is closed before script finish
s.close()
