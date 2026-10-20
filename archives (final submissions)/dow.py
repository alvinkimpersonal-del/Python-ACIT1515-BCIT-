# List for days of the week & dict
dayOfTheWeek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
monthCodeList = {"January": 1, "February": 4, "March": 4, "April": 0, "May": 2, "June": 5, "July": 0, "August": 3, "September": 6, "October": 1, "November": 4, "December": 6}
yearOffsetsCode = {1600: 6, 1700: 4, 1800: 2, 1900: 0, 2000: 6, 2100: 4}
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 30, 31]

# Calculation for leap year
def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Gets day of the week
def getDayOfTheWeek(year, month, day):
    leapYear = isLeapYear(int(year)) # Checks if the year is a leap year
    yearLastDigits = year[-2:] # Grabs the last two digits of the year
    yearLastDigits = int(yearLastDigits) # Converts the year to an int

    # Checks the year offset
    dateOffset = int(year[:2]) * 100
    offsetCode = yearOffsetsCode[dateOffset]

    # Dividing the year by 12
    yearDivided = int(yearLastDigits/12)

    # Finds the remainder from the last two digits of the year
    yearRemainder = yearLastDigits % 12

    # Dividing "yearRemainder" by 4
    yearFours = int(yearRemainder/4)

    # Month codes
    monthCode = monthCodeList[month]

    # Adds up everything
    totalAdded = yearDivided + yearRemainder + yearFours + int(day) + monthCode + offsetCode

    # Does the leap year adjustment
    if leapYear and (month == "January" or month == "February"):
        totalAdded -= 1

    # Mods the toal by 7
    totalAdded = totalAdded % 7

    # Returns the date
    return dayOfTheWeek[totalAdded]

# Prints out every day of the week of the year of 2026
def makeCalendar():
   # Month/Day/Year is a day
   month = 1
   day = 1
   year = 2026

    # Month counter does not go over 12 months
   while month <= 12:
        # Ensures that the day counter does not go over the amount of days in a month
       while day <= daysInMonth[month-1]:
           monthName = list(monthCodeList)[month -1] # Gets the month
           dayOfTheWeek = getDayOfTheWeek(str(year), monthName, day) # Finds the day for the date
           print(f"{day}-{month}-{year} is a {dayOfTheWeek}") # Print statement
           day += 1 # Increases the day by 1 within the month
       day = 1 # Resets the  counter to 1 for a new month
       month += 1 # Increases the month counter by 1
