import os
import requests
from requests import api
import time

country = "Canada" #input("What is your country?\n")
city = "Waterloo" #input("What is your city?\n")
calendar_name = "complete-time" #input("What is the name of the calendar you would like to add prayer times to?\n")
month = 9 #input("What month would you like to input prayer times for? (Enter a number)\n")
year = 2021 #input("What year would you like to input prayer times for?\n")


APIURL = f'https://api.aladhan.com/v1/calendarByCity?city={city}&country={country}&method=2&month={month}&year={year}'

for i in range(10):

    start_time = time.time()

    response = requests.get(APIURL)

    data = response.json()

    api_data = data["data"]


    def parseApiPrayerTime(str):
        sliced = str[0:5]
        
        arr_strings = sliced.split(":")

        return arr_strings


    def parseApiDate(api_date):
        year = api_date["year"][2:]
        month = str(api_date["month"]["number"]) if  api_date["month"]["number"] >= 10 else "0" + str(api_date["month"]["number"])
        day = api_date['day']

        return f"{month}-{day}-{year}"




    for i in range(0, len(api_data)):
        timings = api_data[i]['timings']
        date = api_data[i]['date']

        parsedDate = parseApiDate(date["gregorian"])

        for key in timings:
            times_arr = parseApiPrayerTime(timings[key])
            
            if key == "Fajr" or key == "Dhuhr" or key == "Asr" or key == "Maghrib" or key == "Isha":
                
                hours = int(times_arr[0])
                minutes = int(times_arr[1])
                
                
                system_call = f'osascript add_event.scpt "{calendar_name}" "{parsedDate}" {hours} {minutes} "{key}"'
                
                os.system(system_call)

    end_time = time.time()

    file = open("complete_time.txt", "a")
    file.write(f"\n{end_time - start_time}")

    print(f"Time to complete: {end_time - start_time}")

            


