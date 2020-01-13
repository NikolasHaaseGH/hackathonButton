import requests
import time
from pygame import mixer

previousLatestReleaseId = None
mixer.init()
mixer.music.load("/home/pi/Dokumente/hackApp/Sounds/WinningSound.mp3")

headers = {'content-type': 'application/json',
           'Authorization': 'Basic Onkzd3FjYWdhZWR2Mmh0Y3hwNm8yM3NjY2lzYWdmYnp0cnd6M2RzYmg0anl5cmZ5YTNubmE='}

url = 'https://vsrm.dev.azure.com/prolan365/AzureButton/_apis/release/releases'

while True:
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
            mixer.music.play()
        else:
            print("failed")
    else:
        print("noting changed")
        
    
    time.sleep(10)







#environment = latestRelease['environments'][len(environments)-1]
#print(environment['status'])
