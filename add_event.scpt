on run {calendarName, prayerDate, prayerHour, prayerMinute, prayerName}

    set theStartDate to date prayerDate
    set hours of theStartDate to prayerHour
    set minutes of theStartDate to prayerMinute
    set seconds of theStartDate to 0
    set theEndDate to theStartDate + (5 * minutes)
    
    tell application "Calendar"
        tell calendar calendarName
            make new event with properties {summary: prayerName, start date:theStartDate, end date:theEndDate}
        end tell      
    end tell
end run