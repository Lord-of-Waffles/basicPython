from datetime import date
from calendar import monthrange

def print_month_calendar(year, month):
    #arrays for storing weekdays, months
    month_names = ["", "January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    weekdays = ["", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    tracker = 0

    days_in_month = monthrange(year, month)[1]
    #initialising object array
    day_object_array = []

    #loop to add day objects to array
    for i in range(1, days_in_month + 1):
        date_object = date(year, month, i)
        day_object_array.append(date_object)

    #printing code
    print()
    print(f" > {month_names[month]} {year} <")
    for i in range(1, len(weekdays)):
        print(f"{weekdays[i]:>4}", end='')
    print()

    for day in day_object_array:
        day_of_week = day.weekday() + 1
        if day_of_week == 1 or day.day == 1:
            tracker += 1

        if day.day == 1:
            print("    " * (day_of_week - 1), end="") 
        print(f"{day.day:>4}", end="")
        if day_of_week == 7:
            print()
        if day.day == days_in_month and days_in_month % 4 != 0:
            print()
        elif day.day == days_in_month and tracker > 4:
            print()
       
    
#take input and call function
def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    print_month_calendar(year, month)

main()
