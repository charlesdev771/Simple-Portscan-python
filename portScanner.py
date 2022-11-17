#!/usr/bin/python

##====================================================================##
##                                                                    ##
## SOFTWARE: PortScan python.                                         ##
## AUTHOR: Charles Dantas (ccod)                                 ##
## VERSION: 0.1                                                       ##
## CREATION DATE: 03/06/2022                                          ##
##                                                                    ##
##====================================================================##

import socket


class Portscanner: #Main class

    def main(self):
        self.scan()#Call the scan function

    def scan(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket
        ip = input("Enter with the ip: ")
        for port in range(1, 65535): #Generates the 65535 tcp ports
            if sock.connect_ex((ip, port)) == 0: #Check if the port is open
                print("Port: {} Open.".format(port))
            else:
                print("Port {} close.".format(port))
        sock.close() #Close the connection


scanner = Portscanner()
scanner.main()
