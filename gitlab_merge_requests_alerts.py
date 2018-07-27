# RedAlert-eBay.sh
#9bQeZz2socxJ2aowMCtJ

import requests
# import simplejson as json
import serial
import time

while True:
    try:
        # hc_07 = serial.Serial('/dev/tty.HC-05-SPPDev', 9600)
        merge_requests_alert = serial.Serial('/dev/tty.HC-06-SPPDev', 9600)
        # dota_test_fail = serial.Serial('/dev/tty.HC-06-SPPDev-1', 9600)
        break
    except Exception:
        print()

data = requests.get("http://git.app.gittigidiyor.net/api/v4/projects/488/merge_requests?state=opened&private_token=9bQeZz2socxJ2aowMCtJ",).json()
print(len(data))

if len(data) > 0:
    merge_requests_alert.write(b'6')
