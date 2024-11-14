from datetime import date
from calendar import monthrange

def print_month_calendar(year, month):
    #arrays for storing weekdays, months
    month_names = ["", "January", "February", "March", "April", "May","June",
    "July", "August", "September", "October", "November", "December"]
    weekdays = ["", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


    days_in_month = monthrange(year, month)[1]
    #initialising object array
    day_object_array = []

    #loop to add day objects to array
    for i in range (0, days_in_month, 1):
        date_object = date(year, month, i)
        day_object_array.append = date_object
                        

   

    #printing code
    print()
    print(f" > {month_names[month]} {year} < ")
    for i in range(1, len(weekdays), 1):
        print(f"{weekdays[i]}", end='')
    for i in range(0, 7, 1):
        #some if statement matching date and day name, then prent
        for i in range(1, days_in_month + 1):
            day_of_week = date(year, month, i).weekday() + 1
            if i == 1:
                print("    " * (day_of_week - 1), end="")
            print(f"{i:2} ", end="")
            if day_of_week == 7:
                print()



#take input and call function
def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    print_month_calendar(year, month)

main()