"""
Project :Xbee Wifi Connection 
Engineer : Nikhil.P.Lokhande
email:nikhil.l.1@aol.com

"""

import socket     # Wifi Xbee is using raw feed, hence a raw socket protocol


ip='255.255.255.255'               #Enter IP of your Xbee
p=9750                             #Enter the port number for your Xbee
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #Initialize socket object
s.connect((ip,p))                         #Connect to the Xbee


while(True):                      #Keep looping, receive then print the data
    data=s.recv(1024)
    print(data)
    

