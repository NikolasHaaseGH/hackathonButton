#!/usr/home/documents/python3

import RPi.GPIO as GPIO
import subprocess
import time
from pygame import mixer
from signal import pause

BUZZER = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZER, GPIO.IN, GPIO.PUD_DOWN)

mixer.init()
mixer.music.load("/home/pi/Dokumente/hackApp/Sounds/WinningSound.mp3")

def runPipelineScript(channel):
        mixer.music.play()
        subprocess.call([r'/home/pi/Dokumente/hackApp/publish/AzureCalls'])

GPIO.add_event_detect(BUZZER, GPIO.RISING,runPipelineScript, bouncetime=400)

while True:
    time.sleep(10)