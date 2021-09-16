import os
import requests
from requests import api
import time

# user inputs
country = input("What is your country?\n")
city = input("What is your city?\n")
calendar_name = input("What is the name of the calendar you would like to add prayer times to?\n")
month = input("What month would you like to input prayer times for? (Enter a number)\n")
year = input("What year would you like to input prayer times for?\n")

#api endpoint based on user inputs
APIURL = f'https://api.aladhan.com/v1/calendarByCity?city={city}&country={country}&method=2&month={month}&year={year}'


# api call
response = requests.get(APIURL)

data = response.json()

api_data = data["data"]

# parses string prayer time given by api into a list of hours and minutes
def parseApiPrayerTime(str):
    sliced = str[0:5]
    
    arr_strings = sliced.split(":")

    return arr_strings

# parses date given by api into MM-DD-YY format
def parseApiDate(api_date):
    year = api_date["year"][2:]
    month = str(api_date["month"]["number"]) if  api_date["month"]["number"] >= 10 else "0" + str(api_date["month"]["number"])
    day = api_date['day']

    return f"{month}-{day}-{year}"



# loop through all days given by api
for i in range(0, len(api_data)):
    # destructuring timings and date
    timings = api_data[i]['timings']
    date = api_data[i]['date']

    # MM-DD-YY date using helper function
    parsedDate = parseApiDate(date["gregorian"])

    # iterate over keys in prayer times for that day
    for key in timings:
        # times for that prayer [hours, minutes]
        times_arr = parseApiPrayerTime(timings[key])
        
        # only want the 5 main prayers
        if key == "Fajr" or key == "Dhuhr" or key == "Asr" or key == "Maghrib" or key == "Isha":
            
            hours = int(times_arr[0])
            minutes = int(times_arr[1])
            
            # terminal call to apple script passing in all arguments
            system_call = f'osascript add_event.scpt "{calendar_name}" "{parsedDate}" {hours} {minutes} "{key}"'
            
            os.system(system_call)



    

    

            


