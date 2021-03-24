'''#!/usr/bin/python3'''

import socket

txtName = "rayder13"

print(r"""
__________                 .__        __________  _________ 
\______   \_____     ______|__|  ____ \______   \/   _____/ 
 |    |  _/\__  \   /  ___/|  |_/ ___\ |     ___/\_____  \  
 |    |   \ / __ \_ \___ \ |  |\  \___ |    |    /        \ 
 |______  /(____  //____  >|__| \___  >|____|   /_______  / 
        \/      \/      \/          \/                  \/  """)
print("\n************************************************************")
print("\n" +  txtName.center(60))
print("\n************************************************************")

# AF_INIT = IPv4 - AF_INIT6 used for IPv6
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 5 second timeout between scans
s.settimeout(5)

# get HOST and PORT
host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))

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
