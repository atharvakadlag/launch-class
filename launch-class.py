from datetime import datetime, timedelta
import json
import os
import time
time.sleep(5)

def load_links(file_name = "classlinks.json"):
    # load the given json file
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data

def get_current_class():
    detla = timedelta(minutes=30)
    now = datetime.now() + detla

    day = datetime.today().strftime("%A").lower()
    data = load_links()[day]

    hours = now.strftime("%H")
    minutes = now.strftime("%M")

    now_str = str(hours).zfill(2) + ":" + str(minutes).zfill(2)
    now = datetime.strptime(now_str, "%H:%M")

    for key in data.keys():
        times = key.split("-")
        start_time = times[0]
        start_time = datetime.strptime(times[0], "%H:%M")
        end_time = datetime.strptime(times[1], "%H:%M")
        
        if now >= start_time and now <= end_time:
            return data[key]

def main():
    current_class = get_current_class()
    classname = " ".join([i.capitalize() for i in current_class["name"].split("-")])
    print(current_class["link"])
    if current_class is None:
        print('[-] No class right now')
        return
    print(f'[+] launching {classname}')
    os.system(f'brave {current_class["link"]}')
    return
