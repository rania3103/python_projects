#!/usr/bin/python3
import socket 
"""get the fully qualified domain name"""
hn = socket.getfqdn("8.8.8.8")
print(hn)
