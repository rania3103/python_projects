#!/usr/bin/python3
"""download video from web"""
from pytube import YouTube
url = input ("Enter the url of the video: ")
#download the video with highest resolution in the location you want
YouTube(url).streams.get_highest_resolution().download("desktop")
