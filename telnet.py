__author__ = 'Steve Morris'

# A basic telnet interface to be used either in this code or reused for things like whois calls

# Imports
import telnetlib

def telnet_connect(server, port):
    # Open a telnet server return a connection object
    connection = telnetlib.Telnet(server, port)
    return connection

myconnection = telnet_connect("whois.arin.net", 43)
myconnection.write("n 8.8.8.8\n")
print myconnection.read_all()
