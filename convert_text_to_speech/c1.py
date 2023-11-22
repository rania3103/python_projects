#!/usr/bin/python3
""" convert text to speech"""
from gtts import gTTS
from playsound import playsound
txt = "hello my name is rania"
x = gTTS(text= txt)
x.save("file.mp3") #save txt in file
playsound("file.mp3") #play the text in file
