# Imports to use the functions in DOW
from dow import getDayOfTheWeek
from dow import makeCalendar

# Prints out each day of the week of 2026
print(makeCalendar())

# Repeats the inputs
while True:
    # Inputs
    inputYear = str(input("Enter the year: "))
    inputMonth = str(input("Enter the month: "))
    inputDay = str(input("Enter the day: "))

    # Prints the result
    print(getDayOfTheWeek(inputYear, inputMonth, inputDay))
    print("===============================================")