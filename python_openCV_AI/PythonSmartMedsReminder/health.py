#!/usr/bin/python3
""""""
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime

time = input("Enter the time plz to take your medecines(format h:m:s): ")
alarm = AudioSegment.from_mp3("sounds/alarm.mp3")
play(alarm)
while True:
    tim = datetime.now()
    now = tim.strftime("%H:%M:%S") # format time
    if now == time:
        alarm2 = AudioSegment.from_mp3("sounds/alarm2.mp3")
        play(alarm2)
    if now > time:
        break