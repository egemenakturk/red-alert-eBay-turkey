# RedAlert-eBay.sh

import requests
# import simplejson as json
import serial
import time

folder_api_urls = ['https://jenkins2.app.gittigidiyor.net/job/QA/job/E2E-PROD/job/RESP/api/json',
                   'https://jenkins2.app.gittigidiyor.net/job/QA/job/E2E-PROD/job/WEB/api/json']
job_api_urls = []
job_failure = []
teams = []
headers = {'Authorization': 'Basic bXlhbWFuOjQyMThjMDRmNjJjZWFhMzAwYmVlMzg2YjBhZmRjMjZl'}

while True:
    try:
        # hc_07 = serial.Serial('/dev/tty.HC-05-SPPDev', 9600)
        #merge_requests_alert = serial.Serial('/dev/tty.HC-06-SPPDev', 9600)
        dota_test_fail_alert = serial.Serial('/dev/tty.HC-06-SPPDev-1', 9600)
        break
    except Exception:
        print()

def isJob(data , x) :
    if len(data["jobs"][x]) == 3:
        return 0
    else:
        return 1
    
def select_roots(folder_api_urls, job_api_urls, job_failure):
    data = requests.get(folder_api_urls[0], headers=headers).json()
    length = len(data["jobs"])
    for x in range(0, length):
        if isJob(data, x) == 0:
            folder_api_urls.append(data["jobs"][x]["url"] + "api/json")
            print(data["jobs"][x]["url"] + "api/json")
        else:
            if data["jobs"][x]["color"] == "red":
                full_name = data["jobs"][x]["name"]
                team_name = full_name.split("-")
                job_failure.append(team_name[0])
    del folder_api_urls[0]
    if len(folder_api_urls) == 0:
        return
    else:
        select_roots(folder_api_urls, job_api_urls, job_failure)


def job_results(job_api_urls, job_failure):
    while len(job_api_urls) != 0:
        data = requests.get(job_api_urls[0], headers=headers).json()
        result_data = requests.get(data["builds"][0]["url"] + "api/json").json()
        if result_data["result"] == "FAILURE":
            full_name = result_data["fullDisplayName"].split(" ")
            team_split = full_name[len(full_name) - 2].split("-")
            job_failure.append(team_split)
        del job_api_urls[0]
    return

def send_message(job_failure):
    team_name = job_failure[0]
    print(team_name)
    dota_test_fail.write(b'6')
    time.sleep(1.1)
    del job_failure[0]
    if len(job_failure) == 0:
        return
    else:
        send_message(job_failure)

select_roots(folder_api_urls, job_api_urls, job_failure)
job_results(job_api_urls , job_failure)
send_message(job_failure)
print("-----FINISHED-----")