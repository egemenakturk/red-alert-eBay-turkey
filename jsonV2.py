#RedAlert-eBay

import requests
import simplejson as json
import serial
import time

folder_api_urls = ['https://jenkins2.app.gittigidiyor.net/job/QA/job/E2E-PROD/job/RESP/api/json',
                   'https://jenkins2.app.gittigidiyor.net/job/QA/job/E2E-PROD/job/WEB/api/json',
                   'https://jenkins2.app.gittigidiyor.net/job/PAPI/api/json',
                   'https://jenkins2.app.gittigidiyor.net/job/GG/job/NOTIFICUS/api/json']
job_api_urls = ['https://jenkins2.app.gittigidiyor.net/job/GG/job/GGWEB/job/master/api/json',
                'https://jenkins2.app.gittigidiyor.net/job/GG/job/ZF/job/master/api/json']
job_failure = []
teams = ["bzg", "maste"]
headers = {'Authorization': 'Basic bXlhbWFuOjQyMThjMDRmNjJjZWFhMzAwYmVlMzg2YjBhZmRjMjZl'}

while True:
    try:
        #hc_07 = serial.Serial('/dev/tty.HC-05-SPPDev', 9600)
       # hc_06 = serial.Serial('/dev/tty.HC-06-SPPDev', 9600)
        hc_05 = serial.Serial('/dev/tty.HC-06-SPPDev-1', 9600)
        break
    except Exception:
        print()

def get_jobs (folder_api_urls, job_api_urls, job_failure):
    data = requests.get(folder_api_urls[0],headers=headers).json()
    length = len(data["jobs"])
    for x in range(0, length):
        if len(data["jobs"][x]) == 3:
            folder_api_urls.append(data["jobs"][x]["url"] + "api/json")
        else:
            if data["jobs"][x]["color"] == "red":
                team_name = data["jobs"][x]["name"]
                team_split = team_name.split("-")
                print(team_split[0])
                if team_split[0] == teams[0]:

                    #hc_07.write(b'6')
                    time.sleep(1.1)
                if team_split[0] == teams[1]:

                   # hc_06.write(b'6')
                    time.sleep(1.1)
                else:

                    hc_05.write(b'6')
                    time.sleep(1.1)
    del folder_api_urls[0]
    if len(folder_api_urls) == 0:
        return
    else:
        get_jobs(folder_api_urls, job_api_urls, job_failure)


def job_results (job_api_urls):
    while len(job_api_urls) != 0:
        data = requests.get(job_api_urls[0], headers=headers).json()
        result_data = requests.get(data["builds"][0]["url"] + "api/json").json()
        if result_data["result"] == "FAILURE":
            full_name = result_data["fullDisplayName"].split(" ")
            team_split = full_name[len(full_name)-2].split("-")
            print(team_split[0])
            if team_split[0] == teams[0]:
                #hc_07.write(b'6')
                time.sleep(1.1)
            if team_split[0] == teams[1]:
                #hc_06.write(b'6')

                time.sleep(1.1)
            else:
                hc_05.write(b'6')
                time.sleep(1.1)
        del job_api_urls[0]
    return



get_jobs(folder_api_urls, job_api_urls, job_failure)
job_results(job_api_urls)


