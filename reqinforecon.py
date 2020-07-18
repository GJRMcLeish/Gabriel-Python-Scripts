#Python Banner grabber
#Hostname lookup
#IP Lookup
#Basic usage python <script name>

#Request module, make a GET request to a serevr and print the response
#When one makes a request, the response headers reveal important info about the server

#Embellishment, prints out a small banner where the text will be in bold, multiple options available in the class


print("-" * 22)
print("Python Banner Grabber: ") #Simple to switch from bold with a colour of choice or set it to default with end.
print("-" * 22)
print("\n" *2) #Spaces things out a bit 
import sys #We need this module when performing command line arguments
#If the requests module is not installed, install it with "pip install requests" as its not in the standard python library
import requests #imports the request module as we will be making GET requests to a website
import socket #imports the socket module
import json #imports the json module

#We provide a Command Line Argument which contains the address of the site we want to grab the banner for
    # We will do a simple check and display message if there is no argument provided in the CL

#Provides basic help message if no arguments provided
    #If the message says argv(0)
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1) # exits system

#Here the domain functionality is coded
#Set a variable of req, make a get request, to the URL we supply from the command line
req = requests.get("https://"+sys.argv[1]) #Domain we input is appended to the request, as sys.argv(0) is the name of the script, so when we get a 1 aka true, we print the results of the headers
print("\n"+str(req.headers)) #Prints the result of the requests headers
#Banner grab Script complete


#Hostname retrieval
    #We will use the socket module 

#This function fetches our host name
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+gethostby_ + "\n") #Prints the IP address of the banner, appends the hostname to it and displays them together

#IP Lookup
    #We want the location of the IP for our domain
    #We want the latitude and longitude (the location)
        #We will make an API request which provides this service
            #That API is called "ipinfo.io"
            #In python modules are often used and API's to ehance scripts

#performs a second GET request to the API Service 
req_two = requests.get("https://ipinfo.io/"+gethostby_+"/json") # We call the API, provide the IP address, and we wan our response in json format
#This is how a request should look like, we can mamipulate json, with the json module 
resp_ = json.loads(req_two.text) #The load function loads the response
#We will now print the location, the city and the region
print("location: "+resp_['loc']) #Loc is the index whcih provides location
print("region: "+resp_['region']) #Prints region
print("city: "+resp_['city']) #Prints city
print("country: "+resp_['country']) #Prints country