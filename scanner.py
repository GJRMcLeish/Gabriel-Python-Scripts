#!/bin/python3

#python3 scanner.py <ip>, Scans through a selected port range and will return back results e.g. port 80 is open etc

import sys #import system module
import socket #import socket module
from datetime import datetime #import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translates hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Start banner 
print("-" * 50) #prints 50 dashes
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50) #prints 50 dashes

#Try statement
#Scan range = e.g.(1,50), 
try:
	for port in range(50,85): # for loop iterate .scans ports 50 to 85, can be modified
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Attempt to connect to IPv4 IP and a port
		socket.setdefaulttimeout(0.30) # Waits one second, then moves on
		result = s.connect_ex((target,port)) #connects to target and port,open =0 closed =1
		#enable this to see how fast scanner is running, and how many ports are open in real time
		#print("Checking port {} is open".format(port))
		if result == 0:
			print("Port {} is open".format(port))# if that port is 0, print this statement
		s.close() # closing connection, iterates again trying to connect to next port until loop ends

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit() #Alows ctrl c exit

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()# If no hostname resolution, exits the program

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()#If it can't conect to IP address specific, exit program
	
#end banner 
print("-" * 50) #prints 50 dashes
print("Scanning target "+target)
print("Scanning finished: "+str(datetime.now()))
print("-" * 50) #prints 50 dashes
