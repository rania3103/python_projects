#!/usr/bin/python3
"""search for anything you want"""
from webbrowser import open
search = input("what do you want to search for? ")
open("https://www.google.com?q=" + search)
