#!/usr/home/documents/python3

import RPi.GPIO as GPIO
import subprocess
import time
from pygame import mixer
from signal import pause
import requests

BUZZER = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZER, GPIO.IN, GPIO.PUD_DOWN)

mixer.init()

headers = {'content-type': 'application/json',
           'Authorization': 'Basic Onkzd3FjYWdhZWR2Mmh0Y3hwNm8yM3NjY2lzYWdmYnp0cnd6M2RzYmg0anl5cmZ5YTNubmE='}
url = 'https://vsrm.dev.azure.com/prolan365/AzureButton/_apis/release/releases'


def runPipelineScript(channel):
        mixer.music.load("/home/pi/Dokumente/hackApp/Sounds/ButtonPushed.mp3")
        mixer.music.play()
        subprocess.call([r'/home/pi/Dokumente/hackApp/publish/AzureCalls'])

previousLatestReleaseId = None
def checkReleaseStatus():
    r = requests.get(url, headers=headers)

    rJson = r.json()
    releases = rJson["value"]
    latestRelease = releases[0]['id']

    url1 = 'https://vsrm.dev.azure.com/prolan365/AzureButton/_apis/release/releases/'+ str(latestRelease)
    r1 = requests.get(url1, headers=headers)
    environments = r1.json()['environments']
    environment = environments[len(environments)-1]
    
    if previousLatestReleaseId != latestRelease:
        previousLatestReleaseId = latestRelease
        
        if environment['status'] == "succeeded":
            print("success")
            mixer.music.load("/home/pi/Dokumente/hackApp/Sounds/WinningSound.mp3")
            mixer.music.play()
        else:
            print("failed")
            mixer.music.load("/home/pi/Dokumente/hackApp/Sounds/Failure.mp3")
            mixer.music.play()
    else:
        print("noting changed")
#GPIO.add_event_detect(BUZZER, GPIO.RISING,runPipelineScript, bouncetime=400)

while True:
    input_state = GPIO.input(BUZZER)
    if input_state == False:
        print("call")
        runPipelineScript("")
        
    checkReleaseStatus()
    time.sleep(10)