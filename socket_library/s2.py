#!/usr/bin/python3
import socket 
"""get the ip address"""
url = input("Enter plz the url: ")
ipaddr = socket.gethostbyname(url)
print(ipaddr)
