# Calendar Prayer Time Automator
### What is this?
There are many Islamic prayer time mobile apps out there, however, I found myself forgetting to open the app to check the prayer times thus forgetting to offer my prayers. However, as most adamant Apple users do, I utilized the Apple Calendar daily as a way to schedule my university classes and other commitments. For this reason, I thought that having the prayer times in the Apple Calendar would be extremely useful. The problem I had was that adding every prayer time manually would be extremely tedious as it would involve checking the prayer time online then making a calendar event for each one. As there are 5 prayers in a day and their times change every day, this would take an extremely long time to get even 1 month's prayer times inputted. 

This automation script was created as a way to automate adding all those prayer times using Python and Apple Scripts. The way it works is, the Python script makes an API call to the [Al Adhan API](https://aladhan.com/prayer-times-api) endpoint which returns an entire months prayer times based on the location, month and year provided to it. This data is then parsed to the correct formats and terminal command is called to run the Apple Script for each prayer of every day. The Apple Script creates a new event at the time of the prayer for a length of 5 minutes so that it is visible in the calendar. 

A potential user would be able to input their country, city, calendar name, month and year to input prayer times which would be used for the API call. 

### How long does it take?
Through development testing, the average time it takes to input 1 month of prayer times is 77 seconds or 1 minute and 17 seconds. This is the average of 10 test inputs. 

### How do I use it?
1. Clone the repository
2. `cd` into the cloned repository
3. Run `pip install requests`
4. Create a new Calendar in your Apple Calendar and remember it's name
5. Run `python3 bot.py`
6. Follow the prompts
