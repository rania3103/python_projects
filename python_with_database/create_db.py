#!/usr/bin/python3
"""create database"""
from mysql.connector import connect, Error
try:
    con = connect(host="localhost", user = "root", password = "")
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS rania")
except Error as er:
    print(er)
